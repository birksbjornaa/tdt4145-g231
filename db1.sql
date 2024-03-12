CREATE TABLE IF NOT EXISTS TeaterSal (
    salNavn VARCHAR(50) NOT NULL,
    antallPlasser INTEGER NOT NULL,
    PRIMARY KEY (salNavn)
);

CREATE TABLE IF NOT EXISTS TeaterStykke (
    navnPaStykke VARCHAR(50) NOT NULL,
    tidspunkt TIME NOT NULL,
    salNavn VARCHAR(50) NOT NULL,
    PRIMARY KEY (navnPaStykke),
    FOREIGN KEY (salNavn) 
        REFERENCES TeaterSal(salNavn) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Akt (
    nummer INTEGER NOT NULL,
    navnPaStykke VARCHAR(50) NOT NULL,
    aktNavn VARCHAR(50),
    PRIMARY KEY (nummer, navnPaStykke),
    FOREIGN KEY (navnPaStykke) 
        REFERENCES TeaterStykke(navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Rolle (
    rolleID INTEGER NOT NULL,
    rolleNavn VARCHAR(50),
    PRIMARY KEY (rolleID)
);

CREATE TABLE IF NOT EXISTS RolleiAkt(
    rolleID INTEGER NOT NULL,
    nummer INTEGER NOT NULL,
    navnPaStykke VARCHAR(50) NOT NULL,
    PRIMARY KEY(rolleID, nummer, navnPaStykke),
    FOREIGN KEY (rolleID) 
        REFERENCES Rolle(rolleID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
    FOREIGN KEY (nummer, navnPaStykke) 
        REFERENCES Akt(nummer, navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Skuespiller ( 
    personID INTEGER NOT NULL,
    navn VARCHAR(50) NOT NULL,
    ePost VARCHAR(50) NOT NULL,
    ansattStatus VARCHAR(50) NOT NULL,
    PRIMARY KEY (personID)
);

CREATE TABLE IF NOT EXISTS SpillerRolle ( 
    personID INTEGER NOT NULL,
    rolleID INTEGER NOT NULL,
    PRIMARY KEY (personID, rolleID),
    FOREIGN KEY (personID) 
        REFERENCES Skuespiller(personID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
    FOREIGN KEY (rolleID) 
        REFERENCES Rolle(rolleID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Forestilling (
    dato DATE NOT NULL, 
    navnPaStykke VARCHAR(50) NOT NULL,
    PRIMARY KEY (dato, navnPaStykke),
    FOREIGN KEY (navnPaStykke) 
        REFERENCES TeaterStykke(navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Stol (
    stolNr INTEGER NOT NULL,
    radNr INTEGER NOT NULL,
    omradeNavn VARCHAR(50) NOT NULL,
    salNavn VARCHAR(50) NOT NULL,
    PRIMARY KEY (stolNr, radNr, omradeNavn, salNavn),
    FOREIGN KEY (salNavn) 
        REFERENCES TeaterSal(salNavn) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Kunde (
   kundeID INTEGER NOT NULL,
   navn VARCHAR(50) NOT NULL,
   mobilNr CHAR(8) NOT NULL,
   adresse CHAR(50) NOT NULL,
   kundeGruppe CHAR(8) NOT NULL,
   PRIMARY KEY (kundeID)
);

CREATE TABLE IF NOT EXISTS PrisListe (
    navnPaStykke VARCHAR(50) NOT NULL,
    billettType VARCHAR(50) NOT NULL,
    pris INTEGER NOT NULL,
    PRIMARY KEY (navnPaStykke, billettType),
    FOREIGN KEY (navnPaStykke) 
        REFERENCES TeaterStykke(navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Ordre (
    ordreID INTEGER NOT NULL,
    kundeID INTEGER NOT NULL,
    navnPaStykke VARCHAR(50) NOT NULL,
    antallBilletter INTEGER NOT NULL,
    kjopsDato DATE NOT NULL,
    kjopsTidspunkt TIME NOT NULL,
    PRIMARY KEY (ordreID),
    FOREIGN KEY (kundeID) 
        REFERENCES Kundeprofil(kundeID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
    FOREIGN KEY (navnPaStykke) 
        REFERENCES PrisListe(navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Billett ( 
    billettID INTEGER NOT NULL,
    stolNr INTEGER NOT NULL,
    radNr INTEGER NOT NULL,
    omradeNavn VARCHAR(30) NOT NULL,
    salNavn VARCHAR(50) NOT NULL,
    dato DATE NOT NULL, 
    navnPaStykke VARCHAR(50) NOT NULL,
    ordreID INTEGER NOT NULL,
    PRIMARY KEY (billettID),
    FOREIGN KEY (dato, navnPaStykke) 
        REFERENCES Forestilling(dato, navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
    FOREIGN KEY (stolNr, radNr, omradeNavn, salNavn) 
        REFERENCES Stol(stolNr, radNr, omradeNavn, salNavn) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
    FOREIGN KEY (ordreID) 
        REFERENCES Ordre(ordreID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Oppgave(
   oppgaveNavn VARCHAR(50) NOT NULL, 
   oppgaveBeskrivelse VARCHAR(200),
   PRIMARY KEY (oppgaveNavn)
);

CREATE TABLE IF NOT EXISTS Ansatt(
   ansattID INTEGER NOT NULL,
   navn VARCHAR(50) NOT NULL,
   ePost VARCHAR(50) NOT NULL,
   ansattStatus VARCHAR(50) NOT NULL,
   PRIMARY KEY (ansattID)
);


CREATE TABLE IF NOT EXISTS GjorOppgaveiStykke(
   oppgaveNavn VARCHAR(50) NOT NULL, 
   navnPaStykke VARCHAR(50) NOT NULL,
   ansattID INTEGER NOT NULL,
   PRIMARY KEY (oppgaveNavn, navnPaStykke, ansattID),
   FOREIGN KEY (oppgaveNavn) 
        REFERENCES Oppgave(oppgaveNavn) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
   FOREIGN KEY (navnPaStykke) 
        REFERENCES TeaterStykke(navnPaStykke) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE,
   FOREIGN KEY (ansattID) 
        REFERENCES Ansatt(ansattID) 
        ON DELETE NO ACTION 
        ON UPDATE CASCADE
);