import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('sjekk.db')
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

def playsOnDate(date):
    cursor.execute('''
        SELECT navnPaStykke, count (*) as antallBilletterSolgt
        FROM TeaterStykke 
                INNER JOIN Forestilling ON TeaterStykke.navnPaStykke = Forestilling.navnPaStykke
                INNER JOIN Billett ON Forestilling.navnPaStykke = Billett.navnPaStykke
        WHERE dato = ?
        GROUP BY navnPaStykke
        ORDER BY antallBilletterSolgt DESC
    ''', (date,))
    return cursor.fetchall()


def getAllActors():
    cursor.execute('''
        SELECT navnPaStykke as "Teaterstykke", navn, rolleNavn AS "Navn på rolle"
        FROM Skuespiller
            INNER JOIN SpillerRolle ON Skuespiller.personID = SpillerRolle.personID
            INNER JOIN Rolle ON SpillerRolle.rolleID = Rolle.rolleID
            INNER JOIN RolleiAkt ON SpillerRolle.rolleID = RolleiAkt.rolleID
    ''')
    return cursor.fetchall()

def mostPopularPerformance():
    cursor.execute(''' 
        SELECT navnPaStykke, dato, count (billettID) as antallBilletterSolgt
        FROM TeaterStykke
            INNER JOIN Forestilling ON TeaterStykke.navnPaStykke = Forestilling.navnPaStykke
            INNER JOIN Billett ON Forestilling.navnPaStykke = Billett.navnPaStykke
        GROUP BY navnPaStykke, dato
        ORDER BY antallBilletterSolgt DESC
    ''')
    return cursor.fetchall()

def getCoActors(name):
    if name == "": return "No name given"
    cursor.execute(''' 
        SELECT navn AS "Skuespiller", Medspiller.navn AS "Medspiller", navnPaStykke AS "Teaterstykke"
        FROM (SELECT navn as "Skuespiller", nummer, navnPaStykke
                   FROM Skuespiller
                       INNER JOIN SpillerRolle ON Skuespiller.personID = SpillerRolle.personID
                       INNER JOIN RolleiAkt ON SpillerRolle.rolleID = RolleiAkt.rolleID
                   WHERE navn = ?) AS SpillerAkt
                   INNER JOIN (
            SELECT navn AS "Medspiller", nummer, navnPaStykke
            FROM Skuespiller
            INNER JOIN SpillerRolle ON Skuespiller.personID = SpillerRolle.personID
            INNER JOIN RolleiAkt ON SpillerRolle.rolleID = RolleiAkt.rolleID
        ) AS Medspiller ON SpillerAkt.navnPaStykke = Medspiller.navnPaStykke AND SpillerAkt.nummer = Medspiller.nummer
        WHERE Medspiller.Medspiller != ?
    ''', (name, name))
    #alt etter inner join er chat gpt
    return cursor.fetchall()