import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('sjekk.db')
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

def playsOnDate(date):
    cursor.execute('''
        SELECT TeaterStykke.navnPaStykke, COUNT(Billett.billettID) AS antallBilletterSolgt
        FROM TeaterStykke
            LEFT JOIN Forestilling ON TeaterStykke.navnPaStykke = Forestilling.navnPaStykke
            LEFT JOIN Billett ON Forestilling.dato = Billett.dato AND Forestilling.navnPaStykke = Billett.navnPaStykke
        WHERE Forestilling.dato = ? 
        GROUP BY TeaterStykke.navnPaStykke
    ''', (date,))
    return cursor.fetchall()


def getAllActors():
    cursor.execute('''
        SELECT DISTINCT navnPaStykke as "Teaterstykke", navn, rolleNavn AS "Navn på rolle"
        FROM Skuespiller
            INNER JOIN SpillerRolle ON Skuespiller.personID = SpillerRolle.personID
            INNER JOIN Rolle ON SpillerRolle.rolleID = Rolle.rolleID
            INNER JOIN RolleiAkt ON SpillerRolle.rolleID = RolleiAkt.rolleID
    ''')
    return cursor.fetchall()

def mostPopularPerformance():
    cursor.execute(''' 
        SELECT Billett.navnPaStykke, Billett.dato, count(billettID) AS antallBilletterSolgt
        FROM Billett
        GROUP BY Billett.dato, Billett.navnPaStykke
        ORDER BY antallBilletterSolgt DESC
    ''')
    return cursor.fetchall()

def getCoActors(name):
    if name == "": return "No name given"
    cursor.execute(''' 
       SELECT DISTINCT Skuespiller.navn, navnPaStykke FROM  
        SpillerRolle INNER JOIN (SELECT rolleID, RolleiAkt.navnPaStykke
            FROM RolleiAkt 
                INNER JOIN (SELECT Skuespiller.navn as "Skuespiller", RolleiAkt.nummer, navnPaStykke
                            FROM Skuespiller
                                INNER JOIN SpillerRolle ON Skuespiller.personID = SpillerRolle.personID
                                INNER JOIN RolleiAkt ON SpillerRolle.rolleID = RolleiAkt.rolleID
                            WHERE navn = ?) AS SpillerAkt
                    ON RolleiAkt.nummer = SpillerAkt.nummer AND rolleiAkt.navnPaStykke = SpillerAkt.navnPaStykke) AS IdeEr
                    ON SpillerRolle.rolleID = IdeEr.rolleID
                    INNER JOIN Skuespiller ON SpillerRolle.personID = Skuespiller.PersonID
            WHERE Skuespiller.navn != ?
    ''', (name, name))
    return cursor.fetchall()


def buySeats():
    cursor.execute(''' 
        SELECT stolNr, radNr, omradeNavn
        FROM Stol
        WHERE (stolNr, radNr, omradeNavn) NOT IN (
            SELECT stolNr, radNr, omradeNavn
            FROM Billett
            WHERE Dato = '03-02-2024')
            AND salNavn = 'Gamle scene' 
        GROUP BY radNr, omradeNavn                      
    ''')

    ledigeseter = cursor.fetchall()
    
    query = True
    i = 0
    while query:
        line = ledigeseter[i]
        if int(line[0]) > 9:
            radnr = line[1]
            omrade = line[2]
            cursor.execute('''
                SELECT stolNr, radNr, omradeNavn 
                FROM (SELECT stolNr, radNr, omradeNavn
                    FROM Stol
                    WHERE (stolNr, radNr, omradeNavn) NOT IN (
                        SELECT stolNr, radNr, omradeNavn
                        FROM Billett
                        WHERE Dato = '03-02-2024')
                        AND salNavn = 'Gamle scene') 
                WHERE radNr = ? AND omradeNavn = ?
                    ''', (radnr,omrade,))
            rad = cursor.fetchall()
            query = False
        i += 1

    cursor.execute(''' INSERT INTO Ordre(ordreID, kundeID, navnPaStykke, kundeGruppe, antallBilletter, kjopsDato, kjopsTidspunkt) VALUES (3, 1, 'Størst av alt er kjærligheten', 'Ordinær', 9, '2024-01-03', '1200') ''')

    billettID = 93
    for i in range(0, 9):
        kjopStol = rad[i]
        cursor.execute('''
            INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, ?, 'Gamle scene', '2024-02-03', 'Størst av alt er kjærligheten', 3)
        ''', (billettID, kjopStol[0], kjopStol[1], kjopStol[2]))
        print("   Bought stolNr: " + str(kjopStol[0]) + " on row: " + str(kjopStol[1]) + "   in hall: " + kjopStol[2])
        
        billettID += 1
            

    return rad



def main():
    
    print("\nPlays on given Date:\n")
    pList = playsOnDate('2024-02-03')

    for p in range(len(pList)):
        line = pList[p]
        styke = line[0]
        solgt = line[1]
        print("   Stykke: " + str(styke) + "\n   Antall solgte billetter: " + str(solgt) + "\n")


    print("\nAll Actors:\n")
    List = getAllActors()
    
    for e in range(len(List)):
        stykke = List[e][0]
        skuespiller = List[e][1]
        rolle = List[e][2]
        print("   Stykke: " + stykke + "\n   Skuespiller: " + skuespiller + "\n   Rolle: " + rolle + "\n")

    # Call mostPopularPerformance function
    print("\nMost Popular Performance:\n")
    mostList = mostPopularPerformance()

    for c in range(len(mostList)):
        linje = mostList[c]
        stykkke = linje[0]
        date = linje[1]
        solgt = linje[2]
        print("   Stykke: " + str(stykkke) + "  Dato: " + str(date) + "    Antall solgt: " + str(solgt))



    # Call getCoActors function
    actor = "Sunniva Du Mond Nordal"
    coList = getCoActors(actor)
    stykke = coList[0][1]
    print("\nCo-Actors of " + actor + " in the play " + stykke + "\n")

    for d in range(len(coList)):
        linje = coList[d]
        print("    - " + str(linje[0]))
    
    print("\nBuy 9 seats available on same row:\n")
    buySeats()



if __name__ == "__main__":
    main()

con.commit()
con.close()