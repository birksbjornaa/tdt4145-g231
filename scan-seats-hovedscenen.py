import sys
import sqlite3

#Setter opp connection med databasen
con = sqlite3.connect('trondelagteater.db')
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

# Lage en ordre som alle kjøpte stoler kobles til
cursor.execute(''' INSERT INTO Ordre(ordreID, kundeID, navnPaStykke, kundeGruppe, antallBilletter, kjopsDato, kjopsTidspunkt) VALUES (1, 1, 'Kongsemnene', 'Ordinær', 65, '2024-01-03', '19.00') ''')



# Setter opp stoler, bare brukt til å teste
r = 1
for a in range(1, 505):
    cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Parkett', 'Hovedscenen')''',(a, r))
    if a % 28 == 0:
        r += 1

g = 1
for e in range(505, 525):
    cursor.execute('''INSERT INTO Stol(stolNr, radNr, omradeNavn, salNavn) VALUES (?, ?, 'Galleri', 'Hovedscenen')''',(e, g))
    


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
                            cursor.execute('''INSERT INTO Billett(billettID, stolNr, radNr, omradeNavn, salNavn, dato, navnPaStykke, ordreID) VALUES (?, ?, ?, 'Parkett', 'Hovedscenen', '2024-02-03', 'Kongsemnene',  1 )''', (billettCount, seat_nr, row))
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

# Commit the changes and close the connection
con.commit()
con.close()
