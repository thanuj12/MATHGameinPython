-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2020 at 07:55 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `past_game_details`
--

-- --------------------------------------------------------

--
-- Table structure for table `custom_game`
--

CREATE TABLE `custom_game` (
  `RECORD_NO` int(5) NOT NULL COMMENT '                                  ',
  `Name` varchar(15) NOT NULL,
  `CORRECT_questions` int(5) NOT NULL,
  `TOTAL_questions` int(5) NOT NULL,
  `PERCENTAGE` int(3) NOT NULL,
  `LEVEL` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `custom_game`
--

INSERT INTO `custom_game` (`RECORD_NO`, `Name`, `CORRECT_questions`, `TOTAL_questions`, `PERCENTAGE`, `LEVEL`) VALUES
(1, 'Thanuj', 6, 6, 100, 'MEDIUM'),
(2, 'Thanuj', 2, 3, 66, 'HARD'),
(3, 'Thanuj', 20, 20, 100, 'EASY'),
(4, 'Soul_cruizer', 8, 8, 100, 'EASY'),
(5, 'Thanuj', 5, 5, 100, 'MEDIUM'),
(6, 'Thanuj', 3, 3, 100, 'EASY'),
(7, 'Thanuj', 6, 6, 100, 'EASY'),
(8, 'Thanuj', 3, 3, 100, 'HARD'),
(9, 'Thanuj', 5, 7, 71, 'HARD');

-- --------------------------------------------------------

--
-- Table structure for table `quick_game`
--

CREATE TABLE `quick_game` (
  `RECORD_NO` int(5) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `CORRECT_questions` int(5) NOT NULL,
  `TOTAL_questions` int(5) NOT NULL,
  `PERCENTAGE` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quick_game`
--

INSERT INTO `quick_game` (`RECORD_NO`, `Name`, `CORRECT_questions`, `TOTAL_questions`, `PERCENTAGE`) VALUES
(1, 'Thanuj', 5, 5, 100),
(2, 'Thanuj', 5, 5, 100),
(3, 'Thanuj', 5, 5, 100),
(4, 'Thanuj', 5, 5, 100),
(5, 'Thanuj', 5, 5, 100),
(6, 'Thanuj', 5, 5, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `custom_game`
--
ALTER TABLE `custom_game`
  ADD PRIMARY KEY (`RECORD_NO`);

--
-- Indexes for table `quick_game`
--
ALTER TABLE `quick_game`
  ADD PRIMARY KEY (`RECORD_NO`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `custom_game`
--
ALTER TABLE `custom_game`
  MODIFY `RECORD_NO` int(5) NOT NULL AUTO_INCREMENT COMMENT '                                  ', AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `quick_game`
--
ALTER TABLE `quick_game`
  MODIFY `RECORD_NO` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
