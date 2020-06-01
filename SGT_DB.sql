-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 01/06/2020 às 02:04
-- Versão do servidor: 10.4.11-MariaDB
-- Versão do PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `SGT_DB`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `AtividadeComplementar`
--

CREATE TABLE `AtividadeComplementar` (
  `ID` int(11) NOT NULL,
  `Descricao` varchar(200) NOT NULL,
  `CargaHoraria` int(11) NOT NULL,
  `TutoriaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `AtividadeExtraCurricular`
--

CREATE TABLE `AtividadeExtraCurricular` (
  `ID` int(11) NOT NULL,
  `Descricao` varchar(200) NOT NULL,
  `Tipo` varchar(10) NOT NULL,
  `Bolsista` tinyint(1) NOT NULL,
  `TutoriaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Curso`
--

CREATE TABLE `Curso` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Turno` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Discente`
--

CREATE TABLE `Discente` (
  `Matricula` int(11) NOT NULL,
  `Nome` varchar(200) NOT NULL,
  `NomeSocial` varchar(200) DEFAULT NULL,
  `DataNascimento` date NOT NULL,
  `Gênero` varchar(1) NOT NULL,
  `AnoIngresso` int(11) NOT NULL,
  `TurnoTrabalho` varchar(10) DEFAULT NULL,
  `CidadeOrigem` varchar(100) NOT NULL,
  `MoraEmSerrinha` tinyint(1) NOT NULL,
  `RendaFamiliar` varchar(10) NOT NULL,
  `TempoSemEstudar` int(11) DEFAULT NULL,
  `TipoEscolaEnsMedio` varchar(20) NOT NULL,
  `MotivoEscolhaCurso` varchar(200) NOT NULL,
  `ExpectativasCurso` longtext NOT NULL,
  `SubAreasInteresse` longtext NOT NULL,
  `PlanoEgresso` longtext NOT NULL,
  `NomeCursoTecnico` varchar(200) DEFAULT NULL,
  `LocalCursoTecnico` varchar(200) DEFAULT NULL,
  `NomeGraduacao` varchar(200) DEFAULT NULL,
  `LocalGraduacao` varchar(200) DEFAULT NULL,
  `ProjetoExtensao` longtext DEFAULT NULL,
  `DificuldadesEnsMedio` longtext DEFAULT NULL,
  `DificuldadesCurso` longtext DEFAULT NULL,
  `CoeficienteRendimento` double NOT NULL,
  `SemestreAtual` int(11) NOT NULL,
  `CursoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Disciplina`
--

CREATE TABLE `Disciplina` (
  `ID` int(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `CargaHoraria` int(11) NOT NULL,
  `HorarioSemana` varchar(20) NOT NULL,
  `CursoID` int(11) NOT NULL,
  `Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Docente`
--

CREATE TABLE `Docente` (
  `SIAPE` int(11) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Perfil` varchar(1) NOT NULL,
  `CursoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `EstagioExtraCurricular`
--

CREATE TABLE `EstagioExtraCurricular` (
  `ID` int(11) NOT NULL,
  `Descricao` varchar(100) NOT NULL,
  `Remuneracao` double NOT NULL,
  `CargaHoraria` int(11) NOT NULL,
  `DataInicio` date NOT NULL,
  `DataFim` date DEFAULT NULL,
  `TutoriaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `OrientacaoMatricula`
--

CREATE TABLE `OrientacaoMatricula` (
  `ID` int(11) NOT NULL,
  `DocenteSIAPE` int(11) NOT NULL,
  `DiscenteMatricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `OrientacaoMatricula_Disciplina`
--

CREATE TABLE `OrientacaoMatricula_Disciplina` (
  `OrientacaoID` int(11) NOT NULL,
  `DisciplinaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Tutoria`
--

CREATE TABLE `Tutoria` (
  `ID` int(11) NOT NULL,
  `LegislacoesIFBaiano` longtext NOT NULL,
  `DificuldadesSemestreAtual` longtext NOT NULL,
  `Acoes` longtext NOT NULL,
  `SugestoesDifSemestre` longtext NOT NULL,
  `DificuldadesCurso` longtext NOT NULL,
  `SugestoesDifCurso` longtext NOT NULL,
  `Observacoes` longtext NOT NULL,
  `DocenteSIAPE` int(11) NOT NULL,
  `DiscenteMatricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Tutoria_Disciplina`
--

CREATE TABLE `Tutoria_Disciplina` (
  `TutoriaID` int(11) NOT NULL,
  `DisciplinaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `AtividadeComplementar`
--
ALTER TABLE `AtividadeComplementar`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Tutoria_AC` (`TutoriaID`);

--
-- Índices de tabela `AtividadeExtraCurricular`
--
ALTER TABLE `AtividadeExtraCurricular`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Tutoria_AEC` (`TutoriaID`);

--
-- Índices de tabela `Curso`
--
ALTER TABLE `Curso`
  ADD PRIMARY KEY (`ID`);

--
-- Índices de tabela `Discente`
--
ALTER TABLE `Discente`
  ADD PRIMARY KEY (`Matricula`),
  ADD KEY `FK_Curso_Discente` (`CursoID`);

--
-- Índices de tabela `Disciplina`
--
ALTER TABLE `Disciplina`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Curso_Disciplina` (`CursoID`);

--
-- Índices de tabela `Docente`
--
ALTER TABLE `Docente`
  ADD PRIMARY KEY (`SIAPE`),
  ADD KEY `FK_Curso_Docente` (`CursoID`) USING BTREE;

--
-- Índices de tabela `EstagioExtraCurricular`
--
ALTER TABLE `EstagioExtraCurricular`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Tutoria_EEC` (`TutoriaID`);

--
-- Índices de tabela `OrientacaoMatricula`
--
ALTER TABLE `OrientacaoMatricula`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Docente_OrientacaoMatricula` (`DocenteSIAPE`),
  ADD KEY `FK_Discente_OrientacaoMatricula` (`DiscenteMatricula`);

--
-- Índices de tabela `OrientacaoMatricula_Disciplina`
--
ALTER TABLE `OrientacaoMatricula_Disciplina`
  ADD KEY `FK_Orientacao_TR` (`OrientacaoID`),
  ADD KEY `FK_Disciplina_TR` (`DisciplinaID`);

--
-- Índices de tabela `Tutoria`
--
ALTER TABLE `Tutoria`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_Discente_Tutoria` (`DiscenteMatricula`),
  ADD KEY `FK_Docente_Tutoria` (`DocenteSIAPE`);

--
-- Índices de tabela `Tutoria_Disciplina`
--
ALTER TABLE `Tutoria_Disciplina`
  ADD KEY `FK_Tutoria_TR` (`TutoriaID`),
  ADD KEY `FK_Disciplina_TR_2` (`DisciplinaID`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `AtividadeComplementar`
--
ALTER TABLE `AtividadeComplementar`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `AtividadeExtraCurricular`
--
ALTER TABLE `AtividadeExtraCurricular`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Curso`
--
ALTER TABLE `Curso`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Discente`
--
ALTER TABLE `Discente`
  MODIFY `Matricula` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Disciplina`
--
ALTER TABLE `Disciplina`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Docente`
--
ALTER TABLE `Docente`
  MODIFY `SIAPE` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `EstagioExtraCurricular`
--
ALTER TABLE `EstagioExtraCurricular`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `OrientacaoMatricula`
--
ALTER TABLE `OrientacaoMatricula`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Tutoria`
--
ALTER TABLE `Tutoria`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `AtividadeComplementar`
--
ALTER TABLE `AtividadeComplementar`
  ADD CONSTRAINT `AtividadeComplementar_ibfk_1` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`),
  ADD CONSTRAINT `FK_Tutoria_AC` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`);

--
-- Restrições para tabelas `AtividadeExtraCurricular`
--
ALTER TABLE `AtividadeExtraCurricular`
  ADD CONSTRAINT `AtividadeExtraCurricular_ibfk_1` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`),
  ADD CONSTRAINT `FK_Tutoria_AEC` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`);

--
-- Restrições para tabelas `Discente`
--
ALTER TABLE `Discente`
  ADD CONSTRAINT `Discente_ibfk_1` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`),
  ADD CONSTRAINT `FK_Curso_Discente` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`);

--
-- Restrições para tabelas `Disciplina`
--
ALTER TABLE `Disciplina`
  ADD CONSTRAINT `Disciplina_ibfk_1` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`),
  ADD CONSTRAINT `Disciplina_ibfk_2` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`),
  ADD CONSTRAINT `FK_Curso_Disciplina` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`);

--
-- Restrições para tabelas `Docente`
--
ALTER TABLE `Docente`
  ADD CONSTRAINT `Docente_ibfk_1` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`),
  ADD CONSTRAINT `FK_Curso` FOREIGN KEY (`CursoID`) REFERENCES `Curso` (`ID`);

--
-- Restrições para tabelas `EstagioExtraCurricular`
--
ALTER TABLE `EstagioExtraCurricular`
  ADD CONSTRAINT `EstagioExtraCurricular_ibfk_1` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`),
  ADD CONSTRAINT `FK_Tutoria_EEC` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`);

--
-- Restrições para tabelas `OrientacaoMatricula`
--
ALTER TABLE `OrientacaoMatricula`
  ADD CONSTRAINT `FK_Discente_OrientacaoMatricula` FOREIGN KEY (`DiscenteMatricula`) REFERENCES `Discente` (`Matricula`),
  ADD CONSTRAINT `FK_Docente_OrientacaoMatricula` FOREIGN KEY (`DocenteSIAPE`) REFERENCES `Docente` (`SIAPE`),
  ADD CONSTRAINT `OrientacaoMatricula_ibfk_1` FOREIGN KEY (`DocenteSIAPE`) REFERENCES `Docente` (`SIAPE`),
  ADD CONSTRAINT `OrientacaoMatricula_ibfk_2` FOREIGN KEY (`DocenteSIAPE`) REFERENCES `Docente` (`SIAPE`),
  ADD CONSTRAINT `OrientacaoMatricula_ibfk_3` FOREIGN KEY (`DiscenteMatricula`) REFERENCES `Discente` (`Matricula`);

--
-- Restrições para tabelas `OrientacaoMatricula_Disciplina`
--
ALTER TABLE `OrientacaoMatricula_Disciplina`
  ADD CONSTRAINT `FK_Disciplina_TR` FOREIGN KEY (`DisciplinaID`) REFERENCES `Disciplina` (`ID`),
  ADD CONSTRAINT `FK_Orientacao_TR` FOREIGN KEY (`OrientacaoID`) REFERENCES `OrientacaoMatricula` (`ID`),
  ADD CONSTRAINT `OrientacaoMatricula_Disciplina_ibfk_1` FOREIGN KEY (`OrientacaoID`) REFERENCES `OrientacaoMatricula` (`ID`),
  ADD CONSTRAINT `OrientacaoMatricula_Disciplina_ibfk_2` FOREIGN KEY (`DisciplinaID`) REFERENCES `Disciplina` (`ID`);

--
-- Restrições para tabelas `Tutoria`
--
ALTER TABLE `Tutoria`
  ADD CONSTRAINT `FK_Discente_Tutoria` FOREIGN KEY (`DiscenteMatricula`) REFERENCES `Discente` (`Matricula`),
  ADD CONSTRAINT `FK_Docente_Tutoria` FOREIGN KEY (`DocenteSIAPE`) REFERENCES `Docente` (`SIAPE`),
  ADD CONSTRAINT `Tutoria_ibfk_1` FOREIGN KEY (`DiscenteMatricula`) REFERENCES `Discente` (`Matricula`),
  ADD CONSTRAINT `Tutoria_ibfk_2` FOREIGN KEY (`DocenteSIAPE`) REFERENCES `Docente` (`SIAPE`);

--
-- Restrições para tabelas `Tutoria_Disciplina`
--
ALTER TABLE `Tutoria_Disciplina`
  ADD CONSTRAINT `FK_Disciplina_TR_2` FOREIGN KEY (`DisciplinaID`) REFERENCES `Disciplina` (`ID`),
  ADD CONSTRAINT `FK_Tutoria_TR` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`),
  ADD CONSTRAINT `Tutoria_Disciplina_ibfk_1` FOREIGN KEY (`TutoriaID`) REFERENCES `Tutoria` (`ID`),
  ADD CONSTRAINT `Tutoria_Disciplina_ibfk_2` FOREIGN KEY (`DisciplinaID`) REFERENCES `Disciplina` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
