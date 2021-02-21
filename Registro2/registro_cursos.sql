/*
 Navicat Premium Data Transfer

 Source Server         : Local_Server
 Source Server Type    : MySQL
 Source Server Version : 100116
 Source Host           : 127.0.0.1:3306
 Source Schema         : registro_cursos

 Target Server Type    : MySQL
 Target Server Version : 100116
 File Encoding         : 65001

 Date: 10/11/2020 19:14:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for aspirantes
-- ----------------------------
DROP TABLE IF EXISTS `aspirantes`;
CREATE TABLE `aspirantes`  (
  `RFC` char(13) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `NOMBRE` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `PATERNO` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `MATERNO` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `EMPRESA` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `TELEFONO` bigint(20) NULL DEFAULT NULL,
  `EMAIL` varchar(60) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `FECHA_REGISTRO` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`RFC`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of aspirantes
-- ----------------------------
INSERT INTO `aspirantes` VALUES ('PEPE1234552DF', 'JOSELUIS', 'SAUCEDO', 'GARAY', 'COCA', 8441125555, 'SLASHPAGE15@HOTMAIL.COM', '2020-11-10 17:58:29');
INSERT INTO `aspirantes` VALUES ('PETD7407148Z1', 'DAVID', 'PEREZ', 'TINOCO', 'SE', 8441212121, 'SLASHPAGE15@HOTMAIL.COM', '2020-11-05 16:52:03');

-- ----------------------------
-- Table structure for aspirantes_cursos
-- ----------------------------
DROP TABLE IF EXISTS `aspirantes_cursos`;
CREATE TABLE `aspirantes_cursos`  (
  `ID_CURSO` int(11) NOT NULL,
  `RFC` char(13) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `FECHA_REGISTRO` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_CURSO`, `RFC`) USING BTREE,
  INDEX `FK_ASPIRANTES_CURSOS2`(`RFC`) USING BTREE,
  CONSTRAINT `FK_ASPIRANTES_CURSOS2` FOREIGN KEY (`RFC`) REFERENCES `aspirantes` (`RFC`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_aspirantes_cursos` FOREIGN KEY (`ID_CURSO`) REFERENCES `catalogo_curso` (`ID_CURSO`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of aspirantes_cursos
-- ----------------------------
INSERT INTO `aspirantes_cursos` VALUES (1, 'PEPE1234552DF', '2020-11-10 19:11:40');
INSERT INTO `aspirantes_cursos` VALUES (2, 'PETD7407148Z1', '2020-11-05 16:53:19');
INSERT INTO `aspirantes_cursos` VALUES (3, 'PETD7407148Z1', '2020-11-05 17:25:58');
INSERT INTO `aspirantes_cursos` VALUES (4, 'PEPE1234552DF', '2020-11-10 19:11:59');

-- ----------------------------
-- Table structure for catalogo_curso
-- ----------------------------
DROP TABLE IF EXISTS `catalogo_curso`;
CREATE TABLE `catalogo_curso`  (
  `ID_CURSO` int(11) NOT NULL AUTO_INCREMENT,
  `NOMBRE_CURSO` varchar(35) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `FECHA_ALTA` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_CURSO`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of catalogo_curso
-- ----------------------------
INSERT INTO `catalogo_curso` VALUES (1, 'EL SMOG Y SUS EFECTOS', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso` VALUES (2, 'CIUDADANIA Y COMUNIDADA ECOLOGÍA', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso` VALUES (3, 'PLANTAS MEDICINALES', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso` VALUES (4, 'DESARROLLO URBANO SUSTENTABLE', '2020-03-24 00:00:00');

-- ----------------------------
-- Table structure for catalogo_curso_copy
-- ----------------------------
DROP TABLE IF EXISTS `catalogo_curso_copy`;
CREATE TABLE `catalogo_curso_copy`  (
  `ID_CURSO` int(11) NOT NULL,
  `NOMBRE_CURSO` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `FECHA_ALTA` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_CURSO`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of catalogo_curso_copy
-- ----------------------------
INSERT INTO `catalogo_curso_copy` VALUES (1, 'EL SMOG Y SUS EFECTOS', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso_copy` VALUES (2, 'CIUDADANIA Y COMUNIDADA ECOLOG', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso_copy` VALUES (3, 'PLANTAS MEDICINALES', '2020-03-24 00:00:00');
INSERT INTO `catalogo_curso_copy` VALUES (4, 'DESARROLLO URBANO SUSTENTABLE', '2020-03-24 00:00:00');

SET FOREIGN_KEY_CHECKS = 1;
