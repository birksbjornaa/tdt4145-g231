import sqlite3

#endre filnavn til create.py
con = sqlite3.connect('sjekk.db') #endre til feks database.db, la være tom
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TeaterSal (
        salNavn TEXT NOT NULL,
        antallPlasser INTEGER NOT NULL,
        PRIMARY KEY (salNavn)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS TeaterStykke (
        navnPaStykke TEXT NOT NULL,
        tidspunkt TEXT NOT NULL,
        salNavn TEXT NOT NULL,
        PRIMARY KEY (navnPaStykke),
        FOREIGN KEY (salNavn) REFERENCES TeaterSal(salNavn) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Akt (
        nummer INTEGER NOT NULL,
        navnPaStykke TEXT NOT NULL,
        aktNavn TEXT,
        PRIMARY KEY (nummer, navnPaStykke),
        FOREIGN KEY (navnPaStykke) REFERENCES TeaterStykke(navnPaStykke) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rolle (
        rolleID INTEGER NOT NULL,
        rolleNavn TEXT,
        PRIMARY KEY (rolleID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS RolleiAkt(
        rolleID INTEGER NOT NULL,
        nummer INTEGER NOT NULL,
        navnPaStykke TEXT NOT NULL,
        PRIMARY KEY(rolleID, nummer, navnPaStykke),
        FOREIGN KEY (rolleID) REFERENCES Rolle(rolleID) ON DELETE NO ACTION,
        FOREIGN KEY (nummer, navnPaStykke) REFERENCES Akt(nummer, navnPaStykke) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Skuespiller ( 
        personID INTEGER NOT NULL,
        navn TEXT NOT NULL,
        ePost TEXT NOT NULL,
        ansattStatus TEXT NOT NULL,
        PRIMARY KEY (personID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS SpillerRolle ( 
        personID INTEGER NOT NULL,
        rolleID INTEGER NOT NULL,
        PRIMARY KEY (personID, rolleID),
        FOREIGN KEY (personID) REFERENCES Skuespiller(personID) ON DELETE NO ACTION,
        FOREIGN KEY (rolleID) REFERENCES Rolle(rolleID) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Forestilling (
        dato TEXT NOT NULL, 
        navnPaStykke TEXT NOT NULL,
        PRIMARY KEY (dato, navnPaStykke),
        FOREIGN KEY (navnPaStykke) REFERENCES TeaterStykke(navnPaStykke) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stol (
        stolNr INTEGER NOT NULL,
        radNr INTEGER NOT NULL,
        omradeNavn TEXT NOT NULL,
        salNavn TEXT NOT NULL,
        PRIMARY KEY (stolNr, radNr, omradeNavn, salNavn),
        FOREIGN KEY (salNavn) REFERENCES TeaterSal(salNavn) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Kunde (
       kundeID INTEGER NOT NULL,
       navn TEXT NOT NULL,
       mobilNr TEXT NOT NULL,
       adresse TEXT NOT NULL,
       kundeGruppe TEXT NOT NULL,
       PRIMARY KEY (kundeID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PrisListe (
        navnPaStykke TEXT NOT NULL,
        kundeGruppe TEXT NOT NULL,
        pris INTEGER NOT NULL,
        PRIMARY KEY (navnPaStykke, kundeGruppe),
        FOREIGN KEY (navnPaStykke) REFERENCES TeaterStykke(navnPaStykke) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ordre (
        ordreID INTEGER NOT NULL,
        kundeID INTEGER NOT NULL,
        navnPaStykke TEXT NOT NULL,
        kundeGruppe TEXT NOT NULL,
        antallBilletter INTEGER NOT NULL,
        kjopsDato TEXT NOT NULL,
        kjopsTidspunkt TEXT NOT NULL,
        PRIMARY KEY (ordreID),
        FOREIGN KEY (kundeID) REFERENCES Kunde(kundeID) ON DELETE NO ACTION,
        FOREIGN KEY (navnPaStykke, kundeGruppe) REFERENCES PrisListe(navnPaStykke, kundeGruppe) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Billett ( 
        billettID INTEGER NOT NULL,
        stolNr INTEGER NOT NULL,
        radNr INTEGER NOT NULL,
        omradeNavn TEXT NOT NULL,
        salNavn TEXT NOT NULL,
        dato TEXT NOT NULL, 
        navnPaStykke TEXT NOT NULL,
        ordreID INTEGER NOT NULL,
        PRIMARY KEY (billettID),
        FOREIGN KEY (dato, navnPaStykke) REFERENCES Forestilling(dato, navnPaStykke) ON DELETE NO ACTION,
        FOREIGN KEY (stolNr, radNr, omradeNavn, salNavn) REFERENCES Stol(stolNr, radNr, omradeNavn, salNavn) ON DELETE NO ACTION,
        FOREIGN KEY (ordreID) REFERENCES Ordre(ordreID) ON DELETE NO ACTION
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Oppgave(
       oppgaveNavn TEXT NOT NULL, 
       oppgaveBeskrivelse TEXT,
       PRIMARY KEY (oppgaveNavn)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ansatt(
       ansattID INTEGER NOT NULL,
       navn TEXT NOT NULL,
       ePost TEXT NOT NULL,
       ansattStatus TEXT NOT NULL,
       PRIMARY KEY (ansattID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS GjorOppgaveiStykke(
       oppgaveNavn TEXT NOT NULL, 
       navnPaStykke TEXT NOT NULL,
       ansattID INTEGER NOT NULL,
       PRIMARY KEY (oppgaveNavn, navnPaStykke, ansattID),
       FOREIGN KEY (oppgaveNavn) REFERENCES Oppgave(oppgaveNavn) ON DELETE NO ACTION,
       FOREIGN KEY (navnPaStykke) REFERENCES TeaterStykke(navnPaStykke) ON DELETE NO ACTION,
       FOREIGN KEY (ansattID) REFERENCES Ansatt(ansattID) ON DELETE NO ACTION
    )
''')

# Commit the changes and close the connection
con.commit()
con.close()