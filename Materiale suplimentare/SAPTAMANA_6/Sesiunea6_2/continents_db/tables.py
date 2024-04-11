import sqlite3

# cream o baza de date si stabilim conexiunea catre aceasta
connection = sqlite3.connect("continents.db")

# pentru a putea executa comenzi sau queri-uri SQL si pentru a interactiona cu datele din baza de date,
# trebuie sa ne folosim de un DB cursor
cursor = connection.cursor()
"""
1.	Write a SQL statement to create a table called continents, with the following columns:
a.	continent_id
b.	continent_name
c.	continent_code – 2 letters code, use this link
"""
# crearea tabelului CONTINENTS
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS continents (
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code TEXT(2) NOT NULL
#     );
#     """
# )

"""
2.	Using the link above, write all SQL statements 
needed to add all the seven continents (INSERT).
"""

# popularea tabelului cu valori pentru tabelul creat
# cursor.execute("""
# INSERT INTO continents (continent_name, continent_code)
# VALUES
#         ('Africa', 'AF'),
#         ('Antarctica', 'AN'),
#         ('Asia', 'AS'),
#         ('Europe','EU'),
#         ('North America', 'NA'),
#         ('Oceania', 'OC'),
#         ('South America', 'SA');
#         """)

"""
3.	Write a SQL statement to create a table called countries, with the following columns:
a.	country_code – 2 letters code (e.g. RO, US, IT, etc)
b.	country_name
c.	continent_id – foreign key
d.	population – number
"""

# cursor.execute("""
#     DELETE FROM continents
#     WHERE continent_id > 7""")

# cream tabelul COUNTRIES
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS countries (
#     continent_id INTEGER NOT NULL,
#     country_code TEXT(2) NOT NULL,
#     country_name TEXT NOT NULL,
#     population INTEGER NOT NULL,
#     FOREIGN KEY(continent_id) REFERENCES continents(continent_id)
#     );
#     """)

"""
4.	Write a few SQL statements to add some countries. Here is a list of countries with their codes. 
Feel free to invent or approximate their populations, and use your geography knowledge for their continent. 
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

# popularea tabelului countries cu valori
# cursor.execute("""
#     INSERT INTO countries (continent_id, country_code, country_name, population)
#     VALUES (4, 'RO','Romania', '19000000'),
#     (5, 'USA', 'America',  '330000000'),
#     (4, 'FR', 'Franta', '70000000'),
#     (4, 'HU', 'Hungary', '9000000'),
#     (5, 'CA', 'Canada',  '40000000'),
#     (3, 'CH', 'China', '1450000000'),
#     (4, 'BE', 'Belgia', '12000000'),
#     (1, 'EG', 'Egipt','110000000'),
#     (6, 'AU', 'Australia', '25000000');"""
#                )

"""
5.	Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
"""

# cursor.execute(
#     """
#     SELECT * FROM countries
#     ORDER BY country_name;
#     """
# )
# print(cursor.fetchall())
# print("__________________________________")
# cursor.execute(
#     """
#     SELECT COUNT(country_name)
#     FROM countries;
#     """
# )
# print(cursor.fetchall())

"""
6.	Write a SQL statement to select only countries with a population greater than 20 millions. 
"""

# cursor.execute(
#     """
#     SELECT *
#     FROM countries
#     WHERE population > 20000000;
#     """
# )
# print(cursor.fetchall())

"""
7.	Write a SQL statement to select only countries that start with a certain letter 
(choose one that exists for you, e.g. C in the example above).
"""
# cursor.execute(
#     """
#     SELECT country_name, population
#     FROM countries
#     WHERE country_name LIKE 'C%'
#     """
# )
# print(cursor.fetchall())

"""
8.	Write a SQL statement that groups all countries by continents, and counts them.
"""

# cursor.execute(
#     """
#     SELECT continents.continent_name, COUNT(countries.country_name)
#     FROM countries
#     INNER JOIN continents ON countries.continent_id = continents.continent_id
#     GROUP BY continents.continent_name;
#     """
# )
# print(cursor.fetchall())

"""
9.	Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
"""

cursor.execute(
    """
    SELECT continents.continent_name, SUM(countries.population)
    FROM countries
    INNER JOIN continents ON countries.continent_id = continents.continent_id
    GROUP BY continents.continent_name;
    """
)
print(cursor.fetchall())

connection.commit()
connection.cursor()


"""
10.	Extra exercises can be found online:
W3Schools
OneCompiler
"""
