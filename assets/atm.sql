-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 12, 2021 at 08:10 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atm`
--

-- --------------------------------------------------------

--
-- Table structure for table `atm_txns`
--

CREATE TABLE `atm_txns` (
  `rr_num` int(11) NOT NULL,
  `cardNumber` varchar(20) DEFAULT NULL,
  `amount` varchar(15) DEFAULT NULL,
  `to_cardNumber` varchar(20) DEFAULT NULL,
  `txn_type` varchar(10) DEFAULT NULL,
  `dot` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `atm_txns`
--

INSERT INTO `atm_txns` (`rr_num`, `cardNumber`, `amount`, `to_cardNumber`, `txn_type`, `dot`) VALUES
(1234, '12345', '300', NULL, 'ATMWDL', '2021-11-09 10:50:42'),
(3256, '12345', '400.0', NULL, 'ATMWDL', '2021-11-09 10:54:54'),
(63311, '12345', '400.0', NULL, 'ATMDEP', '2021-11-09 10:59:20'),
(265985, '12345', '888', '1008', 'ATMTFR', '2021-11-09 11:04:50'),
(951143, '1008', '500', '12345', 'ATMTFR', '2021-11-09 11:21:05'),
(507496, '1008', '400', '1043', 'ATMTFR', '2021-11-09 11:21:22'),
(542536, '1008', '600', '3711', 'ATMTFR', '2021-11-09 11:21:36'),
(95232, '12345', '5000.0', NULL, 'ATMDEP', '2021-11-09 11:23:17'),
(1151, '12345', '222.0', NULL, 'ATMWDL', '2021-11-09 11:23:28'),
(295019, '12345', '500', '1008', 'ATMTFR', '2021-11-09 11:23:51'),
(3573, '12345', '9000.0', NULL, 'ATMWDL', '2021-11-09 12:39:09'),
(72856, '12345', '10000.0', NULL, 'ATMDEP', '2021-11-09 12:41:07'),
(50810, '12345', '400.0', NULL, 'ATMDEP', '2021-11-10 11:27:52'),
(4429, '12345', '5000.0', NULL, 'ATMWDL', '2021-11-10 11:29:39'),
(2708, '12345', '90.0', NULL, 'ATMWDL', '2021-11-10 11:40:12'),
(50036, '12345', '1034.0', NULL, 'ATMDEP', '2021-11-11 05:32:14'),
(8871, '12345', '34.0', NULL, 'ATMWDL', '2021-11-11 08:42:48'),
(8905, '12345', '10.0', NULL, 'ATMWDL', '2021-11-11 08:49:48'),
(98312, '12345', '540000.0', NULL, 'ATMDEP', '2021-11-11 09:05:39'),
(45454, '12345', '53000.0', NULL, 'ATMDEP', '2021-11-11 09:06:28'),
(4577, '12345', '100.0', NULL, 'ATMWDL', '2021-11-11 09:07:46'),
(54192, '12345', '88.0', NULL, 'ATMDEP', '2021-11-11 09:08:41'),
(8582, '12345', '600.0', NULL, 'ATMWDL', '2021-11-11 09:15:41'),
(9559, '12345', '500.0', NULL, 'ATMWDL', '2021-11-11 09:16:08'),
(5521, '12345', '500.0', NULL, 'ATMWDL', '2021-11-11 09:17:20'),
(2141, '12345', '500.0', NULL, 'ATMWDL', '2021-11-11 09:17:37'),
(4337, '12345', '100.0', NULL, 'ATMWDL', '2021-11-11 09:20:50'),
(61061, '12345', '600.0', NULL, 'ATMDEP', '2021-11-12 05:37:11'),
(8912, '12345', '100.0', NULL, 'ATMWDL', '2021-11-12 06:01:46');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `cardNumber` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `surname` text DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `mail` text DEFAULT NULL,
  `money` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cardNumber`, `name`, `surname`, `pin`, `mail`, `money`) VALUES
(1008, 'Uuuu', 'Uuuu', 5555, 'uuuu@gmail.com', '88776'),
(1043, 'Addlkn', 'Sjfs', 4555, 'skdk@gmail.com', '844'),
(1222, 'Kir4', 'Lo4', 2222, 'kir@gmail.com', '3500.0'),
(1241, 'Kiran', 'Kale', 5585, 'kiran@gmail.com', '58858.0'),
(1526, 'Ttt', 'Ttt', 2222, 'ttt@gmail.com', '4000.0'),
(1931, 'Kkk', 'Lll', 222, 'le@gmail.com', '8000.0'),
(2632, 'Kiran', 'Kibndn', 4444, 'ksi@gmail.com', '45555.0'),
(2688, 'Ind', 'Oid', 4444, 'kiran@gmail.com', '7000.0'),
(2728, 'Djsjnf', 'Skdfjsnk', 4444, 'wwe@gmail.com', '66000.0'),
(3641, 'Iii', 'Sjjksj', 1111, 'kkk@gmail.com', '5555.0'),
(3711, 'Ksjdfn', 'Skfb', 333, 'kirn@gmail.com', '88600'),
(4067, 'Kaleti3', 'Kaleti3', 1111, 'kaleti@gmail.com', '4000.0'),
(4755, 'Iii', 'Jiii', 4444, 'kiran@gmail.com', '3838.0'),
(5315, 'Skdkws', 'Sdjsj', 33333, 'asjasj@gmail.com', '3333.0'),
(5371, 'Sdjksk', 'Sdnskn', 2222, 'kir@gmail.com', '333.0'),
(6004, 'Yyy', 'Ykkdkd', 3333, 'lor@gmail.com', '4949.0'),
(6252, 'India', 'Oooo', 1111, 'india@gmail.com', '3000.0'),
(6393, 'Jjj', 'Jksjsj', 1111, 'kiran@gmail.com', '4444.0'),
(7426, 'Snkdsnk', 'Sdnsn', 23323, 'kkiran@gmail.com', '3232.0'),
(7988, 'India', 'Idnia2', 2222, 'kkskssk@gmail.com', '398328.0'),
(8251, 'Sdksk', 'Sdjsjk', 2344, 'jsjkdsk@gmail.com', '3444.0'),
(8562, 'Sdksnkd', 'Sdnsnk', 23333, 'kdi@gmail.com', '343'),
(9213, 'Llll', 'Lals', 4444, 'lall@gmail.com', '99900.0'),
(9463, 'Ldfslk', 'Sflnksl', 2333, 'kiran@gmail.com', '333.0'),
(12345, 'kiran', 'kaleti', 3333, 'kiran@gmail.com', '597478'),
(98765, 'kiran2', 'kaleti2', 1111, 'kiran2@gmail.com', '6200');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`cardNumber`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
