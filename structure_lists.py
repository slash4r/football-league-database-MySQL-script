# Populate Leagues table
leagues_data = [
    ("Premier League", 20, "England"),
    ("La Liga", 20, "Spain"),
    ("Bundesliga", 18, "Germany"),
    ("Serie A", 20, "Italy"),
    ("Ligue 1", 20, "France"),
    ("Primeira Liga", 18, "Portugal"),
    ("Eredivisie", 18, "Netherlands"),
    ("Ukrainian Premier League", 16, "Ukraine"),
    # Add more leagues as needed
]

teams_data = [
    # Premier League teams
    ("Manchester City", "Manchester", "Etihad Stadium", "Pep Guardiola", 1),
    ("Liverpool", "Liverpool", "Anfield", "Jurgen Klopp", 1),
    ("Chelsea", "London", "Stamford Bridge", "Thomas Tuchel", 1),
    ("Manchester United", "Manchester", "Old Trafford", "Ole Gunnar Solskjaer", 1),
    # Add more Premier League teams as needed

    # La Liga teams
    ("Real Madrid", "Madrid", "Santiago Bernabeu", "Carlo Ancelotti", 2),
    ("Barcelona", "Barcelona", "Camp Nou", "Xavi Hernandez", 2),
    ("Atletico Madrid", "Madrid", "Wanda Metropolitano", "Diego Simeone", 2),
    ("Sevilla", "Seville", "Ramón Sánchez Pizjuán", "Julen Lopetegui", 2),
    # Add more La Liga teams as needed

    # Bundesliga teams
    ("Bayern Munich", "Munich", "Allianz Arena", "Julian Nagelsmann", 3),
    ("Borussia Dortmund", "Dortmund", "Signal Iduna Park", "Marco Rose", 3),
    ("RB Leipzig", "Leipzig", "Red Bull Arena", "Jesse Marsch", 3),
    ("Bayer Leverkusen", "Leverkusen", "BayArena", "Gerardo Seoane", 3),
    # Add more Bundesliga teams as needed

    # Serie A teams
    ("Juventus", "Turin", "Allianz Stadium", "Massimiliano Allegri", 4),
    ("Inter Milan", "Milan", "San Siro", "Simone Inzaghi", 4),
    ("AC Milan", "Milan", "San Siro", "Stefano Pioli", 4),
    ("Napoli", "Naples", "Stadio Diego Armando Maradona", "Luciano Spalletti", 4),
    # Add more Serie A teams as needed

    # Ligue 1 teams
    ("Paris Saint-Germain", "Paris", "Parc des Princes", "Mauricio Pochettino", 5),
    ("Lille", "Lille", "Stade Pierre-Mauroy", "Jocelyn Gourvennec", 5),
    ("Marseille", "Marseille", "Stade Vélodrome", "Jorge Sampaoli", 5),
    ("Lyon", "Lyon", "Groupama Stadium", "Peter Bosz", 5),
    # Add more Ligue 1 teams as needed

    # Primeira Liga teams
    ("Porto", "Porto", "Estádio do Dragão", "Sérgio Conceição", 6),
    ("Benfica", "Lisbon", "Estádio da Luz", "Jorge Jesus", 6),
    ("Sporting Lisbon", "Lisbon", "Estádio José Alvalade", "Rúben Amorim", 6),
    ("Braga", "Braga", "Estádio Municipal de Braga", "Carvalhal", 6),
    # Add more Primeira Liga teams as needed

    # Eredivisie teams
    ("Ajax", "Amsterdam", "Johan Cruyff Arena", "Erik ten Hag", 7),
    ("PSV Eindhoven", "Eindhoven", "Philips Stadion", "Roger Schmidt", 7),
    ("Feyenoord", "Rotterdam", "De Kuip", "Arne Slot", 7),
    ("AZ Alkmaar", "Alkmaar", "AFAS Stadion", "Pascal Jansen", 7),
    # Add more Eredivisie teams as needed

    # Ukrainian Premier League teams
    ("Shakhtar Donetsk", "Donetsk", "Donbass Arena", "Roberto De Zerbi", 8),
    ("Dynamo Kyiv", "Kyiv", "NSC Olimpiyskiy", "Mircea Lucescu", 8),
    ("Zorya Luhansk", "Luhansk", "Slavutych-Arena", "Viktor Skrypnyk", 8),
    ("Dnipro-1", "Dnipro", "Dnipro-Arena", "Miron Markevich", 8),
    # Add more Ukrainian Premier League teams as needed
]

players_data = [
    # Premier League players
    # Manchester City
    [
        ("Kevin De Bruyne", "1991-06-28", "Belgian", "Midfielder", 17),
        ("Raheem Sterling", "1994-12-08", "English", "Forward", 7),
        ("Ruben Dias", "1997-05-14", "Portuguese", "Defender", 3),
        ("Ederson", "1993-08-17", "Brazilian", "Goalkeeper", 31),
        ("Phil Foden", "2000-05-28", "English", "Midfielder", 47)
    ],
    # Liverpool
    [
        ("Mohamed Salah", "1992-06-15", "Egyptian", "Forward", 11),
        ("Sadio Mané", "1992-04-10", "Senegalese", "Forward", 10),
        ("Virgil van Dijk", "1991-07-08", "Dutch", "Defender", 4),
        ("Alisson Becker", "1992-10-02", "Brazilian", "Goalkeeper", 31),
        ("Trent Alexander-Arnold", "1998-10-07", "English", "Defender", 66)
    ],


    # Chelsea
    [
        ("N'Golo Kanté", "1991-03-29", "French", "Midfielder", 7),
        ("Mason Mount", "1999-01-10", "English", "Midfielder", 19),
        ("Thiago Silva", "1984-09-22", "Brazilian", "Defender", 6),
        ("Edouard Mendy", "1992-03-01", "Senegalese", "Goalkeeper", 31),
        ("Reece James", "1999-12-08", "English", "Defender", 24)
    ],

    # Manchester United
    [
        ("Bruno Fernandes", "1994-09-08", "Portuguese", "Midfielder", 18),
        ("Marcus Rashford", "1997-10-31", "English", "Forward", 10),
        ("Harry Maguire", "1993-03-05", "English", "Defender", 5),
        ("David de Gea", "1990-11-07", "Spanish", "Goalkeeper", 31),
        ("Paul Pogba", "1993-03-15", "French", "Midfielder", 6)
    ],


    # La Liga players
    # Real Madrid
    [
        ("Karim Benzema", "1987-12-19", "French", "Forward", 9),
        ("Vinícius Júnior", "2000-07-12", "Brazilian", "Forward", 20),
        ("Sergio Ramos", "1986-03-30", "Spanish", "Defender", 4),
        ("Thibaut Courtois", "1992-05-11", "Belgian", "Goalkeeper", 1),
        ("Luka Modrić", "1985-09-09", "Croatian", "Midfielder", 10)
    ],

    # Barcelona
    [
        ("Lionel Messi", "1987-06-24", "Argentine", "Forward", 10),
        ("Frenkie de Jong", "1997-05-12", "Dutch", "Midfielder", 21),
        ("Gerard Piqué", "1987-02-02", "Spanish", "Defender", 3),
        ("Marc-André ter Stegen", "1992-04-30", "German", "Goalkeeper", 1),
        ("Ansu Fati", "2002-10-31", "Spanish", "Forward", 22)
    ],

    # Atletico Madrid
    [
        ("Luis Suárez", "1987-01-24", "Uruguayan", "Forward", 9),
        ("Antoine Griezmann", "1991-03-21", "French", "Forward", 7),
        ("Stefan Savić", "1991-01-08", "Montenegrin", "Defender", 15),
        ("Jan Oblak", "1993-01-07", "Slovenian", "Goalkeeper", 13),
        ("Koke", "1992-01-08", "Spanish", "Midfielder", 6)
    ],

    # Sevilla
    [
        ("Youssef En-Nesyri", "1997-06-01", "Moroccan", "Forward", 15),
        ("Lucas Ocampos", "1994-07-11", "Argentine", "Forward", 5),
        ("Diego Carlos", "1993-03-15", "Brazilian", "Defender", 20),
        ("Bono", "1991-04-05", "Moroccan", "Goalkeeper", 13),
        ("Joan Jordán", "1994-07-06", "Spanish", "Midfielder", 8)
    ],

    # Bundesliga players
    # Bayern Munich
    [
        ("Robert Lewandowski", "1988-08-21", "Polish", "Forward", 9),
        ("Thomas Müller", "1989-09-13", "German", "Forward", 25),
        ("Joshua Kimmich", "1995-02-08", "German", "Midfielder", 6),
        ("Manuel Neuer", "1986-03-27", "German", "Goalkeeper", 1),
        ("Leon Goretzka", "1995-02-06", "German", "Midfielder", 18)
    ],

    # Borussia Dortmund
    [
        ("Erling Haaland", "2000-07-21", "Norwegian", "Forward", 9),
        ("Marco Reus", "1989-05-31", "German", "Forward", 11),
        ("Jude Bellingham", "2003-06-29", "English", "Midfielder", 22),
        ("Roman Bürki", "1990-11-14", "Swiss", "Goalkeeper", 1),
        ("Mats Hummels", "1988-12-16", "German", "Defender", 15)
    ],

    # RB Leipzig
    [
        ("Emil Forsberg", "1991-10-23", "Swedish", "Midfielder", 10),
        ("Christopher Nkunku", "1997-11-14", "French", "Midfielder", 18),
        ("Ibrahima Konaté", "1999-05-25", "French", "Defender", 6),
        ("Péter Gulácsi", "1990-05-06", "Hungarian", "Goalkeeper", 1),
        ("Yussuf Poulsen", "1994-06-15", "Danish", "Forward", 9)
    ],

    # Bayer Leverkusen
    [
        ("Patrik Schick", "1996-01-24", "Czech", "Forward", 14),
        ("Moussa Diaby", "1999-07-07", "French", "Forward", 19),
        ("Jonathan Tah", "1996-02-11", "German", "Defender", 4),
        ("Lukáš Hrádecký", "1989-11-24", "Finnish", "Goalkeeper", 1),
        ("Florian Wirtz", "2003-05-03", "German", "Midfielder", 27)
    ],

    # Serie A players
    # Juventus
    [
        ("Cristiano Ronaldo", "1985-02-05", "Portuguese", "Forward", 7),
        ("Paulo Dybala", "1993-11-15", "Argentine", "Forward", 10),
        ("Giorgio Chiellini", "1984-08-14", "Italian", "Defender", 3),
        ("Wojciech Szczęsny", "1990-04-18", "Polish", "Goalkeeper", 1),
        ("Federico Chiesa", "1997-10-25", "Italian", "Forward", 22)
    ],

    # Inter Milan
    [
        ("Romelu Lukaku", "1993-05-13", "Belgian", "Forward", 9),
        ("Lautaro Martínez", "1997-08-22", "Argentine", "Forward", 10),
        ("Stefan de Vrij", "1992-02-05", "Dutch", "Defender", 6),
        ("Samir Handanović", "1984-07-14", "Slovenian", "Goalkeeper", 1),
        ("Nicolo Barella", "1997-02-07", "Italian", "Midfielder", 23)
    ],

    # AC Milan
    [
        ("Zlatan Ibrahimović", "1981-10-03", "Swedish", "Forward", 11),
        ("Gianluigi Donnarumma", "1999-02-25", "Italian", "Goalkeeper", 99),
        ("Theo Hernández", "1997-10-06", "French", "Defender", 19),
        ("Ismaël Bennacer", "1997-12-01", "Algerian", "Midfielder", 4),
        ("Franck Kessié", "1996-12-19", "Ivorian", "Midfielder", 79)
    ],

    # Napoli
    [
        ("Lorenzo Insigne", "1991-06-04", "Italian", "Forward", 24),
        ("Kalidou Koulibaly", "1991-06-20", "Senegalese", "Defender", 26),
        ("Piotr Zieliński", "1994-05-20", "Polish", "Midfielder", 20),
        ("Alex Meret", "1997-03-22", "Italian", "Goalkeeper", 1),
        ("Hirving Lozano", "1995-07-30", "Mexican", "Forward", 11)
    ],

    # Ligue 1 players
    # Paris Saint-Germain
    [
        ("Neymar Jr", "1992-02-05", "Brazilian", "Forward", 10),
        ("Kylian Mbappé", "1998-12-20", "French", "Forward", 7),
        ("Marquinhos", "1994-05-14", "Brazilian", "Defender", 5),
        ("Keylor Navas", "1986-12-15", "Costa Rican", "Goalkeeper", 1),
        ("Ángel Di María", "1988-02-14", "Argentine", "Midfielder", 11)
    ],

    # Lille
    [
        ("Jonathan David", "2000-01-14", "Canadian", "Forward", 9),
        ("Burak Yılmaz", "1985-07-15", "Turkish", "Forward", 17),
        ("José Fonte", "1983-12-22", "Portuguese", "Defender", 6),
        ("Mike Maignan", "1995-07-03", "French", "Goalkeeper", 16),
        ("Renato Sanches", "1997-08-18", "Portuguese", "Midfielder", 18)
    ],

    # Marseille
    [
        ("Dimitri Payet", "1987-03-29", "French", "Midfielder", 10),
        ("Arkadiusz Milik", "1994-02-28", "Polish", "Forward", 14),
        ("Álvaro González", "1990-01-08", "Spanish", "Defender", 3),
        ("Steve Mandanda", "1985-03-28", "French", "Goalkeeper", 30),
        ("Boubacar Kamara", "1999-11-23", "French", "Midfielder", 4)
    ],

    # Lyon
    [
        ("Memphis Depay", "1994-02-13", "Dutch", "Forward", 10),
        ("Tino Kadewere", "1996-01-05", "Zimbabwean", "Forward", 11),
        ("Jason Denayer", "1995-06-28", "Belgian", "Defender", 5),
        ("Anthony Lopes", "1990-10-01", "Portuguese", "Goalkeeper", 1),
        ("Lucas Paquetá", "1997-08-27", "Brazilian", "Midfielder", 12)
    ],

    # Primeira Liga players
    # Porto
    [
        ("Moussa Marega", "1991-04-14", "Malian", "Forward", 11),
        ("Sérgio Oliveira", "1992-06-02", "Portuguese", "Midfielder", 27),
        ("Pepe", "1983-02-26", "Portuguese", "Defender", 3),
        ("Agustín Marchesín", "1988-03-16", "Argentine", "Goalkeeper", 1),
        ("Otávio", "1995-02-04", "Brazilian", "Midfielder", 25)
    ],

    # Benfica
    [
        ("Darwin Núñez", "1999-06-24", "Uruguayan", "Forward", 9),
        ("Pizzi", "1989-10-06", "Portuguese", "Midfielder", 21),
        ("Nicolás Otamendi", "1988-02-12", "Argentine", "Defender", 30),
        ("Odisseas Vlachodimos", "1994-04-26", "Greek", "Goalkeeper", 99),
        ("Rafa Silva", "1993-05-17", "Portuguese", "Midfielder", 27)
    ],

    # Sporting Lisbon
    [
        ("Pedro Gonçalves", "1998-06-28", "Portuguese", "Midfielder", 28),
        ("Paulinho", "1992-11-06", "Portuguese", "Forward", 21),
        ("Sebastián Coates", "1990-10-07", "Uruguayan", "Defender", 4),
        ("Antonio Adán", "1987-05-13", "Spanish", "Goalkeeper", 1),
        ("Nuno Mendes", "2002-06-19", "Portuguese", "Defender", 5)
    ],


    # Braga
    [
        ("Ricardo Horta", "1994-09-15", "Portuguese", "Forward", 21),
        ("Fransérgio", "1990-02-01", "Brazilian", "Midfielder", 30),
        ("Nicolás Gaitán", "1988-02-23", "Argentine", "Midfielder", 20),
        ("Matheus", "1994-03-04", "Brazilian", "Goalkeeper", 1),
        ("Raul Silva", "1989-11-19", "Brazilian", "Defender", 4)
    ],


    # Eredivisie players
    # Ajax
    [
        ("Dusan Tadic", "1988-11-20", "Serbian", "Forward", 10),
        ("David Neres", "1997-03-03", "Brazilian", "Forward", 7),
        ("Daley Blind", "1990-03-09", "Dutch", "Defender", 17),
        ("Andre Onana", "1996-04-02", "Cameroonian", "Goalkeeper", 24),
        ("Ryan Gravenberch", "2002-05-16", "Dutch", "Midfielder", 29)
    ],
    # PSV Eindhoven
    [
        ("Eran Zahavi", "1987-07-25", "Israeli", "Forward", 7),
        ("Cody Gakpo", "1999-05-07", "Dutch", "Forward", 11),
        ("Olivier Boscagli", "1997-04-18", "French", "Defender", 18),
        ("Yvon Mvogo", "1994-06-06", "Swiss", "Goalkeeper", 16),
        ("Mario Götze", "1992-06-03", "German", "Midfielder", 19)
    ],

    # Feyenoord
    [
        ("Steven Berghuis", "1991-12-19", "Dutch", "Forward", 10),
        ("Bryan Linssen", "1990-10-08", "Dutch", "Forward", 11),
        ("Eric Botteghin", "1987-08-31", "Brazilian", "Defender", 33),
        ("Justin Bijlow", "1998-01-22", "Dutch", "Goalkeeper", 1),
        ("Orkun Kökçü", "2000-12-29", "Turkish", "Midfielder", 23)
    ],


    # AZ Alkmaar
    [
        ("Teun Koopmeiners", "1998-02-28", "Dutch", "Midfielder", 6),
        ("Myron Boadu", "2001-01-14", "Dutch", "Forward", 9),
        ("Owen Wijndal", "1999-11-28", "Dutch", "Defender", 5),
        ("Marco Bizot", "1991-03-10", "Dutch", "Goalkeeper", 1),
        ("Calvin Stengs", "1998-12-18", "Dutch", "Forward", 23)
    ],

    # Ukrainian Premier League
    # Shakhtar Donetsk
    [
        ("Taison", "1988-01-13", "Brazilian", "Forward", 7),
        ("Marlos", "1988-06-07", "Brazilian", "Midfielder", 11),
        ("Davit Khocholava", "1993-10-10", "Georgian", "Defender", 34),
        ("Anatoliy Trubin", "2001-01-10", "Ukrainian", "Goalkeeper", 81),
        ("Manor Solomon", "1999-07-19", "Israeli", "Forward", 19)
    ],


    # Dynamo Kyiv
    [
        ("Viktor Tsyhankov", "1997-11-15", "Ukrainian", "Midfielder", 15),
        ("Artem Besedin", "1996-03-31", "Ukrainian", "Forward", 9),
        ("Oleksandr Karavayev", "1992-06-01", "Ukrainian", "Defender", 94),
        ("Heorhiy Bushchan", "1994-06-04", "Ukrainian", "Goalkeeper", 1),
        ("Mykola Shaparenko", "1998-10-04", "Ukrainian", "Midfielder", 10)
    ],


    # Zorya Luhansk
    [
        ("Artem Gromov", "1997-04-12", "Ukrainian", "Forward", 9),
        ("Vladyslav Kochergin", "1998-03-28", "Ukrainian", "Midfielder", 17),
        ("Mykyta Kamenyuka", "1994-08-24", "Ukrainian", "Defender", 3),
        ("Mykyta Shevchenko", "1992-01-01", "Ukrainian", "Goalkeeper", 1),
        ("Igor Khomchenovskyi", "1996-07-11", "Ukrainian", "Midfielder", 10)
    ],

    # Dnipro-1
    [
        ("Serhiy Buletsa", "2000-03-02", "Ukrainian", "Midfielder", 8),
        ("Vladyslav Supryaga", "2000-01-15", "Ukrainian", "Forward", 19),
        ("Yevheniy Isayenko", "1996-05-30", "Ukrainian", "Defender", 21),
        ("Vitaliy Mykolenko", "1999-05-29", "Ukrainian", "Defender", 16),
        ("Oleksandr Tkachenko", "1997-04-04", "Ukrainian", "Goalkeeper", 1)
    ]
]
