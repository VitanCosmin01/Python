import sqlite3

# cream o baza de date si stabilim conexiunea catre aceasta
connection = sqlite3.connect("continents.db")

# pentru a putea executa comenzi sau queri-uri SQL si pentru a interactiona cu datele din baza de date,
# trebuie sa ne folosim de un DB cursor
cursor = connection.cursor()
"""1.	Write a SQL statement to create a table called continents, with the following columns:
a.	continent_id
b.	continent_name
c.	continent_code – 2 letters code, use this link
"""
# crearea tabelului CONTINENTS
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS continents (
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT NOT NULL,
    continent_code TEXT(2) NOT NULL
    );
    """
)

"""2.	Using the link above, write all SQL statements 
needed to add all the seven continents (INSERT)."""
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

"""3.	Write a SQL statement to create a table called countries, with the following columns:
a.	country_code – 2 letters code (e.g. RO, US, IT, etc)
b.	country_name
c.	continent_id – foreign key
d.	population – number
"""
# cursor.execute("""
#     DELETE FROM continents
#     WHERE continent_id > 7""")

# cream tabelul countries
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS countries (
    country_code TEXT(2) NOT NULL,
    country_name TEXT NOT NULL,
    continent_id INTEGER,
    population REAL NOT NULL,
    FOREIGN KEY(continent_id) REFERENCES continents(continent_id)
    );
    """)
"""4.	Write a few SQL statements to add some countries. Here is a list of countries with their codes. Feel free to invent or approximate their populations, and use your geography knowledge for their continent. Add at least 10 countries, as diverse as possible (INSERT). Examples:
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
cursor.execute("""
    INSERT INTO countries (country_code, country_name,continent_id, population)
    VALUES ('RO','Romania', 'EU', '19mil'), 
    ('USA', 'America', 'NA', '330mil'),
    ('FR', 'Franta', 'EU', '70mil'),
    ('HU', 'Hungary', 'EU', '9mil'),
    ('CA', 'Canada', 'EU', '40mil'),
    ('CH', 'China', 'AS', '1450mil');"""
               )
connection.commit()
connection.cursor()
