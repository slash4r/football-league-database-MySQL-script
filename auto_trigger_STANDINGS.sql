CREATE TRIGGER update_standings_after_insert
    AFTER INSERT ON Matches
    FOR EACH ROW
BEGIN
    -- Update standings for the home team
    INSERT INTO standings (match_day_id, team_id, points, played, won, drawn, lost, goals_for, goals_against)
    VALUES (
               NEW.match_day_id,
               NEW.home_team_id,
               CASE
                   WHEN NEW.home_score > NEW.away_score THEN 3
                   WHEN NEW.home_score = NEW.away_score THEN 1
                   ELSE 0
                   END,
               1,
               CASE WHEN NEW.home_score > NEW.away_score THEN 1 ELSE 0 END,
               CASE WHEN NEW.home_score = NEW.away_score THEN 1 ELSE 0 END,
               CASE WHEN NEW.home_score < NEW.away_score THEN 1 ELSE 0 END,
               NEW.home_score,
               NEW.away_score
           );

    -- Update standings for the away team
    INSERT INTO standings (match_day_id, team_id, points, played, won, drawn, lost, goals_for, goals_against)
    VALUES (
               NEW.match_day_id,
               NEW.away_team_id,
               CASE
                   WHEN NEW.away_score > NEW.home_score THEN 3
                   WHEN NEW.away_score = NEW.home_score THEN 1
                   ELSE 0
                   END,
               1,
               CASE WHEN NEW.away_score > NEW.home_score THEN 1 ELSE 0 END,
               CASE WHEN NEW.away_score = NEW.home_score THEN 1 ELSE 0 END,
               CASE WHEN NEW.away_score < NEW.home_score THEN 1 ELSE 0 END,
               NEW.away_score,
               NEW.home_score
           );
END;
