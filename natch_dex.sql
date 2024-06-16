-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 13 juin 2024 à 09:34
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `natch_dex`
--

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_1`
--

DROP TABLE IF EXISTS `transformateur_1`;
CREATE TABLE IF NOT EXISTS `transformateur_1` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `transformateur_1`
--

INSERT INTO `transformateur_1` (`Date`, `O2`, `CO2`, `H2`, `CH4`, `C2H6`, `C2H4`, `C2H2`, `Tension_Rupture`, `Eau`) VALUES
('2023-06-12', 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_2`
--

DROP TABLE IF EXISTS `transformateur_2`;
CREATE TABLE IF NOT EXISTS `transformateur_2` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `transformateur_2`
--

INSERT INTO `transformateur_2` (`Date`, `O2`, `CO2`, `H2`, `CH4`, `C2H6`, `C2H4`, `C2H2`, `Tension_Rupture`, `Eau`) VALUES
('2023-06-12', 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_3`
--

DROP TABLE IF EXISTS `transformateur_3`;
CREATE TABLE IF NOT EXISTS `transformateur_3` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `transformateur_3`
--

INSERT INTO `transformateur_3` (`Date`, `O2`, `CO2`, `H2`, `CH4`, `C2H6`, `C2H4`, `C2H2`, `Tension_Rupture`, `Eau`) VALUES
('2023-06-12', 0, 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_4`
--

DROP TABLE IF EXISTS `transformateur_4`;
CREATE TABLE IF NOT EXISTS `transformateur_4` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_5`
--

DROP TABLE IF EXISTS `transformateur_5`;
CREATE TABLE IF NOT EXISTS `transformateur_5` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_6`
--

DROP TABLE IF EXISTS `transformateur_6`;
CREATE TABLE IF NOT EXISTS `transformateur_6` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_7`
--

DROP TABLE IF EXISTS `transformateur_7`;
CREATE TABLE IF NOT EXISTS `transformateur_7` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `transformateur_8`
--

DROP TABLE IF EXISTS `transformateur_8`;
CREATE TABLE IF NOT EXISTS `transformateur_8` (
  `Date` date NOT NULL,
  `O2` float DEFAULT NULL,
  `CO2` float DEFAULT NULL,
  `H2` float DEFAULT NULL,
  `CH4` float DEFAULT NULL,
  `C2H6` float DEFAULT NULL,
  `C2H4` float DEFAULT NULL,
  `C2H2` float DEFAULT NULL,
  `Tension_Rupture` float DEFAULT NULL,
  `Eau` float DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
