# Host: 127.0.0.1  (Version 5.7.16-log)
# Date: 2017-05-06 15:34:44
# Generator: MySQL-Front 5.4  (Build 4.159)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "log"
#

CREATE TABLE `log` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ts` datetime NOT NULL,
  `names` tinytext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
