-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 06, 2024 at 09:41 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tembaketik`
--

-- --------------------------------------------------------

--
-- Table structure for table `accuracy`
--

CREATE TABLE `accuracy` (
  `ID` int(11) NOT NULL,
  `miss_ID` int(11) DEFAULT NULL,
  `WPM_ID` int(11) DEFAULT NULL,
  `percentage` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accuracy`
--

INSERT INTO `accuracy` (`ID`, `miss_ID`, `WPM_ID`, `percentage`) VALUES
(1, 1, 1, '78.81'),
(2, 2, 2, '93.94');

-- --------------------------------------------------------

--
-- Table structure for table `missed`
--

CREATE TABLE `missed` (
  `ID` int(11) NOT NULL,
  `player_ID` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `words` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `missed`
--

INSERT INTO `missed` (`ID`, `player_ID`, `count`, `words`) VALUES
(1, 1, 175, 'black,black,black,hair,hair,bleed,fast,point,immigrants,immigrants,immigrants,immigrants,immigrants,immigrants,immigrants,immigrants,immigrants,fact,piano,piano,piano,into,jelly,jelly,jelly,jelly,congratulations,congratulations,reconstruction,reconstruction,reconstruction,reconstruction,reconstruction,reconstruction,reconstruction,must,must,must,same,same,smile,smile,test,every,every,every,every,every,bleed,bleed,outsourcing,outsourcing,outsourcing,centuries,centuries,centuries,thriller,thriller,kind,kind,kind,kind,kind,salt,salt,salt,earth,model,model,fault,fault,fault,fault,fault,fault,sheet,auction,wyoming,wyoming,wyoming,wyoming,sweet,sweet,plate,plate,plate,plate,stone,stone,stone,stay,stay,stay,stay,refused,refused,refused,refused,refused,brown,brown,sleep,sleep,brown,brown,run,third,third,third,than,than,than,hope,hope,hope,even,piano,piano,piano,associations,associations,associations,associations,reservation,tuition,smoke,spend,gibraltar,fresh,fresh,first,area,area,area,catch,catch,front,determines,determines,determines,improvement,improvement'),
(2, 1, 2, 'cry,total');

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE `player` (
  `ID` int(11) NOT NULL,
  `Username` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `player`
--

INSERT INTO `player` (`ID`, `Username`, `Password`) VALUES
(1, 'Pythoenix', 'yatagarasu');

-- --------------------------------------------------------

--
-- Table structure for table `score`
--

CREATE TABLE `score` (
  `miss_ID` int(11) NOT NULL,
  `accuracy_ID` int(11) NOT NULL,
  `WPM_ID` int(11) NOT NULL,
  `nilai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `score`
--

INSERT INTO `score` (`miss_ID`, `accuracy_ID`, `WPM_ID`, `nilai`) VALUES
(1, 1, 1, 24866),
(2, 2, 2, 5955);

-- --------------------------------------------------------

--
-- Table structure for table `wpm`
--

CREATE TABLE `wpm` (
  `ID` int(11) NOT NULL,
  `player_ID` int(11) DEFAULT NULL,
  `typed_word_count` int(11) DEFAULT NULL,
  `nilai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wpm`
--

INSERT INTO `wpm` (`ID`, `player_ID`, `typed_word_count`, `nilai`) VALUES
(1, 1, 651, 61),
(2, 1, 31, 73);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accuracy`
--
ALTER TABLE `accuracy`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `miss_ID` (`miss_ID`),
  ADD KEY `WPM_ID` (`WPM_ID`);

--
-- Indexes for table `missed`
--
ALTER TABLE `missed`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `player_ID` (`player_ID`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `score`
--
ALTER TABLE `score`
  ADD PRIMARY KEY (`miss_ID`,`accuracy_ID`,`WPM_ID`),
  ADD KEY `accuracy_ID` (`accuracy_ID`),
  ADD KEY `WPM_ID` (`WPM_ID`);

--
-- Indexes for table `wpm`
--
ALTER TABLE `wpm`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `player_ID` (`player_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accuracy`
--
ALTER TABLE `accuracy`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `missed`
--
ALTER TABLE `missed`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `player`
--
ALTER TABLE `player`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `wpm`
--
ALTER TABLE `wpm`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accuracy`
--
ALTER TABLE `accuracy`
  ADD CONSTRAINT `accuracy_ibfk_1` FOREIGN KEY (`miss_ID`) REFERENCES `missed` (`ID`),
  ADD CONSTRAINT `accuracy_ibfk_2` FOREIGN KEY (`WPM_ID`) REFERENCES `wpm` (`ID`);

--
-- Constraints for table `missed`
--
ALTER TABLE `missed`
  ADD CONSTRAINT `missed_ibfk_1` FOREIGN KEY (`player_ID`) REFERENCES `player` (`ID`);

--
-- Constraints for table `score`
--
ALTER TABLE `score`
  ADD CONSTRAINT `score_ibfk_1` FOREIGN KEY (`miss_ID`) REFERENCES `missed` (`ID`),
  ADD CONSTRAINT `score_ibfk_2` FOREIGN KEY (`accuracy_ID`) REFERENCES `accuracy` (`ID`),
  ADD CONSTRAINT `score_ibfk_3` FOREIGN KEY (`WPM_ID`) REFERENCES `wpm` (`ID`);

--
-- Constraints for table `wpm`
--
ALTER TABLE `wpm`
  ADD CONSTRAINT `wpm_ibfk_1` FOREIGN KEY (`player_ID`) REFERENCES `player` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
