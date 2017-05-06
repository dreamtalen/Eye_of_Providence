
/*!40101 SET NAMES utf8 */;
CREATE TABLE `log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ts` datetime NOT NULL,
  `names` tinytext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
