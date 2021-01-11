-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: frappe
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `loc_id` int NOT NULL AUTO_INCREMENT,
  `l_name` varchar(45) NOT NULL,
  PRIMARY KEY (`loc_id`),
  UNIQUE KEY `Name_UNIQUE` (`l_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (3,'Delhi'),(5,'Nagpur'),(4,'Pune');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prod_mov`
--

DROP TABLE IF EXISTS `prod_mov`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prod_mov` (
  `mov_id` int NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `pid` int NOT NULL,
  `to_loc` int DEFAULT NULL,
  `from_loc` int DEFAULT NULL,
  `quant` int NOT NULL,
  PRIMARY KEY (`mov_id`),
  KEY `pid_idx` (`pid`),
  KEY `loc_id_idx` (`to_loc`,`from_loc`),
  CONSTRAINT `pid` FOREIGN KEY (`pid`) REFERENCES `products` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod_mov`
--

LOCK TABLES `prod_mov` WRITE;
/*!40000 ALTER TABLE `prod_mov` DISABLE KEYS */;
INSERT INTO `prod_mov` VALUES (2,'2021-01-03 12:41:45',7,3,NULL,20),(9,'2021-01-03 13:15:44',7,3,2,7),(10,'2021-01-04 11:39:42',5,4,NULL,4),(11,'2021-01-04 11:49:14',2,4,NULL,2),(12,'2021-01-04 11:53:08',5,4,NULL,3),(13,'2021-01-04 13:23:45',7,NULL,3,2),(22,'2021-01-04 14:50:17',7,5,3,3),(23,'2021-01-04 14:53:30',2,3,NULL,50),(24,'2021-01-04 14:53:44',2,4,3,10),(25,'2021-01-04 14:54:47',2,4,3,5),(28,'2021-01-04 15:06:05',7,3,NULL,3),(30,'2021-01-11 14:44:30',7,3,2,6),(31,'2021-01-11 14:48:20',7,7,NULL,40),(32,'2021-01-11 14:49:05',7,3,7,10);
/*!40000 ALTER TABLE `prod_mov` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `pname` varchar(45) NOT NULL,
  `pcat` varchar(45) NOT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `pid_UNIQUE` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (2,'GPU','Gaming'),(5,'Monitor','Computers'),(7,'Laptop','Computers'),(8,'OnePlus 6T','Mobiles'),(9,'PS5','Gaming'),(12,'Speakers','Electronics');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-11 20:35:21
