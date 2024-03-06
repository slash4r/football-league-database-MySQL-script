create schema assignment_2;
use assignment_2;

CREATE TABLE Leagues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    num_teams INT NOT NULL,
    country VARCHAR(255)
);


CREATE TABLE Teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    stadium VARCHAR(255) NOT NULL,
    manager VARCHAR(255) NOT NULL,
    league_id INT,
    FOREIGN KEY (league_id) REFERENCES Leagues(id)
);

CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE,
    nationality VARCHAR(255),
    position VARCHAR(50),
    number INT
);

-- Junction 
CREATE TABLE Team_Player (
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    PRIMARY KEY (team_id, player_id),
    FOREIGN KEY (team_id) REFERENCES Teams(id),
    FOREIGN KEY (player_id) REFERENCES Players(player_id)
);

CREATE TABLE Seasons (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

# ALTER TABLE matches DROP FOREIGN KEY matches_ibfk_3;
# ALTER TABLE match_days MODIFY COLUMN id INT AUTO_INCREMENT;
# ALTER TABLE matches ADD CONSTRAINT matches_ibfk_3 FOREIGN KEY (match_day_id) REFERENCES match_days (id);

CREATE TABLE Match_days (
    id INT AUTO_INCREMENT PRIMARY KEY,
    season_id INT NOT NULL,
    league_id INT NOT NULL,
    day_number INT NOT NULL CHECK (day_number > 0),
    CONSTRAINT season2league2day_unique UNIQUE (season_id, league_id, day_number),
    FOREIGN KEY (season_id) REFERENCES Seasons(id),
    FOREIGN KEY (league_id) REFERENCES Leagues(id)
);

CREATE TABLE Matches (
    id INT PRIMARY KEY,
    date_time DATETIME NOT NULL,
    venue VARCHAR(255) NOT NULL,
    home_team_id INT,
    away_team_id INT,
    home_score INT NOT NULL,
    away_score INT NOT NULL,
    match_day_id INT NOT NULL,
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id),
    FOREIGN KEY (match_day_id) REFERENCES match_days(id)
);

CREATE TABLE Goals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        match_id INT,
        player_id INT,
        team_id INT,
        time TIME NOT NULL ,
        FOREIGN KEY (match_id) REFERENCES Matches(id),
        FOREIGN KEY (player_id) REFERENCES Players(player_id),
        FOREIGN KEY (team_id) REFERENCES Teams(id)
);

CREATE TABLE standings (
    match_day_id INT NOT NULL,
    team_id INT NOT NULL,
    points INT NOT NULL,
    played INT NOT NULL,
    won INT NOT NULL,
    drawn INT NOT NULL,
    lost INT NOT NULL,
    goals_for INT NOT NULL,
    goals_against INT NOT NULL,
    PRIMARY KEY (match_day_id, team_id),
    FOREIGN KEY (team_id) REFERENCES Teams(id)
);
