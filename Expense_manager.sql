-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 05, 2019 at 04:19 PM
-- Server version: 5.7.26-0ubuntu0.18.04.1
-- PHP Version: 7.2.19-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Expense_manager`
--

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE `expense` (
  `id` int(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `date` date NOT NULL,
  `description` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`id`, `type`, `amount`, `date`, `description`) VALUES
(2017135040, 'education', 25000, '2019-04-13', 'education'),
(2017135040, 'education', 25000, '2018-10-10', ''),
(2017135040, 'Investment', 69, '2019-04-08', '69'),
(2017135040, 'Investment', 20000, '2019-04-01', 'testing'),
(2017135040, 'education', 1000, '2019-04-09', ' '),
(2017135040, 'education', 1000, '2019-04-16', ' '),
(2017135040, 'education', 3000, '2019-02-14', ' '),
(2017135040, 'Investment', 1000, '2019-04-01', ' '),
(2017135040, 'food', 1000, '2019-04-01', 'qwerty'),
(2017135040, 'food', 1000, '2019-04-01', ' '),
(2017135040, 'food', 1000, '2019-04-01', ' '),
(2017135040, 'food', 1000, '2019-04-01', ' '),
(2017135040, 'food', 1000, '2019-04-16', ' '),
(2017135040, 'food', 1000, '2019-04-16', ' '),
(2017135040, 'food', 69, '2019-04-01', 'showing winston'),
(2017135040, 'food', 21, '2019-04-18', ' '),
(2017135040, 'food', 32, '2019-04-18', ' '),
(2017135040, 'food', 123, '2019-04-18', ' '),
(2017135040, 'education', 0, '2019-04-18', ' '),
(2017135040, 'Investment', 25000, '2019-04-17', 'investment into shares'),
(2017135040, 'Travel', 100, '2019-08-05', 'travel');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `id` int(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `date` date NOT NULL,
  `description` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`id`, `type`, `amount`, `date`, `description`) VALUES
(2017135040, 'Job', 20000, '2019-04-01', 'got salary for 3rd month'),
(2017135040, 'Business', 1000, '2019-01-26', 'from dairy'),
(2017135040, 'Business', 123, '2019-04-08', ' '),
(2017135040, 'Business', 4500, '2019-04-08', ' '),
(2017135040, 'Business', 2500, '2019-04-08', 'hello'),
(2017135040, 'Job', 123, '2019-04-08', 'testing'),
(2017135040, 'Business', 77, '2019-04-01', 'refresh wala'),
(2017135040, 'Job', 69, '2019-04-02', 'addgh'),
(2017135040, 'Business', 69, '2017-04-01', ' '),
(2017135040, 'Business', 1, '2019-04-01', ' '),
(2017135040, 'Job', 1200, '2019-04-02', 'salary of apil'),
(2017135040, 'Business', 1234, '2019-05-01', 'showing to rushi'),
(2017135040, 'Business', 1230, '2019-05-27', ' '),
(2017135040, 'Job', 8, '2019-08-06', 'checking'),
(2017135040, 'Job', 1600, '2019-08-05', ' '),
(2017135040, 'Job', 2000, '2019-08-05', ' '),
(2017135040, 'Job', 5000, '2019-08-05', ' ');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) NOT NULL,
  `name` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `password`) VALUES
(2017134979, 'saurabh yadav', 'qwerty'),
(2017135040, 'viraj', 'asdfg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `expense`
--
ALTER TABLE `expense`
  ADD KEY `id` (`id`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD KEY `id` (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
