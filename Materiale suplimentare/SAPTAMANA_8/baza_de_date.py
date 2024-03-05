"""

1. Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link: https://datahub.io/core/continent-codes
"""

import sqlite3

connection = sqlite3.connect('Geography_practice1.db')
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS continents(
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code CHAR(2) NOT NULL
    );
    '''
)

"""
2. Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
"""

# continents_query = """
# INSERT INTO continents (continent_name, continent_code)
# VALUES (?,?);
# """

# continents_to_add = [
#     ('AF', 'Africa'),
#     ('NA', 'North America'),
#     ('OC', 'Oceania'),
#     ('AN', 'Antarctica'),
#     ('AS', 'Asia'),
#     ('EU', 'Europe'),
#     ('SA', 'South America')
# ]
#
# cursor.executemany(continents_query, continents_to_add)
# connection.commit()

"""
3. Write a SQL statement to create a table called countries, 
with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
"""
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS countries (
    contry_code CHAR(2) NOT NULL,
    contry_name TEXT NOT NULL,
    continent_id INTEGER NOT NULL,
    population INTEGER NOT NULL,
    FOREIGN KEY(continent_id) REFERENCES continents(continent_id)
    );
    '''
)
connection.commit()

"""
4. Write a few SQL statements to add some countries. Here is a list of countries with 
their codes.
Feel free to invent or approximate their populations,
 and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mil
"""

countries_query = """
INSERT INTO countries (contry_code, contry_name, continent_id, population)
VALUES (?, ?, ?, ?)
"""

countries_to_add = [
    ('RO', 'Romania', 6, 19000000),
    ('US', 'USA', 2, 330000000),
    ('FR', 'France', 6, 70000000),
    ('HU', 'Hungary', 6, 9000000),
    ('CA', 'Canada', 2, 40000000),
    ('CN', 'China', 5, 1450000000),
    ('BL', 'Belgium', 6, 12000000),
    ('EG', 'Egypt', 1, 110000000),
    ('AU', 'Australia', 3, 25000000)
]

cursor.executemany(countries_query, countries_to_add)
connection.commit()


"""
5. Write a SQL statement to select all countries, ordered by 
name. Write another statement to count them all.
"""

"""
6. Write a SQL statement to select only countries with a 
population greater than 20 millions.
"""

"""
7. Write a SQL statement to select only countries that start 
with a certain letter (choose one that exists for you, e.g. C
in the example above).
"""

"""
8. Write a SQL statement that groups all countries by
 continents, and counts them.
"""

"""
9. Write a SQL statement that groups all countries by 
continent, and computes the total population per continent 
(SUM).
"""

"""
10.Extra exercises can be found online:
W3Schools: https://www.w3schools.com/mysql/exercise.asp?filename=exercise_select1
OneCompiler: https://onecompiler.com/mysql

"""