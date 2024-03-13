import sys
import sqlite3

# #Setter opp connection med databasen
# con = sqlite3.connect('sjekk.db')
# con.execute('PRAGMA foreign_keys = ON')
# cursor = con.cursor()

# #Lage eksempelbruker
# cursor.execute(''' INSERT INTO Kunde(kundeID, navn, mobilNr, adresse, kundeGruppe) VALUES (1, 'initBruker', '46765761', 'Gløshaugen', 'Ordinær') ''')

# #Lager hovedscene
# cursor.execute('''INSERT INTO TeaterSal(salNavn, antallPlasser) VALUES ('Hovedscenen', 516) ''')

# #Lager stykke til hovedscene
# cursor.execute('''INSERT INTO TeaterStykke(navnPaStykke, tidspunkt, salNavn) VALUES ('Kongsemnene', 19.00, 'Hovedscenen')''')

# #Lager forestilling til billett
# cursor.execute('''INSERT INTO Forestilling(dato, navnPaStykke) VALUES ('2024-02-03', 'Kongsemnene')''')

# #Lager prisliste for Kongsnemn
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Ordinær', 450)''')
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Honnør', 380)''')
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Kongsemnene', 'Student', 280)''')


# #Lage en ordre som alle kjøpte stoler kobles til
# cursor.execute(''' INSERT INTO Ordre(ordreID, kundeID, navnPaStykke, kundeGruppe, antallBilletter, kjopsDato, kjopsTidspunkt) VALUES (1, 1, 'Kongsemnene', 'Ordinær', 65, '2024-01-03', '19.00') ''')


# # Setter opp stoler, bare brukt til å teste
# r = 1
# for a in range(1, 505):
#     cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Parkett', 'Hovedscenen')''',(a, r))
#     if a % 28 == 0:
#         r += 1


def main():
    if len(sys.argv) != 2:
        print("Correct format: python3 script_name.py input_file.txt")
        return

    #Henter ut filnavnet gitt i commandoen
    input_file = sys.argv[1]

    try:
        # Leser filen
        with open(input_file, 'r') as file:
            data = file.readlines()

        for i, line in enumerate(data):
            line = line.replace("\n", "")

            if "Dato" in line:
                words = line.split()
                for word in words:
                    if len(word) == 10 and word[4] == "-" and word[7] == "-":
                        date = word
                        print(date) 
                        

            if "Galleri" in line:
                if i + 1 < len(data): 
                    next_line = data[i + 1].strip()  
            
            if "Parkett" in line:
                i += 1
                row = 18
                seats_parkett = 504
                billettCount = 1

                while i < len(data):  
                    row_line = data[i].strip()[::-1]
                    for e in range(len(row_line)):
                        if row_line[e] == "1" :
                            seat_nr = seats_parkett - e
                            print("Bought: seat" + str(seat_nr) +"  row: " + str(row))

                            # cursor.execute('''INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, 'Parkett', 'Hovedscenen', '2024-02-03', 'Kongsemnene',  1 )''', (billettCount, seat_nr, row))
                            billettCount += 1
                    i += 1
                    row -= 1
                    seats_parkett -= len(row_line)
                

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()

# # Commit the changes and close the connection
# con.commit()
# con.close()
