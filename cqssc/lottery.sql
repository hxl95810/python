/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : lottery

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2017-12-04 14:34:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cqssc
-- ----------------------------
DROP TABLE IF EXISTS `cqssc`;
CREATE TABLE `cqssc` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `date` int(6) DEFAULT NULL,
  `expect` int(5) DEFAULT NULL,
  `opencode` varchar(5) DEFAULT NULL,
  `opentime` varchar(100) DEFAULT NULL,
  `sizebetting` int(5) DEFAULT NULL,
  `paritybetting` int(5) DEFAULT NULL,
  `parityprofit` int(6) DEFAULT NULL,
  `sizeprofit` int(6) DEFAULT NULL,
  `myriabit` int(1) DEFAULT NULL,
  `thousands` int(1) DEFAULT NULL,
  `hundredsdigit` int(1) DEFAULT NULL,
  `tensdigit` int(1) DEFAULT NULL,
  `singledigit` int(1) DEFAULT NULL,
  `size` varchar(100) DEFAULT NULL,
  `parity` varchar(100) DEFAULT NULL,
  `codesum` int(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4441 DEFAULT CHARSET=utf8;
