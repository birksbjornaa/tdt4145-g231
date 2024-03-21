# TDT4145_231

```
Prosjekt 2024
Innlevering, del 2: Realisert databasesystem
Gruppe 231
Birk Strand Bjørnaa, Just Lunde Broch, Oskar Voldsund
```

## Getting started

When you are in the tdt4145_231 folder of this project you can run the commands listed below in the order they are sorted in.

The commands create and insert the requested information into a database file.

Running the commands in another order, will lead to errors.

- create.py creates all the tables in the database
- insert.py inserts all data provided into the databases, apart from the chairs
- scan-seats-hovedscenen.py and scan-seats-gamle-scene.py reads the txt files provided, and inserts the chairs into the databases
- queries.py runs all functions/queries.

The output of the queries are included in the file [output.txt](./output.txt) in the delivery.
In order to check for plays on other dates than March 3rd 2024, or for the co actors of other actors than Sunniva Du Mond Nordal, the strings must be altered in the main method of the queries.py file, on line 117 for date, and line 149 for co actor.

```
1. python3 create.py

2. python3 insert.py

3. python3 scan-seats-hovedscenen.py hovedscenen.txt

4. python3 scan-seats-gamle-scene.py gamle-scene.txt

5. python3 queries.py
```

### Comment

The group's experience with SQL is by using db Browser for SQLite, and when using that, running python3 create.py after opening the database does not show any changes. However, if the database is opened in db Browser after the first command is run in the terminal, the updates are visible after changing viewed table.

## Kommentar til oppgavegjennomføring

Vi har gjort prosjektet slik at vi har oppfylt kravene akkurat slik de står. Dette innebærer at vi i SQL spørringene har forbestemt hvilken input som gis. Altså vi har gitt inn en dato hvor forestillingene som spilles denne dagen hentes ut, vi har gitt et navn hvor det hentes ut alle co-actors.

Hvilken input som gis kan endres i koden. Vi har valgt å ikke bruke tid på å lage et python program hvor brukeren kan spørre fritt og gi input på hva den vil hente ut, da vi valgte å prioritere at spørringene fungerte. Følgelig er ikke programmet spesielt brukervennlig/interaktivt.
