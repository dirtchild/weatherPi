-- MySQL dump 10.16  Distrib 10.1.24-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: u164969887_wthr
-- ------------------------------------------------------
-- Server version	10.1.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sensor_reading`
--

DROP TABLE IF EXISTS `sensor_reading`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_reading` (
  `dateutc` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `winddir` float NOT NULL,
  `windspeedmph` float NOT NULL,
  `windgustmph` float NOT NULL,
  `windgustdir` float NOT NULL,
  `windspdmph_avg2m` float NOT NULL,
  `winddir_avg2m` float NOT NULL,
  `windgustmph_10m` float NOT NULL,
  `windgustdir_10m` float NOT NULL,
  `humidity` float NOT NULL,
  `dewptf` float NOT NULL,
  `tempf` float NOT NULL,
  `rainin` float NOT NULL,
  `dailyrainin` float NOT NULL,
  `baromin` float NOT NULL,
  `weather` text COLLATE utf8_unicode_ci NOT NULL,
  `clouds` text COLLATE utf8_unicode_ci NOT NULL,
  `soiltempf` float NOT NULL,
  `soilmoisture` float NOT NULL,
  `leafwetness` float NOT NULL,
  `solarradiation` float NOT NULL,
  `UV` float NOT NULL,
  `visibility` float NOT NULL,
  `indoortempf` float NOT NULL,
  `indoorhumidity` float NOT NULL,
  KEY `dateutc` (`dateutc`),
  KEY `dateutc_2` (`dateutc`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='see: http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_reading`
--

/*!40000 ALTER TABLE `sensor_reading` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor_reading` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-08  9:28:53
