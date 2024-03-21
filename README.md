# TDT4145_231

## Getting started

When you are in the tdt4145_231 folder of this project you can run the commands listed below in the order they are sorted in.

The commands create and insert the requested information into a database file.

Running the commands in another order, will lead to errors.

- create.py creates all the tables in the database
- insert.py inserts all data provided into the databases, apart from the chairs
- scan-seats-hovedscenen.py and scan-seats-gamle-scene.py reads the txt files provided, and inserts the chairs into the databases
- queries.py runs all functions/queries.

The output of the queries are included in the file TDT4145_DB2_231 in the delivery.
In order to check for plays on other dates than March 3rd 2024, or for the co actors of other actors than Sunniva Du Mond Nordal, the strings must be altered in the main method of the queries.py file, on line 117 for date, and line 149 for co actor.

```
1. python3 create.py

2. python3 insert.py

3. python3 scan-seats-hovedscenen.py hovedscenen.txt

4. python3 scan-seats-gamle-scene.py gamle-scene.txt

5. python3 queries.py
```
