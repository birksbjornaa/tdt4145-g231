import sys
import sqlite3

# #Setter opp connection med databasen
# con = sqlite3.connect('sjekk.db')
# con.execute('PRAGMA foreign_keys = ON')
# cursor = con.cursor()



# #Lager Gamle Scene
# cursor.execute('''INSERT INTO TeaterSal(salNavn, antallPlasser) VALUES ('Gamle scene', 332) ''')

# #Lager stykke til hovedscene
# cursor.execute('''INSERT INTO TeaterStykke(navnPaStykke, tidspunkt, salNavn) VALUES ('Størst av alt er kjærligheten', 18.30, 'Gamle scene')''')

# #Lager forestilling til billett
# cursor.execute('''INSERT INTO Forestilling(dato, navnPaStykke) VALUES ('2024-02-03', 'Størst av alt er kjærligheten')''')

# #Lager prisliste for Kongsnemn
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Ordinær', 350)''')
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Honnør', 380)''')
# cursor.execute('''INSERT INTO PrisListe(navnPaStykke, kundeGruppe, pris) VALUES ('Størst av alt er kjærligheten', 'Student', 280)''')


# #Lage en ordre som alle kjøpte stoler kobles til
# cursor.execute(''' INSERT INTO Ordre(ordreID, kundeID, navnPaStykke, kundeGruppe, antallBilletter, kjopsDato, kjopsTidspunkt) VALUES (2, 1, 'Kongsemnene', 'Ordinær', 27, '2024-01-03', '18.30') ''')


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
            billettCount = 66

        for i, line in enumerate(data):
            line = line.replace("\n", "")

            if "Dato" in line:
                words = line.split()
                for word in words:
                    if len(word) == 10 and word[4] == "-" and word[7] == "-":
                        date = word
                        print(date) 
                        
            rg = 3
            if "Galleri" in line:
                i += 1
                for e in range(3):
                    next_line = data[i].strip()
                    # print(next_line)
                    for sg in range(len(next_line)):
                        a_sg = sg + 1
                        # cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Galleri', 'Gamle scene')''',(a_sg, rg))
                        if next_line[sg] == '1':
                            print("Bought: seat" + str(a_sg) +"  row: " + str(rg))
                            # cursor.execute('''INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, 'Galler', 'Gamle scene', '2024-02-03', 'Størst av alt er kjærligheten',  1 )''', (billettCount, sg, rg)) 
                            billettCount += 1
                    i += 1
                    rg -= 1
                    

            rb = 4
            if "Balkong" in line:
                i += 1
                for c in range(4):
                    next_line = data[i].strip()
                    # print(next_line)
                    for sb in range(len(next_line)):
                        a_sb = sb + 1
                        # cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Galleri', 'Gamle scene')''',(a_sb, rb))
                        if next_line[sb] == '1':
                            print("Bought: seat" + str(a_sb) +"  row: " + str(rb))
                            # cursor.execute('''INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, 'Galler', 'Gamle scene', '2024-02-03', 'Størst av alt er kjærligheten',  1 )''', (billettCount, sb, rb)) 
                            billettCount += 1
                    i += 1
                    rb -= 1
            
            rp = 10
            if "Parkett" in line:
                i += 1
                for d in range(10):
                    next_line = data[i].strip()
                    # print(next_line)
                    for sp in range(len(next_line)):
                        a_sp = sp + 1
                        # cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Galleri', 'Gamle scene')''',(a_sp, rp))
                        if next_line[sp] == '1':
                            print("Bought: seat" + str(a_sp) +"  row: " + str(rp))
                            # cursor.execute('''INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, 'Galler', 'Gamle scene', '2024-02-03', 'Størst av alt er kjærligheten',  1 )''', (billettCount, sp, rp)) 
                            billettCount += 1
                    i += 1
                    rp -= 1
                

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()

# Commit the changes and close the connection
# con.commit()
# con.close()