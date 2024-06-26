import sqlite3

def create_database():
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS continents (
        code TEXT PRIMARY KEY,
        latitude TEXT,
        longitude TEXT,
        name TEXT,
        nameEs TEXT,
        nameFr TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        code TEXT PRIMARY KEY,
        continent_code TEXT,
        latitude TEXT,
        longitude TEXT,
        name TEXT,
        nameEs TEXT,
        nameFr TEXT,
        nameNative TEXT,
        population INTEGER,
        pib INTEGER DEFAULT 0,
        FOREIGN KEY (continent_code) REFERENCES continents (code)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS encrypt_key (
        key TEXT PRIMARY KEY not null
    )
    ''')


    connection.commit()
    connection.close()

create_database()
