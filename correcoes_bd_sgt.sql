ALTER TABLE Tutoria DROP COLUMN DocenteSIAPE;
ALTER TABLE Tutoria ADD COLUMN DocenteID INT NOT NULL;

ALTER TABLE OrientacaoMatricula DROP COLUMN DocenteSIAPE;
ALTER TABLE OrientacaoMatricula ADD COLUMN DocenteID INT NOT NULL;

/* COMANDOS JÁ EXECUTADOS NO TERMINAL */

/*
ALTER TABLE Disciplina DROP COLUMN Status;
ALTER TABLE Disciplina ADD COLUMN Ativa BOOLEAN DEFAULT TRUE;
ALTER TABLE OrientacaoMatricula DROP FOREIGN KEY FK_Docente_OrientacaoMatricula;
ALTER TABLE Tutoria DROP FOREIGN KEY FK_Docente_Tutoria;
ALTER TABLE OrientacaoMatricula DROP FOREIGN KEY OrientacaoMatricula_ibfk_1;
ALTER TABLE Tutoria DROP FOREIGN KEY Tutoria_ibfk_2;
ALTER TABLE OrientacaoMatricula DROP FOREIGN KEY OrientacaoMatricula_ibfk_2;
ALTER TABLE Docente DROP COLUMN SIAPE;
ALTER TABLE Docente ADD COLUMN siape int NOT NULL;
ALTER TABLE Docente ADD PRIMARY KEY (ID);
ALTER TABLE Docente ADD COLUMN ID int NOT NULL auto_increment;

ALTER TABLE Tutoria DROP FOREIGN KEY Tutoria_ibfk_2;
ALTER TABLE Tutoria DROP FOREIGN KEY FK_Docente_Tutoria_1;
ALTER TABLE OrientacaoMatricula DROP FOREIGN KEY OrientacaoMatricula_ibfk_4;
ALTER TABLE OrientacaoMatricula DROP FOREIGN KEY FK_OrientacaoMatricula_Tutoria;

ALTER TABLE Docente MODIFY ID INT AUTO_INCREMENT;

ALTER TABLE Tutoria ADD FOREIGN KEY (ID) REFERENCES Docente(ID);
ALTER TABLE Tutoria ADD CONSTRAINT FK_Docente_Tutoria
FOREIGN KEY (ID) REFERENCES Docente(ID);

ALTER TABLE OrientacaoMatricula ADD FOREIGN KEY (ID) REFERENCES Docente(ID);
ALTER TABLE OrientacaoMatricula ADD CONSTRAINT FK_OrientacaoMatricula_Tutoria 
FOREIGN KEY (ID) REFERENCES Docente(ID);

ALTER TABLE Tutoria ADD COLUMN Status VARCHAR(1);
ALTER TABLE Tutoria ADD COLUMN DisciplinasCursadas VARCHAR(200);

ALTER TABLE OrientacaoMatricula ADD COLUMN Status VARCHAR(1);
ALTER TABLE OrientacaoMatricula ADD COLUMN Disciplinas VARCHAR(200);

source /home/lazaro/Documentos/Projeto_Tutorias_IFBaiano/correcoes_bd_sgt.sql;


*/
