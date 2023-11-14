import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('ecuries.db')
cursor = conn.cursor()

# Création de la table 'lieu'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lieu (
        id_lieu TEXT,
        disponibilite TEXT,
        photo TEXT
    )
''')

# Création de la table 'animal'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animal (
        id_animal TEXT,
        etat TEXT,
        type TEXT,
        race TEXT,
        photo TEXT,
        id_lieu TEXT, 
        FOREIGN KEY (id_lieu) REFERENCES lieu(id_lieu)
    )
''')

# Insertion des données dans les tables 'animal' et 'lieu'
animaux = [
    ('Bucephale', 'fatigue', 'cheval', 'thessalien', '/static/images/Bucephale.jpg', 1),
    ('Pegase', 'endormi', 'cheval', 'pegase', '/static/images/Pegase.jpg', 2),
    ('Jappeloup', 'affame', 'cheval', 'hongre_bai', '/static/images/Jappeloup.jpg', 3),
    ('Rocinante', 'affame', 'cheval', 'rocin', '/static/images/Rocinante.jpg', 3),
    ('Leo', 'cheval', 'affame', 'mustang', '/static/images/Leo.jpg', 3)
]

lieux = [
    ('coin_toilettes', 'libre', '/static/images/coin_toilettes.jpg'),
    ('paturages', 'libre', '/static/images/paturages.jpg'),
    ('champs_d_entrainement', 'occupe', '/static/images/champs_d_entrainement.jpg'),
    ('box_dodo', 'occupe', '/static/images/box_dodo.jpg')
]

# Insertion des données dans la table 'lieu'
for lieu in lieux:
    cursor.execute('INSERT INTO lieu (id_lieu, disponibilite, photo) VALUES (?, ?, ?)', lieu)

# Insertion des données dans la table 'animal'
for animal in animaux:
    cursor.execute('INSERT INTO animal (id_animal, etat, type, race, photo, id_lieu) VALUES (?, ?, ?, ?, ?, ?)', animal)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()
