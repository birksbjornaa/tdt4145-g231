import sqlite3
# Connect to the SQLite database
con = sqlite3.connect('sjekk.db')
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

cursor.execute('''INSERT INTO TeaterSal (salNavn, antallPlasser) VALUES ('Hovedscenen', 516)''')
cursor.execute('''INSERT INTO TeaterSal (salNavn, antallPlasser) VALUES ('Gamle scene', 332)''')
cursor.execute('''INSERT INTO TeaterStykke (navnPaStykke, tidspunkt, salNavn) VALUES ('Kongsemnene', '1900', 'Hovedscenen')''')
cursor.execute('''INSERT INTO TeaterStykke (navnPaStykke, tidspunkt, salNavn) VALUES ('Størst av alt er kjærligheten', '1830', 'Gamle scene')''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (1, 'Kongsemnene', NULL)''')
# Her ha med aktNavn?
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (2, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (3, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (4, 'Kongsemnene', NULL)''')
cursor.execute('''INSERT INTO Akt(nummer, navnPaStykke, aktNavn) VALUES (5, 'Kongsemnene', NULL)''')

cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (1, 'Håkon Håkonson')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (2, 'Dagfinn Bonde')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (3, 'Jatgeir Skald')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (4, 'Sigrid')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (5, 'Ingeborg')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (6, 'Guttorm Ingesson')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (7, 'Skule Jarl')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (8, 'Inga frå Vartejg')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (9, 'Paal Flida')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (10, 'Ragnhild')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (11, 'Gregorius Jonsson')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (12, 'Margrete')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (13, 'Biskop Nikolas')''')
cursor.execute('''INSERT INTO Rolle(rolleID, rolleNavn) VALUES (14, 'Peter')''')

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
cursor.execute('''INSERT INTO RolleiAkt(rolleID, nummer, navnPaStykke) VALUES (5, 4, 'Kongsemnene')''')

cursor.execute('''INSERT INTO Skuespiller(personID, navn, ePost, ansattStatus) VALUES (5, 4, 'Kongsemnene')''')
# Hva mangler heretter:
# Skuespiller, SpillerRolle, Forestilling, Stol, Kunde, PrisListe,
# Ordre, Billett, Oppgave, Ansatt, GjorOppgaveIStykke
# Ser om jeg får til noe med løkker
def create_seats_for_sal(salNavn, omradeNavn, antallRader, seterPrRad):
    for rad in range(1, antallRader + 1):