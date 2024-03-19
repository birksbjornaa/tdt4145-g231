import sqlite3
# Connect to the SQLite database
con = sqlite3.connect('sjekk.db')
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

# Setter inn salene
cursor.execute('''INSERT INTO TeaterSal (salNavn, antallPlasser) VALUES ('Hovedscenen', 516)''')
cursor.execute('''INSERT INTO TeaterSal (salNavn, antallPlasser) VALUES ('Gamle scene', 332)''')

# Setter inn stykker
cursor.execute('''INSERT INTO TeaterStykke (navnPaStykke, tidspunkt, salNavn) VALUES ('Kongsemnene', '1900', 'Hovedscenen')''')
cursor.execute('''INSERT INTO TeaterStykke (navnPaStykke, tidspunkt, salNavn) VALUES ('Størst av alt er kjærligheten', '1830', 'Gamle scene')''')

# Setter inn forestillinger Kongsemne
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-01', 'Kongsemnene')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-02', 'Kongsemnene')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-03', 'Kongsemnene')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-05', 'Kongsemnene')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-06', 'Kongsemnene')''')


# Setter inn forestillinger Størst av alt er kjærligheten
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-03', 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-06', 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-07', 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-12', 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-13', 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO Forestilling (dato, navnPaStykke) VALUES ('2024-02-14', 'Størst av alt er kjærligheten')''')

# Setter inn prisliste for Kongsnemn
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Ordinær', 450)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Honnør', 380)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Student', 280)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Gruppe 10', 420)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Gruppe Honnør', 360)''')

# Setter inn prisliste for Størst av alt er kjærligheten
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Ordinær', 350)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Honnør', 300)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Student', 220)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Barn', 220)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe 10', 320)''')
cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe Honnør', 270)''')







# Setter inn Akter for Kongsemnene
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (1, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (2, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (3, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (4, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (5, 'Kongsemnene', NULL)''')

# Setter inn Roller for Kongsemnene
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (1, 'Håkon Håkonson')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (2, 'Dagfinn Bonde')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (3, 'Jatgeir Skald')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (4, 'Sigrid')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (5, 'Skule Jarl')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (6, 'Inga frå Vartejg')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (7, 'Paal Flida')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (8, 'Ragnhild')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (9, 'Gregorius Jonssønn')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (10, 'Margrete')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (11, 'Biskop Nikolas')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (12, 'Peter')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (13, 'Ingebjørg')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (14, 'Trønder')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (15, 'Baard Bratte')''')

# Setter inn Rolle i Akt for Kongsemnene
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (1, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (1, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (1, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (1, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (1, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (2, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (2, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (2, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (2, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (2, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (3, 4, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (4, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (4, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (4, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (6, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (6, 3, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (7, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (7, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (7, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (8, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (8, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (9, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (9, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (9, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (9, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (9, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (10, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (10, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (10, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (10, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (10, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (11, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (11, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (11, 3, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (12, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (12, 4, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (12, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (13, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (13, 4, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (14, 1, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (14, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (14, 5, 'Kongsemnene')''')

cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (15, 2, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (15, 3, 'Kongsemnene')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (15, 4, 'Kongsemnene')''')

# Setter inn skuespiller for Kongsemnene
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (1, 'Arturo Scotti', 'Arturo@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (2, 'Ingunn Beate Strige Øyen', 'Ingunn@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (3, 'Hans Petter Nilsen', 'Hans@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (4, 'Madeleine Brandtzæg Nilsen', 'Madeleine@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (5, 'Synnøve Fossum Eriksen', 'Synnøve@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (6, 'Emma Caroline Deichmann', 'Emma@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (7, 'Thomas Jensen Takyi', 'Thomas@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (8, 'Per Bogstad Gulliksen', 'Per@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (9, 'Isak Holmen Sørensen', 'Isak@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (10, 'Fabian Heidelberg Lunde', 'Fabian@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (11, 'Emil Olafsson', 'Emile@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (12, 'Snorre Ryen Tøndel', 'Snorre@gmail.com', 'Aktiv')''')

# Setter inn spiller rolle i Kongsemnene
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (1, 1)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (2, 6)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (3, 5)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (4, 8)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (5, 10)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (6, 4)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (6, 13)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (7, 11)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (8, 9)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (9, 7)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (9, 14)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (10, 15)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (10, 14)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (11, 3)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (11, 2)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (12, 12)''')

# Setter inn Ansatt i Kongsemnene
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (1, 'Yury Butusov', 'Yury@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (2, 'Aleksandr Shishkin-Hokusai', 'Aleksandr@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (3, 'Eivind Myren', 'Eivind@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (4, 'Mina Rype Stokke', 'Mina@gmail.com', 'Aktiv')''')

# Setter inn oppgaver til Kongsemnene
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Regi og musikkutvelgelse', 'Blablabla')''')
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Scenografi og Kostymer', 'Blablabla')''')
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Lysdesign', 'Blablabla')''')
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Dramaturg', 'Blablabla')''')

# Setter inn GjørOppgave i stykke til Kongsemnene
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Regi og musikkutvelgelse', 'Kongsemnene', 1)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Scenografi og Kostymer', 'Kongsemnene', 2)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Lysdesign', 'Kongsemnene', 3)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Dramaturg', 'Kongsemnene', 4)''')







# Setter inn Akt for Størst av Alt
cursor.execute('''INSERT INTO Akt (nummer, navnPaStykke, aktNavn) VALUES (1, 'Størst av alt er kjærligheten', NULL)''')

# Setter inn Roller for Størst av Alt
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (16, 'Sunniva Du Mond Nordal')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (17, 'Jo Saberniak')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (18, 'Marte M. Steinholt')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (19, 'Tor Ivar Hagen')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (20, 'Trond-Ove Skrødal')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (21, 'Natalie Grøndahl Tangen')''')
cursor.execute('''INSERT INTO Rolle (rolleID, rolleNavn) VALUES (22, 'Åsmund Flaten')''')

# Setter inn Rolle i Akt for Størst av Alt
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (16, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (17, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (18, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (19, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (20, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (21, 1, 'Størst av alt er kjærligheten')''')
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (22, 1, 'Størst av alt er kjærligheten')''')

# Setter inn skuespiller for Størst av Alt
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (13, 'Sunniva Du Mond Nordal', 'Sunniva@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (14, 'Jo Saberniak', 'Jo@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (15, 'Marte M. Steinholt', 'Marte@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (16, 'Tor Ivar Hagen', 'Tor@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (17, 'Trond-Ove Skrødal', 'Trond@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (18, 'Natalie Grøndahl Tangen', 'Natalie@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (19, 'Åsmund Flaten', 'Åsmund@gmail.com', 'Aktiv')''')

# Setter inn spiller rolle i Størst av Alt
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (13, 16)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (14, 17)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (15, 18)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (16, 19)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (17, 20)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (18, 21)''')
cursor.execute('''INSERT INTO SpillerRolle(personID, rolleID) VALUES (19, 22)''')

# Setter inn Ansatt i Størst av Alt
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (5, 'Jonas Corell Petersen', 'Jona@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (6, 'David Gehrt', 'Davi@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (7, 'Gaute Tønder', 'Gaute@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (8, 'Magnus Mikaelsen', 'Magnus@gmail.com', 'Aktiv')''')
cursor.execute('''INSERT INTO Ansatt (ansattID, navn, ePost, ansattStatus) VALUES (9, 'Kristoffer Spender', 'Kristoffer@gmail.com', 'Aktiv')''')

# Setter inn oppgaver til Størst av Alt
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Regi', 'Blablabla')''')
cursor.execute('''INSERT INTO Oppgave (oppgaveNavn, oppgaveBeskrivelse) VALUES ('Musikalsk ansvarlig', 'Blablabla')''')

# Setter inn GjørOppgave i stykke til Størst av Alt
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Regi', 'Størst av alt er kjærligheten', 5)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Scenografi og Kostymer', 'Størst av alt er kjærligheten', 6)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Musikalsk ansvarlig', 'Størst av alt er kjærligheten', 7)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Lysdesign', 'Størst av alt er kjærligheten', 8)''')
cursor.execute('''INSERT INTO GjorOppgaveiStykke (oppgaveNavn, navnPaStykke, ansattID) VALUES ('Dramaturg', 'Størst av alt er kjærligheten', 9)''')



#Lage eksempelbruker
cursor.execute(''' INSERT INTO Kunde(kundeID, navn, mobilNr, adresse, kundeGruppe) VALUES (1, 'initBruker', '46765761', 'Gløshaugen', 'Ordinær') ''')




# Commit the changes and close the connection
con.commit()
con.close()



# Hva mangler heretter:
# Skuespiller, SpillerRolle, Forestilling, Stol, Kunde, PrisListe,
# Ordre, Billett, Oppgave, Ansatt, GjorOppgaveIStykke
# Ser om jeg får til noe med løkker
