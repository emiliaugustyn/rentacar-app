-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Gru 2019, 20:14
-- Wersja serwera: 10.4.8-MariaDB
-- Wersja PHP: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `rentacar`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `make` varchar(25) DEFAULT NULL,
  `model` varchar(25) DEFAULT NULL,
  `registration_number` varchar(25) NOT NULL,
  `horse_power` int(11) DEFAULT NULL,
  `passengers` int(11) DEFAULT NULL,
  `price_day` int(11) DEFAULT NULL,
  `in_stock` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `cars`
--

INSERT INTO `cars` (`id`, `make`, `model`, `registration_number`, `horse_power`, `passengers`, `price_day`, `in_stock`) VALUES
(1, 'Oldsmobile', 'Aurora', 'DW55525', 66, 4, 367, NULL),
(2, 'Chevrolet', 'Suburban 2500', 'DW55635', 162, 6, 874, NULL),
(3, 'Acura', 'MDX', 'DW43455', 130, 4, 503, NULL),
(4, 'Infiniti', 'J', 'DW32235', 118, 3, 299, NULL),
(5, 'Corbin', 'Sparrow', 'DW90355', 137, 6, 384, NULL),
(6, 'Chrysler', '300M', 'DW43225', 92, 5, 917, NULL),
(7, 'Isuzu', 'Oasis', 'DW12344', 171, 4, 320, NULL),
(8, 'Oldsmobile', 'Cutlass Cruiser', 'DW07654', 70, 4, 766, NULL),
(9, 'Saab', '9-5', 'DW35654', 159, 5, 524, NULL),
(10, 'Volvo', 'S40', 'DW94304', 158, 4, 788, NULL),
(11, 'BMW', '4', 'DW439HH', 250, 5, 250, NULL),
(14, 'BMW', '5', 'DW439AU', 350, 5, 349, NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `clients`
--

CREATE TABLE `clients` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `firstname` varchar(25) DEFAULT NULL,
  `lastname` varchar(25) DEFAULT NULL,
  `pesel` varchar(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(9) DEFAULT NULL,
  `id_number` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `clients`
--

INSERT INTO `clients` (`id`, `username`, `password`, `firstname`, `lastname`, `pesel`, `email`, `phone_number`, `id_number`) VALUES
(1, 'wkrojn0', 'vwDWW4dN', 'Waiter', 'Krojn', '78905513158', 'wkrojn0@prnewswire.com', '435787213', '245547520'),
(2, 'jgarahan1', 'HQY9EJKr8', 'Jaquith', 'Garahan', '84683898190', 'jgarahan1@dion.ne.jp', '296903017', '725543286'),
(3, 'gtrewett2', 'St2qeS', 'Gabie', 'Trewett', '78156553404', 'gtrewett2@fastcompany.com', '687314134', '363569542'),
(4, 'balbury3', 'Dw7O5BueuM', 'Beitris', 'Albury', '93576513010', 'balbury3@digg.com', '793897722', '357691498'),
(5, 'lzanolli4', 'MtHAALN', 'Letty', 'Zanolli', '67113293468', 'lzanolli4@amazon.com', '957279378', '813288480'),
(6, 'wcunnington5', 'ppPKrBiyt2', 'Whitby', 'Cunnington', '51513459731', 'wcunnington5@loc.gov', '740404979', '398445545'),
(7, 'cdunniom6', 'rptZ3q74UDr7', 'Carling', 'Dunniom', '87776077752', 'cdunniom6@privacy.gov.au', '790139323', '869792379'),
(8, 'hmacginlay7', 'CIl8cVjvaWi', 'Honor', 'MacGinlay', '99156349443', 'hmacginlay7@toplist.cz', '561994279', '19538791'),
(9, 'cmarques8', 'r8FUdjxM', 'Case', 'Marques', '59754639618', 'cmarques8@mapy.cz', '668170583', '871772335'),
(10, 'alavallie9', 'ARYBhS2', 'Antonie', 'Lavallie', '74967784951', 'alavallie9@booking.com', '911425216', '370199144');

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `efektywnosc`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `efektywnosc` (
`firstname` varchar(25)
,`lastname` varchar(25)
,`id` int(11)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `najlepsi_klienci`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `najlepsi_klienci` (
`COUNT(reservations.client_id)` bigint(21)
);

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `popularnosc`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `popularnosc` (
`make` varchar(25)
,`model` varchar(25)
,`id` int(11)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `reservations`
--

CREATE TABLE `reservations` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `car_id` int(11) NOT NULL,
  `worker_id` int(11) NOT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Zastąpiona struktura widoku `rezerwacje_klienta`
-- (Zobacz poniżej rzeczywisty widok)
--
CREATE TABLE `rezerwacje_klienta` (
`make` varchar(25)
,`model` varchar(25)
);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `workers`
--

CREATE TABLE `workers` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `firstname` varchar(25) DEFAULT NULL,
  `lastname` varchar(25) DEFAULT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `workers`
--

INSERT INTO `workers` (`id`, `username`, `password`, `firstname`, `lastname`, `email`) VALUES
(1, 'kgobert0', '5TF33yI27UC', 'Kermy', 'Gobert', 'kgobert0@msu.edu'),
(2, 'rbrogden1', 'YigsGx2', 'Rena', 'Brogden', 'rbrogden1@vistaprint.com'),
(3, 'hfrayling2', 'jbGditvq', 'Hilary', 'Frayling', 'hfrayling2@cbsnews.com');

-- --------------------------------------------------------

--
-- Struktura widoku `efektywnosc`
--
DROP TABLE IF EXISTS `efektywnosc`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `efektywnosc`  AS  (select `w`.`firstname` AS `firstname`,`w`.`lastname` AS `lastname`,`r`.`id` AS `id` from (`workers` `w` left join `reservations` `r` on(`w`.`id` = `r`.`car_id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `najlepsi_klienci`
--
DROP TABLE IF EXISTS `najlepsi_klienci`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `najlepsi_klienci`  AS  (select count(`reservations`.`client_id`) AS `COUNT(reservations.client_id)` from `reservations` group by `reservations`.`client_id`) ;

-- --------------------------------------------------------

--
-- Struktura widoku `popularnosc`
--
DROP TABLE IF EXISTS `popularnosc`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `popularnosc`  AS  (select `c`.`make` AS `make`,`c`.`model` AS `model`,`r`.`id` AS `id` from (`cars` `c` left join `reservations` `r` on(`c`.`id` = `r`.`car_id`))) ;

-- --------------------------------------------------------

--
-- Struktura widoku `rezerwacje_klienta`
--
DROP TABLE IF EXISTS `rezerwacje_klienta`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `rezerwacje_klienta`  AS  (select `cars`.`make` AS `make`,`cars`.`model` AS `model` from ((`clients` join `reservations` on(`clients`.`id` = `reservations`.`client_id`)) join `cars` on(`reservations`.`car_id` = `cars`.`id`))) ;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `registration_number` (`registration_number`);

--
-- Indeksy dla tabeli `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `password` (`password`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indeksy dla tabeli `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `car_id` (`car_id`),
  ADD KEY `worker_id` (`worker_id`);

--
-- Indeksy dla tabeli `workers`
--
ALTER TABLE `workers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `password` (`password`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT dla tabeli `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `workers`
--
ALTER TABLE `workers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `reservations`
--
ALTER TABLE `reservations`
  ADD CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
  ADD CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`),
  ADD CONSTRAINT `reservations_ibfk_3` FOREIGN KEY (`worker_id`) REFERENCES `workers` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
