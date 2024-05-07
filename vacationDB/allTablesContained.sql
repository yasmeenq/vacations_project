-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: vacation
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `countryID` int NOT NULL AUTO_INCREMENT,
  `countryName` varchar(45) NOT NULL,
  PRIMARY KEY (`countryID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Japan'),(2,'Italy'),(3,'USA'),(4,'Switzerland'),(5,'Egypt'),(6,'Spain'),(7,'Brazil'),(8,'Germany'),(9,'UK'),(10,'Greece');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `likesID` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `vacationID` int NOT NULL,
  PRIMARY KEY (`likesID`),
  KEY `userID_idx` (`userID`),
  KEY `vacationID_idx` (`vacationID`),
  CONSTRAINT `userID` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `vacationID` FOREIGN KEY (`vacationID`) REFERENCES `vacations` (`vacationID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `roleID` int NOT NULL AUTO_INCREMENT,
  `roleName` varchar(45) NOT NULL,
  PRIMARY KEY (`roleID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `roleID` int NOT NULL,
  PRIMARY KEY (`userID`),
  KEY `roleID_idx` (`roleID`),
  CONSTRAINT `roleID` FOREIGN KEY (`roleID`) REFERENCES `roles` (`roleID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'John','Smith','john@mail.com','1234',1),(2,'Emily','Brown','emily@mail.com','abcd',1),(6,'Taylor','Swift','taylor@mail.com','a1b2c3',2),(15,'Mia','Patel','mia@mail.com','7771',2),(18,'Adam','Lee','lee@mail.com','8888',2),(24,'Sarah','Brown','sarah@mail.com','qwerty123',2),(27,'Blake','Lively','blake@mail.com','qwerty123',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacationID` int NOT NULL AUTO_INCREMENT,
  `countryID` int NOT NULL,
  `description` varchar(255) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `vacationPictureFile` varchar(255) NOT NULL,
  PRIMARY KEY (`vacationID`),
  KEY `countryID_idx` (`countryID`),
  CONSTRAINT `countryID` FOREIGN KEY (`countryID`) REFERENCES `countries` (`countryID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (1,1,'Explore the Land of the Rising Sun','2024-05-01','2024-05-10',1500.00,'japan_vacation.jpg'),(2,2,'Discover the Beauty of Italy','2024-06-15','2024-06-25',1800.00,'italy_vacation.jpg'),(3,3,'Experience the Wonders of the USA','2024-07-10','2024-07-20',2000.00,'usa_vacation.jpg'),(4,4,'Explore the Swiss Alps','2024-08-05','2024-08-15',2200.00,'switzerland_vacation.jpg'),(5,5,'Discover Ancient Egypt','2024-09-01','2024-09-10',1700.00,'egypt_vacation.jpg'),(6,6,'Experience Vibrant Spain','2024-10-15','2024-10-25',1900.00,'spain_vacation.jpg'),(7,7,'Explore the Beauty of Brazil','2024-11-10','2024-11-20',2100.00,'brazil_vacation.jpg'),(8,8,'Discover the Rich History of Germany','2024-12-05','2024-12-15',2300.00,'germany_vacation.jpg'),(9,9,'Experience the Charm of the UK','2025-01-01','2025-01-10',1600.00,'uk_vacation.jpg'),(10,10,'Explore the Beauty of Greece','2025-02-15','2025-02-25',1850.00,'greece_vacation.jpg'),(11,1,'Discover Modern Japan','2025-03-10','2025-03-20',1550.00,'japan_vacation2.jpg'),(12,2,'Experience the Romance of Italy','2025-04-05','2025-04-15',1750.00,'italy_vacation2.jpg'),(44,3,'explore manhattan','2025-01-03','2025-01-05',2750.00,'manhattan.png'),(49,3,'a tour in LA ','2024-12-01','2024-12-09',5000.00,'la.png');
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-07 23:26:30
