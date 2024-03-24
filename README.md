# football-league-database-MySQL-script
This repository contains Python scripts developed as an educational resource for KSE University. Specifically tailored to the university's curriculum and educational objectives. These scripts automate the process of setting up the database schema, tables, and initial data for managing football-related information.

## Overview

The scripts automate the process of setting up the database schema, tables, and initial data for managing football-related information. The database can store information about leagues, teams, players, matches, goals, and more.

## Getting Started (English)

To use these scripts, follow these steps:

1. **Clone the Repository**: 
`git clone https://github.com/your-username/football-league-database-MySQL-script.git`


2. **Install Dependencies**:
Ensure you have Python installed on your system!

3. **Prepare Database Structure (Important!!!)**:
Before generating inserts, it's crucial to set up the database structure by executing the scripts in the `create's.sql` and `auto_trigger_STANDINGS.sql` files. These scripts create the necessary tables and define triggers for automatically updating standings. Ensure that the database is properly configured before proceeding with insert generation.

3.1 **Moving .SQL files to your directory**:
After cloning the repository, navigate to the directory containing the downloaded files. Move the `create's.sql` and `auto_trigger_STANDINGS.sql` files to your MySQL directory. This step is necessary to ensure that the scripts are accessible and can be executed smoothly.

To find your MySQL directory path:

a) On Windows, you can press `Alt+Shift+R` when your database is open to reveal the directory path.

b) Alternatively, you can manually locate the MySQL directory by navigating through your file system.

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/caa72946-0e79-45c3-b373-016cfb4a968e)

![nthg](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/14a4bc96-467a-4b78-8171-7ec55d7c611a)

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/de50283c-8eda-4276-a307-7aa49257ccfd)

c) Now you can execute .sql scripts!

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/0a875132-4824-4abb-844f-ba40ca46a620)


4. **Run the Scripts**:
Execute the `main.py` file to run the main program. This will provide a menu with options to generate inserts for different parts of the football database.

5. **Insert Data**:
Choose the appropriate options from the menu to generate SQL inserts for leagues, teams, players, matches, goals, etc. The inserts will be written to separate `.sql` files.

6. **Import Inserts into MySQL**:
After generating the SQL inserts, you can import them into your MySQL database using the method I described above or by simple copy/pasting.

## Початок роботи (Українська)

Щоб використовувати ці скрипти, дотримуйтеся наступних кроків:

1. **Клонування репозиторію**: 
`git clone https://github.com/your-username/football-league-database-MySQL-script.git`


2. **Встановлення необхідних програм**:
Переконайтеся, що у вас встановлено Python на вашій системі!

3. **Підготовка структури бази даних (Важливо!!!)**:
Перед генерацією вставок важливо налаштувати структуру бази даних, виконавши скрипти у файлах `create's.sql` та `auto_trigger_STANDINGS.sql`. Ці скрипти створюють необхідні таблиці та визначають тригери для автоматичного оновлення таблиці рейтингу. Переконайтеся, що база даних налаштована правильно перед продовженням генерації вставок!

3.1 **Переміщення .SQL файлів у вашу папку**:
Після клонування репозиторію перейдіть до директорії із завантаженими файлами. Перемістіть файли `create's.sql` та `auto_trigger_STANDINGS.sql` у вашу папку для MySQL. Цей крок необхідний, щоб забезпечити доступність скриптів та безперешкодне їх виконання.

Як знайти шлях до вашої папки MySQL:

a) На Windows ви можете натиснути `Alt+Shift+R`, коли ваша база даних відкрита, щоб відкрити шлях до папки.

b) Також, ви можете вручну знайти папку MySQL, перейшовши по вашій файловій системі.

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/caa72946-0e79-45c3-b373-016cfb4a968e)

![nthg (1)](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/9ee12448-07e4-4650-85ac-7adb5d4d8697)

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/de50283c-8eda-4276-a307-7aa49257ccfd)

c) Тепер ви можете запустити .sql скрипти!

![image](https://github.com/slash4r/football-league-database-MySQL-script/assets/145005277/0a875132-4824-4abb-844f-ba40ca46a620)


4. **Запуск скриптів**:
Запустите файл `main.py`, головну програму. Це надасть вам меню з варіантами для генерації вставок для різних частин бази даних футболу.

5. **Вставка даних**:
Виберіть відповідні варіанти з меню, щоб згенерувати SQL-вставки для ліг, команд, гравців, матчів, голів тощо. Вставки будуть записані у окремі файли `.sql`.

6. **Імпорт вставок у MySQL**:
Після генерації SQL-вставок ви можете імпортувати їх у вашу базу даних MySQL за допомогою методу, описаного вище, або простим копіюванням/вставленням.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License
empty lol
