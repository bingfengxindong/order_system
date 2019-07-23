/*
Navicat MySQL Data Transfer

Source Server         : win7mysql
Source Server Version : 50640
Source Host           : localhost:3306
Source Database       : order_system_b

Target Server Type    : MYSQL
Target Server Version : 50640
File Encoding         : 65001

Date: 2019-07-22 13:04:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for accounting_documents_accountingdocuments
-- ----------------------------
DROP TABLE IF EXISTS `accounting_documents_accountingdocuments`;
CREATE TABLE `accounting_documents_accountingdocuments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ad_id` char(32) NOT NULL,
  `ad_ps_dollar_total_price` varchar(200) DEFAULT NULL,
  `ad_actual_cost` varchar(200) DEFAULT NULL,
  `ad_total_profit` varchar(200) DEFAULT NULL,
  `ad_total_amount_materials` varchar(200) DEFAULT NULL,
  `ad_total_amount_fabric` varchar(200) DEFAULT NULL,
  `ad_total_amount_fabric_express` varchar(200) DEFAULT NULL,
  `ad_total_amount_bonding` varchar(200) DEFAULT NULL,
  `ad_total_amount_ingredients` varchar(200) DEFAULT NULL,
  `ad_total_amount_ingredients_express` varchar(200) DEFAULT NULL,
  `ad_total_amount_other` varchar(200) DEFAULT NULL,
  `ad_total_amount_labor_payment` varchar(200) DEFAULT NULL,
  `ad_total_amount_tailor` varchar(200) DEFAULT NULL,
  `ad_tailor_start_date` datetime(6) DEFAULT NULL,
  `ad_tailor_end_date` datetime(6) DEFAULT NULL,
  `ad_tailor_number_people` varchar(200) DEFAULT NULL,
  `ad_total_amount_sewing` varchar(200) DEFAULT NULL,
  `ad_sewing_start_date` datetime(6) DEFAULT NULL,
  `ad_sewing_end_date` datetime(6) DEFAULT NULL,
  `ad_sewing_number_people` varchar(200) DEFAULT NULL,
  `ad_total_amount_iron` varchar(200) DEFAULT NULL,
  `ad_iron_start_date` datetime(6) DEFAULT NULL,
  `ad_iron_end_date` datetime(6) DEFAULT NULL,
  `ad_iron_number_people` varchar(200) DEFAULT NULL,
  `ad_total_amount_embroide_print` varchar(200) DEFAULT NULL,
  `ad_total_amount_water_washing` varchar(200) DEFAULT NULL,
  `ad_total_amount_embroide` varchar(200) DEFAULT NULL,
  `ad_total_amount_print` varchar(200) DEFAULT NULL,
  `ad_total_amount_packaging_shipping` varchar(200) DEFAULT NULL,
  `ad_total_amount_paperboard` varchar(200) DEFAULT NULL,
  `ad_total_amount_physical_distribution` varchar(200) DEFAULT NULL,
  `ad_total_amount_warehouse_entry` varchar(200) DEFAULT NULL,
  `ad_total_amount_customs_declaration` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of accounting_documents_accountingdocuments
-- ----------------------------
INSERT INTO `accounting_documents_accountingdocuments` VALUES ('18', '31f36b9ea12f11e996c0005056c00008', '3376.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '2019-07-08 11:19:28.510201', '2019-07-10 14:11:51.301700', '0');
INSERT INTO `accounting_documents_accountingdocuments` VALUES ('19', 'fa09e30ca2eb11e998c7005056c00008', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '2019-07-10 16:23:20.749700', '2019-07-10 16:23:20.749700', '0');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 用户表', '7', 'add_user');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 用户表', '7', 'change_user');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 用户表', '7', 'delete_user');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 绣印花表', '8', 'add_embroiderorprint');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 绣印花表', '8', 'change_embroiderorprint');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 绣印花表', '8', 'delete_embroiderorprint');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 帽型表', '9', 'add_captype');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 帽型表', '9', 'change_captype');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 帽型表', '9', 'delete_captype');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 帽子颜色表', '10', 'add_capcolor');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 帽子颜色表', '10', 'change_capcolor');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 帽子颜色表', '10', 'delete_capcolor');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 订单表', '11', 'add_order');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 订单表', '11', 'change_order');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 订单表', '11', 'delete_order');
INSERT INTO `auth_permission` VALUES ('34', 'Can add 客户表', '12', 'add_customer');
INSERT INTO `auth_permission` VALUES ('35', 'Can change 客户表', '12', 'change_customer');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete 客户表', '12', 'delete_customer');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 帽眉表', '13', 'add_capeyebrow');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 帽眉表', '13', 'change_capeyebrow');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 帽眉表', '13', 'delete_capeyebrow');
INSERT INTO `auth_permission` VALUES ('40', 'Can add 后扣表', '14', 'add_afterdeduction');
INSERT INTO `auth_permission` VALUES ('41', 'Can change 后扣表', '14', 'change_afterdeduction');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete 后扣表', '14', 'delete_afterdeduction');
INSERT INTO `auth_permission` VALUES ('43', 'Can add 版号表', '15', 'add_versionnumber');
INSERT INTO `auth_permission` VALUES ('44', 'Can change 版号表', '15', 'change_versionnumber');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete 版号表', '15', 'delete_versionnumber');
INSERT INTO `auth_permission` VALUES ('46', 'Can add 打样修改意见表', '16', 'add_modifyopinion');
INSERT INTO `auth_permission` VALUES ('47', 'Can change 打样修改意见表', '16', 'change_modifyopinion');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete 打样修改意见表', '16', 'delete_modifyopinion');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 操作工表', '17', 'add_worker');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 操作工表', '17', 'change_worker');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 操作工表', '17', 'delete_worker');
INSERT INTO `auth_permission` VALUES ('52', 'Can add 打样表', '18', 'add_proofingprogress');
INSERT INTO `auth_permission` VALUES ('53', 'Can change 打样表', '18', 'change_proofingprogress');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete 打样表', '18', 'delete_proofingprogress');
INSERT INTO `auth_permission` VALUES ('55', 'Can add 生产车间表', '19', 'add_productionworkshop');
INSERT INTO `auth_permission` VALUES ('56', 'Can change 生产车间表', '19', 'change_productionworkshop');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete 生产车间表', '19', 'delete_productionworkshop');
INSERT INTO `auth_permission` VALUES ('58', 'Can add 大货表', '20', 'add_productionschedule');
INSERT INTO `auth_permission` VALUES ('59', 'Can change 大货表', '20', 'change_productionschedule');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete 大货表', '20', 'delete_productionschedule');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 报价单表', '21', 'add_quotation');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 报价单表', '21', 'change_quotation');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 报价单表', '21', 'delete_quotation');
INSERT INTO `auth_permission` VALUES ('64', 'Can add 核算单表', '22', 'add_accountingdocuments');
INSERT INTO `auth_permission` VALUES ('65', 'Can change 核算单表', '22', 'change_accountingdocuments');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete 核算单表', '22', 'delete_accountingdocuments');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$100000$kpd5RZ6ziNVS$ybkdRh2rX06o3Fd8i3YTAZ3VfAD+jzBaTBZO/FEO1T4=', '2019-07-08 09:16:48.699201', '1', 'order', '', '', 'order@qq.com', '1', '1', '2019-06-28 13:25:09.313600');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=296 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-06-28 15:07:06.727600', '1', '绣花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-06-28 15:07:19.646600', '2', '印花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-06-28 15:07:30.962600', '3', '绣花+印花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-06-28 15:07:42.008600', '4', '空白', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-06-28 15:07:54.894600', '5', '其他', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-06-28 15:08:03.297600', '1', '后扣1', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-06-28 15:08:09.134600', '2', '后扣2', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-06-28 15:08:18.936600', '1', 'nike', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-06-28 15:08:25.975600', '2', 'adidas', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-06-28 15:08:37.555600', '1', '平眉帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-06-28 15:08:49.812600', '2', '弯眉帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-06-28 15:08:58.468600', '1', '红色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-06-28 15:09:03.206600', '2', '蓝色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-06-28 15:09:10.686600', '3', '白色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-06-28 15:09:16.140600', '4', '灰色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-06-28 15:09:23.584600', '1', '平眉', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-06-28 15:09:28.681600', '2', '弯眉', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-06-28 15:09:39.527600', '1', '111111111', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-06-28 15:09:46.168600', '2', '222222222', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-07-01 13:59:11.804008', '1', '王师傅', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-07-01 13:59:32.278008', '2', '李师傅', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2019-07-01 13:59:41.781008', '1', '王师傅', '2', '[{\"changed\": {\"fields\": [\"u_username\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2019-07-01 13:59:46.449008', '2', '李师傅', '2', '[{\"changed\": {\"fields\": [\"u_username\"]}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2019-07-01 15:54:44.549008', '1', '123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2019-07-01 15:55:51.466008', '2', '123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2019-07-01 16:15:44.886008', '3', '123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2019-07-02 14:27:03.842201', '1', '工人一', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2019-07-02 14:27:17.629201', '2', '工人二', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2019-07-02 15:21:12.431201', '1', '123', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2019-07-02 15:24:04.252201', '1', '123', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2019-07-02 15:26:20.513201', '1', '123', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2019-07-02 15:31:22.865201', '2', '123123', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2019-07-02 15:34:15.285201', '3', '111111', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2019-07-02 16:06:30.937201', '4', '11111', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2019-07-02 16:18:06.498201', '5', '123123', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2019-07-02 16:18:27.966201', '6', '121212', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2019-07-02 16:19:26.379201', '7', '122112', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2019-07-02 16:21:13.868201', '7', '122112', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2019-07-02 16:21:37.867201', '13', '123456', '2', '[{\"changed\": {\"fields\": [\"o_pp_all_end\"]}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2019-07-02 16:23:00.525201', '7', '122112', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2019-07-02 16:23:45.834201', '8', '112211', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2019-07-02 16:24:09.994201', '9', '111223', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2019-07-03 09:20:02.833600', '1', '123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2019-07-03 09:20:02.949600', '2', '123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2019-07-04 11:07:36.854600', '1', '车间一', '1', '[{\"added\": {}}]', '19', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2019-07-04 11:07:41.133600', '2', '车间二', '1', '[{\"added\": {}}]', '19', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2019-07-04 12:58:53.961600', '1', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2019-07-04 13:00:59.954600', '2', '121212', '2', '[{\"changed\": {\"fields\": [\"ps_number\", \"ps_date\"]}}]', '20', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2019-07-04 13:12:17.387600', '2', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2019-07-04 13:12:17.499600', '3', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('51', '2019-07-04 13:12:17.608600', '4', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2019-07-04 15:20:34.559600', '1', 'None', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2019-07-04 15:20:34.718600', '2', 'None', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2019-07-04 15:21:50.617600', '4', '123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2019-07-04 15:21:50.726600', '9', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('56', '2019-07-04 15:21:50.808600', '13', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('57', '2019-07-04 15:21:50.901600', '14', '111111', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('58', '2019-07-04 15:21:51.084600', '15', '222222', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('59', '2019-07-04 15:21:51.329600', '18', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('60', '2019-07-04 15:21:51.458600', '19', '111223', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('61', '2019-07-04 15:21:51.552600', '20', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('62', '2019-07-04 15:22:03.896600', '3', '1234', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('63', '2019-07-04 15:22:04.005600', '4', '12345', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('64', '2019-07-04 15:22:04.112600', '5', '123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('65', '2019-07-04 15:22:04.212600', '6', '1231\r\n12312\r\n123123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('66', '2019-07-04 15:22:11.771600', '1', '123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('67', '2019-07-04 15:22:11.871600', '2', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('68', '2019-07-04 15:22:11.964600', '3', '111111', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('69', '2019-07-04 15:22:12.054600', '4', '11111', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('70', '2019-07-04 15:22:12.148600', '5', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('71', '2019-07-04 15:22:12.246600', '6', '121212', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('72', '2019-07-04 15:22:12.364600', '7', '122112', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('73', '2019-07-04 15:22:12.464600', '8', '112211', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('74', '2019-07-04 15:22:12.573600', '9', '111223', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('75', '2019-07-04 15:22:12.704600', '10', '123212', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('76', '2019-07-04 15:22:12.857600', '11', '123333', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('77', '2019-07-04 15:22:13.021600', '12', '122233', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('78', '2019-07-04 15:22:13.223600', '13', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('79', '2019-07-04 15:22:13.313600', '14', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('80', '2019-07-04 15:22:13.406600', '15', '122123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('81', '2019-07-04 15:22:13.496600', '16', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('82', '2019-07-04 15:22:13.589600', '17', '123112', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('83', '2019-07-04 15:22:24.371600', '5', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('84', '2019-07-04 15:22:24.526600', '6', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('85', '2019-07-04 15:22:33.412600', '1', '1', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('86', '2019-07-04 15:22:33.635600', '2', '1', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('87', '2019-07-04 15:22:33.759600', '3', '1', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('88', '2019-07-04 16:55:19.356600', '12', '121212', '2', '[{\"changed\": {\"fields\": [\"ps_end\"]}}]', '20', '1');
INSERT INTO `django_admin_log` VALUES ('89', '2019-07-05 14:13:37.150400', '21', '111111', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('90', '2019-07-05 14:13:37.265400', '22', '222222', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('91', '2019-07-05 14:13:37.367400', '23', '123121', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('92', '2019-07-05 14:13:37.473400', '24', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('93', '2019-07-05 14:13:37.622400', '25', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('94', '2019-07-05 14:13:37.773400', '26', '123123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('95', '2019-07-05 14:13:37.867400', '27', '12312312', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('96', '2019-07-05 14:13:37.964400', '28', '1234', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('97', '2019-07-05 14:13:47.689400', '3', '123', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('98', '2019-07-05 14:13:47.786400', '4', '11', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('99', '2019-07-05 14:13:47.892400', '5', '123', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('100', '2019-07-05 14:13:48.242400', '6', '123', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('101', '2019-07-05 14:13:48.459400', '7', '1', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('102', '2019-07-05 14:13:48.552400', '8', '1', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('103', '2019-07-05 14:13:48.651400', '9', '460.80', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('104', '2019-07-05 14:13:55.391400', '4', '12', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('105', '2019-07-05 14:13:55.496400', '5', '12', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('106', '2019-07-05 14:13:55.652400', '6', '123', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('107', '2019-07-05 14:13:55.745400', '7', '123', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('108', '2019-07-05 14:13:55.852400', '8', '1', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('109', '2019-07-05 14:13:55.954400', '9', '123', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('110', '2019-07-05 14:13:56.060400', '10', '115.20', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('111', '2019-07-05 14:13:56.154400', '11', 'None', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('112', '2019-07-05 14:13:56.311400', '12', '8.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('113', '2019-07-05 14:14:04.108400', '18', '121212', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('114', '2019-07-05 14:14:04.206400', '19', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('115', '2019-07-05 14:14:04.321400', '20', '123111', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('116', '2019-07-05 14:14:04.432400', '21', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('117', '2019-07-05 14:14:04.672400', '22', '123333', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('118', '2019-07-05 14:14:04.990400', '23', '111111', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('119', '2019-07-05 14:14:05.088400', '24', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('120', '2019-07-05 14:14:05.182400', '25', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('121', '2019-07-05 14:14:05.279400', '26', '123132', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('122', '2019-07-05 14:14:05.364400', '27', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('123', '2019-07-05 14:14:05.529400', '28', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('124', '2019-07-05 14:14:05.623400', '29', '123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('125', '2019-07-05 14:14:05.713400', '30', '1231', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('126', '2019-07-05 14:14:11.841400', '7', '123123\r\n123123\r\n123123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('127', '2019-07-05 14:14:11.949400', '8', '123\r\n123\r\n123\r\n123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('128', '2019-07-05 14:14:12.064400', '9', '123123\r\n12312312\r\n123123\r\n12312', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('129', '2019-07-05 14:14:12.174400', '10', '4123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('130', '2019-07-05 14:14:12.330400', '11', '1231231\r\n12312\r\n13123\r\n123123\r\n123123', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('131', '2019-07-05 14:14:12.432400', '12', 'qewrqewrqw\r\nqewrqwer\r\nqwerqwer\r\nqwerqewr\r\nqewrqwer\r\nqwerqwerq\r\nqewrqewr\r\nqewrqwer\r\nqwerqwe\r\nadfjasldfj', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('132', '2019-07-05 14:14:20.755400', '7', '123123', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('133', '2019-07-05 14:14:20.926400', '8', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('134', '2019-07-05 14:14:21.024400', '9', '123123', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('135', '2019-07-05 14:14:21.135400', '10', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('136', '2019-07-05 14:14:21.249400', '11', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('137', '2019-07-05 14:14:21.407400', '12', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('138', '2019-07-05 14:14:21.524400', '13', '412312', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('139', '2019-07-05 14:14:21.626400', '14', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('140', '2019-07-05 15:37:28.805400', '29', '121212', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('141', '2019-07-05 15:37:28.908400', '30', '123321', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('142', '2019-07-05 15:37:29.133400', '31', '12341234', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('143', '2019-07-05 15:37:36.749400', '10', '1968.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('144', '2019-07-05 15:37:36.851400', '11', '96.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('145', '2019-07-05 15:37:36.950400', '12', '96.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('146', '2019-07-05 15:37:43.293400', '13', '16.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('147', '2019-07-05 15:37:43.402400', '14', '8.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('148', '2019-07-05 15:37:43.501400', '15', '8.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('149', '2019-07-05 15:37:49.435400', '13', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('150', '2019-07-05 15:37:49.545400', '14', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('151', '2019-07-05 15:37:49.685400', '15', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('152', '2019-07-05 15:37:55.255400', '31', 'None', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('153', '2019-07-05 15:37:55.421400', '32', 'None', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('154', '2019-07-05 15:37:55.530400', '33', 'None', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('155', '2019-07-05 15:38:03.726400', '15', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('156', '2019-07-05 15:38:03.830400', '16', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('157', '2019-07-05 15:38:03.915400', '17', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('158', '2019-07-08 09:10:02.197201', '36', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('159', '2019-07-08 09:10:02.296201', '35', '12312', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('160', '2019-07-08 09:10:02.421201', '34', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('161', '2019-07-08 09:10:02.521201', '33', '123456', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('162', '2019-07-08 09:10:02.671201', '32', '111111', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('163', '2019-07-08 09:10:09.530201', '1', '绣花', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('164', '2019-07-08 09:10:09.690201', '2', '印花', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('165', '2019-07-08 09:10:09.790201', '3', '绣花+印花', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('166', '2019-07-08 09:10:09.890201', '4', '空白', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('167', '2019-07-08 09:10:09.988201', '5', '其他', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('168', '2019-07-08 09:10:17.585201', '1', '111111111', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('169', '2019-07-08 09:10:17.682201', '2', '222222222', '3', '', '15', '1');
INSERT INTO `django_admin_log` VALUES ('170', '2019-07-08 09:10:26.129201', '1', '平眉', '3', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('171', '2019-07-08 09:10:26.414201', '2', '弯眉', '3', '', '13', '1');
INSERT INTO `django_admin_log` VALUES ('172', '2019-07-08 09:10:33.477201', '1', '红色', '3', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('173', '2019-07-08 09:10:33.585201', '2', '蓝色', '3', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('174', '2019-07-08 09:10:33.753201', '3', '白色', '3', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('175', '2019-07-08 09:10:33.860201', '4', '灰色', '3', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('176', '2019-07-08 09:10:41.263201', '1', '平眉帽', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('177', '2019-07-08 09:10:41.372201', '2', '弯眉帽', '3', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('178', '2019-07-08 09:10:47.533201', '1', 'nike', '3', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('179', '2019-07-08 09:10:47.639201', '2', 'adidas', '3', '', '12', '1');
INSERT INTO `django_admin_log` VALUES ('180', '2019-07-08 09:10:53.496201', '1', '后扣1', '3', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('181', '2019-07-08 09:10:53.598201', '2', '后扣2', '3', '', '14', '1');
INSERT INTO `django_admin_log` VALUES ('182', '2019-07-08 09:11:00.968201', '1', '王师傅', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('183', '2019-07-08 09:11:01.060201', '2', '李师傅', '3', '', '7', '1');
INSERT INTO `django_admin_log` VALUES ('184', '2019-07-08 09:11:07.589201', '13', '92400.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('185', '2019-07-08 09:11:07.736201', '14', 'None', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('186', '2019-07-08 09:11:07.843201', '15', '8000.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('187', '2019-07-08 09:11:07.952201', '16', 'None', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('188', '2019-07-08 09:11:08.051201', '17', '80000.00', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('189', '2019-07-08 09:11:13.893201', '16', '92.40', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('190', '2019-07-08 09:11:14.004201', '17', 'None', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('191', '2019-07-08 09:11:14.094201', '18', '8.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('192', '2019-07-08 09:11:14.302201', '19', '496.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('193', '2019-07-08 09:11:14.421201', '20', '8.00', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('194', '2019-07-08 09:11:20.025201', '16', '好！好！好！\r\n好！\r\n好！\r\n好！\r\n好！好！好！\r\n好！\r\n好！\r\n好！\r\n好！好！好！', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('195', '2019-07-08 09:11:20.130201', '17', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('196', '2019-07-08 09:11:20.279201', '18', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('197', '2019-07-08 09:11:20.389201', '19', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('198', '2019-07-08 09:11:20.678201', '20', '123\r\nfasd\r\nasfd\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\nasdf\r\na\r\nf', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('199', '2019-07-08 09:11:25.825201', '34', '121212', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('200', '2019-07-08 09:11:25.979201', '35', 'None', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('201', '2019-07-08 09:11:26.072201', '36', '123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('202', '2019-07-08 09:11:26.163201', '37', '123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('203', '2019-07-08 09:11:26.248201', '38', '123123', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('204', '2019-07-08 09:11:33.951201', '1', '工人一', '3', '', '17', '1');
INSERT INTO `django_admin_log` VALUES ('205', '2019-07-08 09:11:34.056201', '2', '工人二', '3', '', '17', '1');
INSERT INTO `django_admin_log` VALUES ('206', '2019-07-08 09:11:40.649201', '1', '车间一', '3', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('207', '2019-07-08 09:11:40.859201', '2', '车间二', '3', '', '19', '1');
INSERT INTO `django_admin_log` VALUES ('208', '2019-07-08 09:11:45.379201', '19', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('209', '2019-07-08 09:11:45.493201', '20', '121212', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('210', '2019-07-08 09:17:42.908201', '3', '上海样品间', '1', '[{\"added\": {}}]', '19', '1');
INSERT INTO `django_admin_log` VALUES ('211', '2019-07-08 09:18:13.163201', '4', '上海大货车间', '1', '[{\"added\": {}}]', '19', '1');
INSERT INTO `django_admin_log` VALUES ('212', '2019-07-08 09:18:25.957201', '5', '东海大货车间', '1', '[{\"added\": {}}]', '19', '1');
INSERT INTO `django_admin_log` VALUES ('213', '2019-07-08 09:19:03.710201', '3', '六片帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('214', '2019-07-08 09:19:14.038201', '4', '盆帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('215', '2019-07-08 09:19:25.218201', '5', '沙滩帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('216', '2019-07-08 09:19:35.959201', '6', '空顶帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('217', '2019-07-08 09:19:46.203201', '7', '五片网眼帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('218', '2019-07-08 09:19:57.462201', '8', '军帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('219', '2019-07-08 09:20:31.186201', '9', '五片帽', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('220', '2019-07-08 09:20:51.804201', '6', '绣花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('221', '2019-07-08 09:21:03.153201', '7', '印花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('222', '2019-07-08 09:21:17.133201', '8', '绣花+印花', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('223', '2019-07-08 09:21:28.964201', '9', '无', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('224', '2019-07-08 09:36:39.657201', '9', '空白', '2', '[{\"changed\": {\"fields\": [\"eop_type\"]}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('225', '2019-07-08 09:36:54.054201', '10', '其它', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('226', '2019-07-08 09:38:39.807201', '3', '弯眉DK-283(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('227', '2019-07-08 09:39:19.566201', '4', '弯眉加硬 759Q(2.6mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('228', '2019-07-08 09:39:52.959201', '5', '加硬 稍弯眉 509N(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('229', '2019-07-08 09:40:39.863201', '6', '平眉DK-214-1(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('230', '2019-07-08 09:41:05.669201', '7', '平眉480N(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('231', '2019-07-08 09:41:33.537201', '8', '弯眉669Q(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('232', '2019-07-08 09:42:10.491201', '9', '加硬平眉507N(2.4mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('233', '2019-07-08 09:42:41.764201', '10', '弯眉BE-001(2.6mm)', '1', '[{\"added\": {}}]', '13', '1');
INSERT INTO `django_admin_log` VALUES ('234', '2019-07-08 09:43:11.012201', '3', '759Q', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('235', '2019-07-08 09:43:26.635201', '4', 'DK-283', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('236', '2019-07-08 09:43:38.551201', '5', '806Q', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('237', '2019-07-08 09:43:57.327201', '6', '306W', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('238', '2019-07-08 09:44:11.932201', '7', '480N', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('239', '2019-07-08 09:44:25.861201', '8', '669Q', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('240', '2019-07-08 09:44:38.425201', '9', '611N', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('241', '2019-07-08 09:44:55.971201', '10', '785A-B', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('242', '2019-07-08 09:45:15.303201', '11', 'W084', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('243', '2019-07-08 11:14:48.485201', '3', 'Madness', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('244', '2019-07-08 11:15:06.092201', '4', '上海优加服饰', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('245', '2019-07-08 11:15:20.533201', '5', '大连圣马国际', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('246', '2019-07-08 11:15:37.180201', '6', '上海智丰', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('247', '2019-07-08 11:18:36.015201', '2', '潘军', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('248', '2019-07-08 11:18:47.883201', '3', '李浩岚', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('249', '2019-07-08 11:19:14.062201', '4', '张黎', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('250', '2019-07-08 11:20:31.598201', '4', '张黎', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('251', '2019-07-08 11:20:31.897201', '3', '李浩岚', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('252', '2019-07-08 11:20:32.003201', '2', '潘军', '3', '', '4', '1');
INSERT INTO `django_admin_log` VALUES ('253', '2019-07-08 11:21:18.554201', '3', '李浩岚', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('254', '2019-07-08 11:21:46.221201', '4', '潘军', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('255', '2019-07-08 14:15:44.302400', '38', '123123123', '3', '', '11', '1');
INSERT INTO `django_admin_log` VALUES ('256', '2019-07-08 14:16:00.182400', '19', 'None', '3', '', '22', '1');
INSERT INTO `django_admin_log` VALUES ('257', '2019-07-08 14:16:06.940400', '22', 'None', '3', '', '21', '1');
INSERT INTO `django_admin_log` VALUES ('258', '2019-07-08 14:16:15.444400', '40', 'None', '3', '', '18', '1');
INSERT INTO `django_admin_log` VALUES ('259', '2019-07-08 14:16:22.480400', '22', 'None', '3', '', '16', '1');
INSERT INTO `django_admin_log` VALUES ('260', '2019-07-08 14:16:29.788400', '24', 'None', '3', '', '20', '1');
INSERT INTO `django_admin_log` VALUES ('261', '2019-07-09 13:08:09.361400', '5', '顾永莲', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('262', '2019-07-09 13:08:54.106400', '6', '邵菊芳', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('263', '2019-07-09 13:09:49.354400', '7', '王建香', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('264', '2019-07-09 13:10:53.862400', '8', '盛燕萍', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('265', '2019-07-09 13:11:58.796400', '9', '张黎', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('266', '2019-07-09 13:13:22.098400', '1', '本布条+古铜手套扣+绣扣洞', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('267', '2019-07-09 13:13:35.455400', '2', '单排塑料排扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('268', '2019-07-09 13:14:05.209400', '3', '本布+同冠色雌雄粘扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('269', '2019-07-09 13:14:22.960400', '4', '本布条+压花夹扣+插孔', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('270', '2019-07-09 13:15:09.124400', '5', '本布+金属夹扣+插环', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('271', '2019-07-09 13:15:33.857400', '6', '本布条+日字扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('272', '2019-07-09 13:15:50.927400', '7', '双排塑料排扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('273', '2019-07-09 13:16:33.837400', '8', '本布+夹扣+插孔', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('274', '2019-07-09 13:16:54.333400', '9', '黑色织带+黑色塑料插扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('275', '2019-07-09 13:17:24.342400', '10', '雌雄粘扣', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('276', '2019-07-09 13:18:10.308400', '9', '织带+塑料插扣', '2', '[{\"changed\": {\"fields\": [\"ad_type\"]}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('277', '2019-07-09 13:20:06.222400', '1', '黑色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('278', '2019-07-09 13:20:30.660400', '2', '灰色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('279', '2019-07-09 13:20:53.678400', '3', '蓝色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('280', '2019-07-09 13:21:11.133400', '4', '漂白', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('281', '2019-07-09 13:21:27.474400', '5', '黄色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('282', '2019-07-09 13:21:51.432400', '6', '橄绿', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('283', '2019-07-09 16:44:07.737400', '39', 'None', '2', '[{\"changed\": {\"fields\": [\"pp_end\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('284', '2019-07-10 08:34:27.350700', '10', '张婷婷', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('285', '2019-07-10 08:35:32.697700', '7', '今世多开发商品', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('286', '2019-07-10 08:39:56.156700', '7', '浅米', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('287', '2019-07-10 13:19:14.472700', '8', '卡其', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('288', '2019-07-10 13:19:29.333700', '9', '红色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('289', '2019-07-10 13:19:44.079700', '10', '麻灰', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('290', '2019-07-10 13:19:57.715700', '11', '藏青', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('291', '2019-07-10 13:20:11.296700', '12', '白色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('292', '2019-07-10 13:20:23.308700', '13', '橘色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('293', '2019-07-10 13:20:37.393700', '14', '棕色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('294', '2019-07-10 13:20:39.347700', '15', '棕色', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('295', '2019-07-10 13:20:55.066700', '16', '绿色', '1', '[{\"added\": {}}]', '10', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('22', 'accounting_documents', 'accountingdocuments');
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('14', 'order', 'afterdeduction');
INSERT INTO `django_content_type` VALUES ('10', 'order', 'capcolor');
INSERT INTO `django_content_type` VALUES ('13', 'order', 'capeyebrow');
INSERT INTO `django_content_type` VALUES ('9', 'order', 'captype');
INSERT INTO `django_content_type` VALUES ('12', 'order', 'customer');
INSERT INTO `django_content_type` VALUES ('8', 'order', 'embroiderorprint');
INSERT INTO `django_content_type` VALUES ('11', 'order', 'order');
INSERT INTO `django_content_type` VALUES ('15', 'order', 'versionnumber');
INSERT INTO `django_content_type` VALUES ('20', 'production_schedule', 'productionschedule');
INSERT INTO `django_content_type` VALUES ('19', 'production_schedule', 'productionworkshop');
INSERT INTO `django_content_type` VALUES ('16', 'proofing_progress', 'modifyopinion');
INSERT INTO `django_content_type` VALUES ('18', 'proofing_progress', 'proofingprogress');
INSERT INTO `django_content_type` VALUES ('17', 'proofing_progress', 'worker');
INSERT INTO `django_content_type` VALUES ('21', 'quotation', 'quotation');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'user', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-06-28 13:22:57.039600');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-06-28 13:23:37.116600');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-06-28 13:23:48.831600');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-06-28 13:23:48.935600');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-06-28 13:23:53.014600');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-06-28 13:23:56.137600');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-06-28 13:24:00.901600');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-06-28 13:24:00.943600');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-06-28 13:24:02.002600');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-06-28 13:24:02.075600');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-06-28 13:24:02.135600');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-06-28 13:24:03.429600');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-06-28 13:24:04.693600');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2019-06-28 13:24:05.883600');
INSERT INTO `django_migrations` VALUES ('15', 'user', '0001_initial', '2019-06-28 13:24:06.673600');
INSERT INTO `django_migrations` VALUES ('16', 'order', '0001_initial', '2019-06-28 14:58:57.910600');
INSERT INTO `django_migrations` VALUES ('17', 'order', '0002_order_o_user', '2019-06-28 15:33:44.761600');
INSERT INTO `django_migrations` VALUES ('18', 'order', '0003_auto_20190702_0900', '2019-07-02 09:02:05.204201');
INSERT INTO `django_migrations` VALUES ('19', 'proofing_progress', '0001_initial', '2019-07-02 14:24:08.529201');
INSERT INTO `django_migrations` VALUES ('20', 'order', '0004_auto_20190702_1423', '2019-07-02 14:24:32.376201');
INSERT INTO `django_migrations` VALUES ('21', 'order', '0005_order_o_pp_all_end', '2019-07-02 14:44:23.543201');
INSERT INTO `django_migrations` VALUES ('22', 'proofing_progress', '0002_proofingprogress_pp_end', '2019-07-02 14:44:26.305201');
INSERT INTO `django_migrations` VALUES ('23', 'order', '0006_auto_20190702_1559', '2019-07-02 15:59:29.976201');
INSERT INTO `django_migrations` VALUES ('24', 'order', '0007_auto_20190703_0918', '2019-07-03 09:18:18.375600');
INSERT INTO `django_migrations` VALUES ('25', 'production_schedule', '0001_initial', '2019-07-04 11:00:13.730600');
INSERT INTO `django_migrations` VALUES ('26', 'order', '0008_order_o_productionschedule', '2019-07-04 11:00:26.876600');
INSERT INTO `django_migrations` VALUES ('27', 'quotation', '0001_initial', '2019-07-04 13:37:33.143600');
INSERT INTO `django_migrations` VALUES ('28', 'order', '0009_order_o_quotation', '2019-07-04 13:37:46.624600');
INSERT INTO `django_migrations` VALUES ('29', 'accounting_documents', '0001_initial', '2019-07-04 14:42:40.096600');
INSERT INTO `django_migrations` VALUES ('30', 'order', '0010_order_o_accountingdocuments', '2019-07-04 14:42:55.981600');
INSERT INTO `django_migrations` VALUES ('31', 'production_schedule', '0002_auto_20190704_1628', '2019-07-04 16:28:23.504600');
INSERT INTO `django_migrations` VALUES ('32', 'order', '0011_order_o_end', '2019-07-04 16:30:13.840600');
INSERT INTO `django_migrations` VALUES ('33', 'production_schedule', '0003_productionschedule_ps_end', '2019-07-04 16:51:55.639600');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1e20y38rr1qd9jefydkteqn35edz68r1', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-12 15:24:29.505600');
INSERT INTO `django_session` VALUES ('cskb0hpoqw29uq0tm3hx5owi9cyzqaa4', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-18 11:07:26.868600');
INSERT INTO `django_session` VALUES ('k19q7ra9vqknckyso1en965vf3138c19', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-15 13:58:56.088008');
INSERT INTO `django_session` VALUES ('lxaoc2j1w494bouyaax5s8wx7k49z7eb', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-16 14:25:04.063201');
INSERT INTO `django_session` VALUES ('t3gaezi2rzoo8yawl532ah1b4qcrrhtw', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-22 09:16:48.789201');
INSERT INTO `django_session` VALUES ('ulpd2zgpcodw5ru0dv1osmblll0zotwz', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-12 13:25:52.598600');
INSERT INTO `django_session` VALUES ('us6wty80lvf5w4hrg4fvicty1z0o9jpq', 'MjJlOGEyODA1MGY2MzQzYjFhNGZkNWVjMDA2NzI3YjA3NjA0NzdhNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYjg3MTFiOGQyNTE2ZGY3NmNjZjBmZjIyNzI4YTlkMDA1Yzc4M2U3In0=', '2019-07-17 09:16:46.708600');

-- ----------------------------
-- Table structure for order_afterdeduction
-- ----------------------------
DROP TABLE IF EXISTS `order_afterdeduction`;
CREATE TABLE `order_afterdeduction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ad_id` char(32) NOT NULL,
  `ad_type` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_afterdeduction
-- ----------------------------
INSERT INTO `order_afterdeduction` VALUES ('1', '3f9107c64bae48278b34f5e1fa822da6', '本布条+古铜手套扣+绣扣洞', '2019-07-09 13:13:22.097400', '2019-07-09 13:13:22.097400', '0');
INSERT INTO `order_afterdeduction` VALUES ('2', 'ae9e23849d7e40d38afa1b402deee734', '单排塑料排扣', '2019-07-09 13:13:35.455400', '2019-07-09 13:13:35.455400', '0');
INSERT INTO `order_afterdeduction` VALUES ('3', '18b567bf86cd4fd983c88d089031d6a0', '本布+同冠色雌雄粘扣', '2019-07-09 13:14:05.208400', '2019-07-09 13:14:05.209400', '0');
INSERT INTO `order_afterdeduction` VALUES ('4', 'f95e75226ec74b90becba01bea1d0b3e', '本布条+压花夹扣+插孔', '2019-07-09 13:14:22.959400', '2019-07-09 13:14:22.959400', '0');
INSERT INTO `order_afterdeduction` VALUES ('5', '7f94d0f1cfce4a8c9f3d07b700db1395', '本布+金属夹扣+插环', '2019-07-09 13:15:09.123400', '2019-07-09 13:15:09.123400', '0');
INSERT INTO `order_afterdeduction` VALUES ('6', 'ae90f40be9d344689bf01e28c4398eef', '本布条+日字扣', '2019-07-09 13:15:33.856400', '2019-07-09 13:15:33.856400', '0');
INSERT INTO `order_afterdeduction` VALUES ('7', '74e788fdf5214dde819dceeeba55e427', '双排塑料排扣', '2019-07-09 13:15:50.926400', '2019-07-09 13:15:50.926400', '0');
INSERT INTO `order_afterdeduction` VALUES ('8', '490b44f9330e4ed9a64dcbd8c7d5689c', '本布+夹扣+插孔', '2019-07-09 13:16:33.835400', '2019-07-09 13:16:33.835400', '0');
INSERT INTO `order_afterdeduction` VALUES ('9', '6ea6f7131af0431ab74e042309aae0ac', '织带+塑料插扣', '2019-07-09 13:16:54.332400', '2019-07-09 13:18:10.306400', '0');
INSERT INTO `order_afterdeduction` VALUES ('10', 'd0de23e99f0c47dea2dfd3e247533f81', '雌雄粘扣', '2019-07-09 13:17:24.341400', '2019-07-09 13:17:24.341400', '0');

-- ----------------------------
-- Table structure for order_capcolor
-- ----------------------------
DROP TABLE IF EXISTS `order_capcolor`;
CREATE TABLE `order_capcolor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cc_id` char(32) NOT NULL,
  `cc_color` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_capcolor
-- ----------------------------
INSERT INTO `order_capcolor` VALUES ('1', 'ab4c0dd936794006a23535ae6ceafd5e', '黑色', '2019-07-09 13:20:06.222400', '2019-07-09 13:20:06.222400', '0');
INSERT INTO `order_capcolor` VALUES ('2', '61ee390039a54202a0ed3ba96d6d83f7', '灰色', '2019-07-09 13:20:30.659400', '2019-07-09 13:20:30.659400', '0');
INSERT INTO `order_capcolor` VALUES ('3', '4e20af53a41b43e7bfd4b7d463883d04', '蓝色', '2019-07-09 13:20:53.677400', '2019-07-09 13:20:53.677400', '0');
INSERT INTO `order_capcolor` VALUES ('4', 'a434ee79a4c14766940d0f573926ec0b', '漂白', '2019-07-09 13:21:11.133400', '2019-07-09 13:21:11.133400', '0');
INSERT INTO `order_capcolor` VALUES ('5', 'd0174256ce11497f82e2093db6e73c6f', '黄色', '2019-07-09 13:21:27.474400', '2019-07-09 13:21:27.474400', '0');
INSERT INTO `order_capcolor` VALUES ('6', 'acbe583d4f60464aa13ebc3b2c27fdbd', '橄绿', '2019-07-09 13:21:51.431400', '2019-07-09 13:21:51.431400', '0');
INSERT INTO `order_capcolor` VALUES ('7', 'af0f49691cdc45a5a14b7ec319d21df1', '浅米', '2019-07-10 08:39:56.155700', '2019-07-10 08:39:56.155700', '0');
INSERT INTO `order_capcolor` VALUES ('8', '32a350cc8c1343bd9611fd3d761117fc', '卡其', '2019-07-10 13:19:14.471700', '2019-07-10 13:19:14.471700', '0');
INSERT INTO `order_capcolor` VALUES ('9', '4a6cae8f38184651bed83d8e9306d896', '红色', '2019-07-10 13:19:29.332700', '2019-07-10 13:19:29.332700', '0');
INSERT INTO `order_capcolor` VALUES ('10', 'de482f5d88d54c358d2251d9205aae32', '麻灰', '2019-07-10 13:19:44.078700', '2019-07-10 13:19:44.078700', '0');
INSERT INTO `order_capcolor` VALUES ('11', '448c123fa813460c950d748cc28c1354', '藏青', '2019-07-10 13:19:57.713700', '2019-07-10 13:19:57.713700', '0');
INSERT INTO `order_capcolor` VALUES ('12', 'c1017f7990bc49ceafeed688b4e6b574', '白色', '2019-07-10 13:20:11.296700', '2019-07-10 13:20:11.296700', '0');
INSERT INTO `order_capcolor` VALUES ('13', 'df18e6e5c9824d3aba270daee1cefd44', '橘色', '2019-07-10 13:20:23.308700', '2019-07-10 13:20:23.308700', '0');
INSERT INTO `order_capcolor` VALUES ('14', '8b57f17d677b450ea0bbca7c75af6089', '棕色', '2019-07-10 13:20:37.392700', '2019-07-10 13:20:37.392700', '0');
INSERT INTO `order_capcolor` VALUES ('15', '8b57f17d677b450ea0bbca7c75af6089', '棕色', '2019-07-10 13:20:39.346700', '2019-07-10 13:20:39.346700', '0');
INSERT INTO `order_capcolor` VALUES ('16', '0c84af43b06a4f5a874abcca44c72dd6', '绿色', '2019-07-10 13:20:55.065700', '2019-07-10 13:20:55.065700', '0');

-- ----------------------------
-- Table structure for order_capeyebrow
-- ----------------------------
DROP TABLE IF EXISTS `order_capeyebrow`;
CREATE TABLE `order_capeyebrow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ce_id` char(32) NOT NULL,
  `ce_type` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_capeyebrow
-- ----------------------------
INSERT INTO `order_capeyebrow` VALUES ('3', 'ef3eed1f3b16480f850477a5867e8a5a', '弯眉DK-283(2.4mm)', '2019-07-08 09:38:39.807201', '2019-07-08 09:38:39.807201', '0');
INSERT INTO `order_capeyebrow` VALUES ('4', '2de12887f416419f9872e21a57585c08', '弯眉加硬 759Q(2.6mm)', '2019-07-08 09:39:19.565201', '2019-07-08 09:39:19.565201', '0');
INSERT INTO `order_capeyebrow` VALUES ('5', 'df53d8e509ab48ac85adb109d9d597dd', '加硬 稍弯眉 509N(2.4mm)', '2019-07-08 09:39:52.957201', '2019-07-08 09:39:52.957201', '0');
INSERT INTO `order_capeyebrow` VALUES ('6', '74690d7d3e3741efa8a747389be9722e', '平眉DK-214-1(2.4mm)', '2019-07-08 09:40:39.862201', '2019-07-08 09:40:39.862201', '0');
INSERT INTO `order_capeyebrow` VALUES ('7', '710cd96f101d43bfaf39bdc80b2c2a22', '平眉480N(2.4mm)', '2019-07-08 09:41:05.668201', '2019-07-08 09:41:05.668201', '0');
INSERT INTO `order_capeyebrow` VALUES ('8', 'c293a29dad8041058ab5d0270b5ddd1c', '弯眉669Q(2.4mm)', '2019-07-08 09:41:33.536201', '2019-07-08 09:41:33.536201', '0');
INSERT INTO `order_capeyebrow` VALUES ('9', '86bc25a4d86243d78613d848dc62c9ee', '加硬平眉507N(2.4mm)', '2019-07-08 09:42:10.491201', '2019-07-08 09:42:10.491201', '0');
INSERT INTO `order_capeyebrow` VALUES ('10', '0fc449b5fb214be69ea6e18077526add', '弯眉BE-001(2.6mm)', '2019-07-08 09:42:41.763201', '2019-07-08 09:42:41.763201', '0');

-- ----------------------------
-- Table structure for order_captype
-- ----------------------------
DROP TABLE IF EXISTS `order_captype`;
CREATE TABLE `order_captype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ct_id` char(32) NOT NULL,
  `ct_type` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_captype
-- ----------------------------
INSERT INTO `order_captype` VALUES ('3', 'd46bac28375148e99686e6c9b44c82c3', '六片帽', '2019-07-08 09:19:03.709201', '2019-07-08 09:19:03.709201', '0');
INSERT INTO `order_captype` VALUES ('4', '5c90752c48b24dccbadf1390c5d3c693', '盆帽', '2019-07-08 09:19:14.036201', '2019-07-08 09:19:14.037201', '0');
INSERT INTO `order_captype` VALUES ('5', 'ecbce21db1504515a28981bd56c1ca51', '沙滩帽', '2019-07-08 09:19:25.216201', '2019-07-08 09:19:25.216201', '0');
INSERT INTO `order_captype` VALUES ('6', '460d8609302d48128d42bd5bc1c82fb8', '空顶帽', '2019-07-08 09:19:35.958201', '2019-07-08 09:19:35.958201', '0');
INSERT INTO `order_captype` VALUES ('7', 'ae42bade422943f48f8a8601796edff2', '五片网眼帽', '2019-07-08 09:19:46.203201', '2019-07-08 09:19:46.203201', '0');
INSERT INTO `order_captype` VALUES ('8', 'd1b979e8422d40b19ab41d4da7231e6f', '军帽', '2019-07-08 09:19:57.461201', '2019-07-08 09:19:57.461201', '0');
INSERT INTO `order_captype` VALUES ('9', 'f2816c54909e4375aa6a0ee77946e58e', '五片帽', '2019-07-08 09:20:31.186201', '2019-07-08 09:20:31.186201', '0');

-- ----------------------------
-- Table structure for order_customer
-- ----------------------------
DROP TABLE IF EXISTS `order_customer`;
CREATE TABLE `order_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` char(32) NOT NULL,
  `c_name` varchar(200) NOT NULL,
  `c_contack` varchar(200) NOT NULL,
  `c_email` varchar(254) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_customer
-- ----------------------------
INSERT INTO `order_customer` VALUES ('3', '0c3f90c429c8408fbcbd90eefbb8ca90', 'Madness', '苏先生', 'morrissu1963@gmail.com', '2019-07-08 11:14:48.483201', '2019-07-08 11:14:48.483201', '0');
INSERT INTO `order_customer` VALUES ('4', '84152f9bf0d2404cac28a16e8f8e29de', '上海优加服饰', '陈蔚', 'youjia@eiplas.com', '2019-07-08 11:15:06.090201', '2019-07-08 11:15:06.090201', '0');
INSERT INTO `order_customer` VALUES ('5', '813fdc3fd06b4bff82566c162a386f66', '大连圣马国际', '梁月娇', 'maggie@tbfashion.com.cn', '2019-07-08 11:15:20.533201', '2019-07-08 11:15:20.533201', '0');
INSERT INTO `order_customer` VALUES ('6', '32d8433f066c4feea953870333bc2f61', '上海智丰', '张先娇', 'alice@zoomf.cn', '2019-07-08 11:15:37.179201', '2019-07-08 11:15:37.179201', '0');
INSERT INTO `order_customer` VALUES ('7', '262af6ec365f4341bf4e4dc902cef40a', '今世多开发商品', '张婷婷', 'ztt@king-store.com', '2019-07-10 08:35:32.696700', '2019-07-10 08:35:32.696700', '0');

-- ----------------------------
-- Table structure for order_embroiderorprint
-- ----------------------------
DROP TABLE IF EXISTS `order_embroiderorprint`;
CREATE TABLE `order_embroiderorprint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eop_id` char(32) NOT NULL,
  `eop_type` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_embroiderorprint
-- ----------------------------
INSERT INTO `order_embroiderorprint` VALUES ('6', '71ea9dda2f6b4b3fb643131d7d4dc752', '绣花', '2019-07-08 09:20:51.804201', '2019-07-08 09:20:51.804201', '0');
INSERT INTO `order_embroiderorprint` VALUES ('7', '76aa52113fef435aa1a512b61c0c1e9c', '印花', '2019-07-08 09:21:03.152201', '2019-07-08 09:21:03.152201', '0');
INSERT INTO `order_embroiderorprint` VALUES ('8', '489ce9da967b406ba1140b61525db18e', '绣花+印花', '2019-07-08 09:21:17.132201', '2019-07-08 09:21:17.132201', '0');
INSERT INTO `order_embroiderorprint` VALUES ('9', 'c97bfaa4cf3c4f138b1330e4415da26e', '空白', '2019-07-08 09:21:28.962201', '2019-07-08 09:36:39.655201', '0');
INSERT INTO `order_embroiderorprint` VALUES ('10', '796b8df1ca64414fbc996977521c8560', '其它', '2019-07-08 09:36:54.054201', '2019-07-08 09:36:54.054201', '0');

-- ----------------------------
-- Table structure for order_order
-- ----------------------------
DROP TABLE IF EXISTS `order_order`;
CREATE TABLE `order_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `o_id` char(32) NOT NULL,
  `o_customer_number` varchar(200) NOT NULL,
  `o_date` date DEFAULT NULL,
  `o_price_type` varchar(200) NOT NULL,
  `o_dollar_type` varchar(200) NOT NULL,
  `o_count` int(11) DEFAULT NULL,
  `o_image` varchar(100) DEFAULT NULL,
  `o_file` varchar(100) DEFAULT NULL,
  `o_main_fabric` varchar(200) DEFAULT NULL,
  `o_ps_price` varchar(200) DEFAULT NULL,
  `o_dollar_exchange_rate` varchar(200) DEFAULT NULL,
  `o_dollar_price` varchar(200) DEFAULT NULL,
  `o_ps_amount` varchar(200) DEFAULT NULL,
  `o_ps_dollar_total_price` varchar(200) DEFAULT NULL,
  `o_delivery_date` date DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `o_afterdeduction_id` int(11) DEFAULT NULL,
  `o_capeyebrow_id` int(11) DEFAULT NULL,
  `o_captype_id` int(11) DEFAULT NULL,
  `o_customer_id` int(11) DEFAULT NULL,
  `o_embroiderorprint_id` int(11) DEFAULT NULL,
  `o_versionnumber_id` int(11) DEFAULT NULL,
  `o_user_id` int(11) DEFAULT NULL,
  `o_modifyopinion_id` int(11) DEFAULT NULL,
  `o_pp_all_end` tinyint(1) NOT NULL,
  `o_productionschedule_id` int(11) DEFAULT NULL,
  `o_quotation_id` int(11) DEFAULT NULL,
  `o_accountingdocuments_id` int(11) DEFAULT NULL,
  `o_end` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_o_modifyopinion_id_c0d7aa3c_uniq` (`o_modifyopinion_id`),
  UNIQUE KEY `o_productionschedule_id` (`o_productionschedule_id`),
  UNIQUE KEY `o_quotation_id` (`o_quotation_id`),
  UNIQUE KEY `o_accountingdocuments_id` (`o_accountingdocuments_id`),
  KEY `order_order_o_afterdeduction_id_5a49bcee` (`o_afterdeduction_id`),
  KEY `order_order_o_capeyebrow_id_aa51efd6` (`o_capeyebrow_id`),
  KEY `order_order_o_captype_id_71380878` (`o_captype_id`),
  KEY `order_order_o_customer_id_351a8037` (`o_customer_id`),
  KEY `order_order_o_embroiderorprint_id_af3be8b9` (`o_embroiderorprint_id`),
  KEY `order_order_o_user_id_c86a2936` (`o_user_id`),
  KEY `order_order_o_versionnumber_id_463b99d5` (`o_versionnumber_id`),
  CONSTRAINT `order_order_o_accountingdocument_c423bf94_fk_accountin` FOREIGN KEY (`o_accountingdocuments_id`) REFERENCES `accounting_documents_accountingdocuments` (`id`),
  CONSTRAINT `order_order_o_afterdeduction_id_5a49bcee_fk_order_aft` FOREIGN KEY (`o_afterdeduction_id`) REFERENCES `order_afterdeduction` (`id`),
  CONSTRAINT `order_order_o_capeyebrow_id_aa51efd6_fk_order_capeyebrow_id` FOREIGN KEY (`o_capeyebrow_id`) REFERENCES `order_capeyebrow` (`id`),
  CONSTRAINT `order_order_o_captype_id_71380878_fk_order_captype_id` FOREIGN KEY (`o_captype_id`) REFERENCES `order_captype` (`id`),
  CONSTRAINT `order_order_o_customer_id_351a8037_fk_order_customer_id` FOREIGN KEY (`o_customer_id`) REFERENCES `order_customer` (`id`),
  CONSTRAINT `order_order_o_embroiderorprint_i_af3be8b9_fk_order_emb` FOREIGN KEY (`o_embroiderorprint_id`) REFERENCES `order_embroiderorprint` (`id`),
  CONSTRAINT `order_order_o_modifyopinion_id_c0d7aa3c_fk_proofing_` FOREIGN KEY (`o_modifyopinion_id`) REFERENCES `proofing_progress_modifyopinion` (`id`),
  CONSTRAINT `order_order_o_productionschedule_21a560d1_fk_productio` FOREIGN KEY (`o_productionschedule_id`) REFERENCES `production_schedule_productionschedule` (`id`),
  CONSTRAINT `order_order_o_quotation_id_511e47c1_fk_quotation_quotation_id` FOREIGN KEY (`o_quotation_id`) REFERENCES `quotation_quotation` (`id`),
  CONSTRAINT `order_order_o_user_id_c86a2936_fk_user_user_id` FOREIGN KEY (`o_user_id`) REFERENCES `user_user` (`id`),
  CONSTRAINT `order_order_o_versionnumber_id_463b99d5_fk_order_ver` FOREIGN KEY (`o_versionnumber_id`) REFERENCES `order_versionnumber` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_order
-- ----------------------------
INSERT INTO `order_order` VALUES ('37', '318826aea12f11e9aa51005056c00008', '2019SS SURFING COMPLETE SEASON', '2019-06-10', '￥', '$', '4', 'image/2019/07/08/童帽大货照片.jpg', '', null, '16.88', '6.9', '2.45', '200', '490.00', null, '2019-07-08 11:19:27.823201', '2019-07-10 14:11:51.678700', '0', null, null, '9', '3', '6', null, '4', '21', '1', '23', '21', '18', '0');
INSERT INTO `order_order` VALUES ('38', 'f99acd8ca2eb11e98ca7005056c00008', '名爵车迷帽', '2019-06-28', '￥', '$', '2', 'image/2019/07/10/名爵车迷帽.png', '', '16*12纱卡', null, '6.9', null, null, null, null, '2019-07-10 16:23:20.037700', '2019-07-10 16:49:18.674700', '0', null, null, '9', '4', '6', null, '4', '22', '0', '24', '22', '19', '0');

-- ----------------------------
-- Table structure for order_order_o_capcolor
-- ----------------------------
DROP TABLE IF EXISTS `order_order_o_capcolor`;
CREATE TABLE `order_order_o_capcolor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `capcolor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_o_capcolor_order_id_capcolor_id_7309bdec_uniq` (`order_id`,`capcolor_id`),
  KEY `order_order_o_capcolor_capcolor_id_0b4d38e4_fk_order_capcolor_id` (`capcolor_id`),
  CONSTRAINT `order_order_o_capcolor_capcolor_id_0b4d38e4_fk_order_capcolor_id` FOREIGN KEY (`capcolor_id`) REFERENCES `order_capcolor` (`id`),
  CONSTRAINT `order_order_o_capcolor_order_id_37de618c_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_order_o_capcolor
-- ----------------------------
INSERT INTO `order_order_o_capcolor` VALUES ('3', '37', '13');
INSERT INTO `order_order_o_capcolor` VALUES ('4', '37', '14');
INSERT INTO `order_order_o_capcolor` VALUES ('6', '38', '1');

-- ----------------------------
-- Table structure for order_order_o_proofingprogress
-- ----------------------------
DROP TABLE IF EXISTS `order_order_o_proofingprogress`;
CREATE TABLE `order_order_o_proofingprogress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `proofingprogress_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_order_o_proofingpr_order_id_proofingprogres_3c6b8c95_uniq` (`order_id`,`proofingprogress_id`),
  KEY `order_order_o_proofi_proofingprogress_id_b20aaee0_fk_proofing_` (`proofingprogress_id`),
  CONSTRAINT `order_order_o_proofi_order_id_34e5deeb_fk_order_ord` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`),
  CONSTRAINT `order_order_o_proofi_proofingprogress_id_b20aaee0_fk_proofing_` FOREIGN KEY (`proofingprogress_id`) REFERENCES `proofing_progress_proofingprogress` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_order_o_proofingprogress
-- ----------------------------
INSERT INTO `order_order_o_proofingprogress` VALUES ('39', '37', '39');
INSERT INTO `order_order_o_proofingprogress` VALUES ('40', '37', '40');
INSERT INTO `order_order_o_proofingprogress` VALUES ('41', '38', '41');

-- ----------------------------
-- Table structure for order_versionnumber
-- ----------------------------
DROP TABLE IF EXISTS `order_versionnumber`;
CREATE TABLE `order_versionnumber` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vn_id` char(32) NOT NULL,
  `vn_version` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_versionnumber
-- ----------------------------
INSERT INTO `order_versionnumber` VALUES ('3', 'd346c48078db43daaec03d0cf2c62c83', '759Q', '2019-07-08 09:43:11.011201', '2019-07-08 09:43:11.011201', '0');
INSERT INTO `order_versionnumber` VALUES ('4', '2505339677264f2ea46c954b925ac51a', 'DK-283', '2019-07-08 09:43:26.634201', '2019-07-08 09:43:26.634201', '0');
INSERT INTO `order_versionnumber` VALUES ('5', '1ebb4dda18a04b02a9f12bc54573f80d', '806Q', '2019-07-08 09:43:38.549201', '2019-07-08 09:43:38.549201', '0');
INSERT INTO `order_versionnumber` VALUES ('6', '66e79cd7235d449dbba4ea41e6d9af01', '306W', '2019-07-08 09:43:57.326201', '2019-07-08 09:43:57.326201', '0');
INSERT INTO `order_versionnumber` VALUES ('7', '8d283ab325974fb085ec66337d35e93e', '480N', '2019-07-08 09:44:11.931201', '2019-07-08 09:44:11.931201', '0');
INSERT INTO `order_versionnumber` VALUES ('8', '3a23da02c15c4de29aecbaffb2e8eb7a', '669Q', '2019-07-08 09:44:25.860201', '2019-07-08 09:44:25.860201', '0');
INSERT INTO `order_versionnumber` VALUES ('9', '28fea3dc6a4041559ed0c54a69ffbe34', '611N', '2019-07-08 09:44:38.424201', '2019-07-08 09:44:38.424201', '0');
INSERT INTO `order_versionnumber` VALUES ('10', '3418b1cd371040ea8f7535710a385eec', '785A-B', '2019-07-08 09:44:55.970201', '2019-07-08 09:44:55.970201', '0');
INSERT INTO `order_versionnumber` VALUES ('11', 'c69c4003ae7c40219337e5801584f0f4', 'W084', '2019-07-08 09:45:15.302201', '2019-07-08 09:45:15.302201', '0');

-- ----------------------------
-- Table structure for production_schedule_productionschedule
-- ----------------------------
DROP TABLE IF EXISTS `production_schedule_productionschedule`;
CREATE TABLE `production_schedule_productionschedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ps_id` char(32) NOT NULL,
  `ps_number` varchar(200) DEFAULT NULL,
  `ps_date` date DEFAULT NULL,
  `ps_confirm_date` date DEFAULT NULL,
  `ps_arrival_date` date DEFAULT NULL,
  `ps_tailor_date` date DEFAULT NULL,
  `ps_embroider_date` date DEFAULT NULL,
  `ps_print_date` date DEFAULT NULL,
  `ps_water_washing_date` date DEFAULT NULL,
  `ps_sewing_date` date DEFAULT NULL,
  `ps_ingredients_fabric_arrival_date` date DEFAULT NULL,
  `ps_tags_arrival_date` date DEFAULT NULL,
  `ps_iron_package_date` date DEFAULT NULL,
  `ps_outward_transport_date` date DEFAULT NULL,
  `ps_gathering_date` date DEFAULT NULL,
  `ps_gathering_price` varchar(200) DEFAULT NULL,
  `ps_contract_balance` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `ps_workshop_id` int(11) DEFAULT NULL,
  `ps_end` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `production_schedule_productionschedule_ps_workshop_id_d65aabb1` (`ps_workshop_id`),
  CONSTRAINT `production_schedule__ps_workshop_id_d65aabb1_fk_productio` FOREIGN KEY (`ps_workshop_id`) REFERENCES `production_schedule_productionworkshop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of production_schedule_productionschedule
-- ----------------------------
INSERT INTO `production_schedule_productionschedule` VALUES ('23', '31cd1eeea12f11e9b242005056c00008', 'KS19-0717', '2019-07-10', null, '2019-06-18', null, null, null, null, null, null, null, null, '2019-07-10', null, null, null, '2019-07-08 11:19:28.258201', '2019-07-10 13:44:21.856700', '0', '4', '0');
INSERT INTO `production_schedule_productionschedule` VALUES ('24', 'f9deb45ca2eb11e9a59f005056c00008', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '2019-07-10 16:23:20.465700', '2019-07-10 16:23:20.465700', '0', null, '0');

-- ----------------------------
-- Table structure for production_schedule_productionworkshop
-- ----------------------------
DROP TABLE IF EXISTS `production_schedule_productionworkshop`;
CREATE TABLE `production_schedule_productionworkshop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pw_id` char(32) NOT NULL,
  `pw_workshop` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of production_schedule_productionworkshop
-- ----------------------------
INSERT INTO `production_schedule_productionworkshop` VALUES ('3', '094c278a094043f4b04471c22e31cca7', '上海样品间', '2019-07-08 09:17:42.907201', '2019-07-08 09:17:42.907201', '0');
INSERT INTO `production_schedule_productionworkshop` VALUES ('4', '1c3a524d1e774d4d9331ccb0ff595f48', '上海大货车间', '2019-07-08 09:18:13.162201', '2019-07-08 09:18:13.162201', '0');
INSERT INTO `production_schedule_productionworkshop` VALUES ('5', '1433c83535894db1acf6974b376f9017', '东海大货车间', '2019-07-08 09:18:25.957201', '2019-07-08 09:18:25.957201', '0');

-- ----------------------------
-- Table structure for proofing_progress_modifyopinion
-- ----------------------------
DROP TABLE IF EXISTS `proofing_progress_modifyopinion`;
CREATE TABLE `proofing_progress_modifyopinion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mo_id` char(32) NOT NULL,
  `mo_customer_info` longtext,
  `mo_factory_info` longtext,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of proofing_progress_modifyopinion
-- ----------------------------
INSERT INTO `proofing_progress_modifyopinion` VALUES ('21', '31be2acca12f11e9a719005056c00008', '2019.04.23\r\n牛仔的洗水效果他們看後不太接受, 所以會改做你們之前有做過辦的螢光橙色面料. 後面的金屬扣請用克叻色(橙色配青古銅跟樣辦是OK的). 後幅的MAD用白色, 前帽中的MONSTER請用黑色\r\n>\r\n> 2) 杏色的話其中一頂是洗水效果和尺寸都OK的, 另外一頂就只是看繡花顏色是OK的.\r\n>\r\n> 3) 後幅會加一個MAD-MONSTER的旗嘜, 先寄出2個給你做辦, 另外帽內會加一個MAIN LABEL, 此MAIN LABEL暫時未有辦, 我會再寄出給', null, '2019-07-08 11:19:28.159201', '2019-07-10 13:36:20.783700', '0');
INSERT INTO `proofing_progress_modifyopinion` VALUES ('22', 'f9d0aa9ca2eb11e99108005056c00008', null, null, '2019-07-10 16:23:20.374700', '2019-07-10 16:23:20.374700', '0');

-- ----------------------------
-- Table structure for proofing_progress_proofingprogress
-- ----------------------------
DROP TABLE IF EXISTS `proofing_progress_proofingprogress`;
CREATE TABLE `proofing_progress_proofingprogress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pp_id` char(32) NOT NULL,
  `pp_number` varchar(200) DEFAULT NULL,
  `pp_erp_number` varchar(200) DEFAULT NULL,
  `pp_date` date DEFAULT NULL,
  `pp_delivery_date` date DEFAULT NULL,
  `pp_main_fabric_arrival` date DEFAULT NULL,
  `pp_ingredients_fabric_arrival` date DEFAULT NULL,
  `pp_tailor_date` date DEFAULT NULL,
  `pp_send_embroide` date DEFAULT NULL,
  `pp_receive_embroide` date DEFAULT NULL,
  `pp_send_print` date DEFAULT NULL,
  `pp_receive_print` date DEFAULT NULL,
  `pp_delivery_proofing` date DEFAULT NULL,
  `pp_end_date` date DEFAULT NULL,
  `pp_express_date` date DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `pp_worker_id` int(11) DEFAULT NULL,
  `pp_end` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proofing_progress_pr_pp_worker_id_51164262_fk_proofing_` (`pp_worker_id`),
  CONSTRAINT `proofing_progress_pr_pp_worker_id_51164262_fk_proofing_` FOREIGN KEY (`pp_worker_id`) REFERENCES `proofing_progress_worker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of proofing_progress_proofingprogress
-- ----------------------------
INSERT INTO `proofing_progress_proofingprogress` VALUES ('39', '319e46bea12f11e9b2e6005056c00008', 'FW18-0025A', '19020059', '2019-04-10', '2019-04-19', null, null, null, null, null, null, null, null, '2019-07-19', null, '2019-07-08 11:19:27.951201', '2019-07-10 13:35:47.647700', '0', null, '1');
INSERT INTO `proofing_progress_proofingprogress` VALUES ('40', '206d94eea2d511e9b677005056c00008', 'FW18-0025B', '19040125', '2019-04-23', null, null, null, null, null, null, null, null, null, '2019-05-21', null, '2019-07-10 13:39:46.741700', '2019-07-10 13:40:02.889700', '0', null, '1');
INSERT INTO `proofing_progress_proofingprogress` VALUES ('41', 'f9a57beea2eb11e989e9005056c00008', 'PR19-0207', '19070001', '2019-06-28', null, '2019-06-28', null, null, null, null, null, '2019-07-10', '2019-07-10', null, null, '2019-07-10 16:23:20.091700', '2019-07-10 16:49:03.927700', '0', null, '0');

-- ----------------------------
-- Table structure for proofing_progress_worker
-- ----------------------------
DROP TABLE IF EXISTS `proofing_progress_worker`;
CREATE TABLE `proofing_progress_worker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `w_id` char(32) NOT NULL,
  `w_worker` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of proofing_progress_worker
-- ----------------------------

-- ----------------------------
-- Table structure for quotation_quotation
-- ----------------------------
DROP TABLE IF EXISTS `quotation_quotation`;
CREATE TABLE `quotation_quotation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `q_id` char(32) NOT NULL,
  `q_offer` varchar(200) DEFAULT NULL,
  `q_floating_rate` varchar(200) DEFAULT NULL,
  `q_end_offer` varchar(200) DEFAULT NULL,
  `q_fabric_quotation` varchar(200) DEFAULT NULL,
  `q_ingredients_quotation` varchar(200) DEFAULT NULL,
  `q_labor_payment_quotation` varchar(200) DEFAULT NULL,
  `q_water_washing_quotation` varchar(200) DEFAULT NULL,
  `q_embroider_quotation` varchar(200) DEFAULT NULL,
  `q_print_quotation` varchar(200) DEFAULT NULL,
  `q_packaging_quotation` varchar(200) DEFAULT NULL,
  `q_other_quotation` varchar(200) DEFAULT NULL,
  `q_reserved_profits` varchar(200) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of quotation_quotation
-- ----------------------------
INSERT INTO `quotation_quotation` VALUES ('21', '31e33efea12f11e99d76005056c00008', '16.88', '1.58', '26.67', '4.26', '1.86', '4.96', '3.20', '1.90', '0', '0.7', '0', '1', '2019-07-08 11:19:28.403201', '2019-07-10 14:02:54.786700', '0');
INSERT INTO `quotation_quotation` VALUES ('22', 'f9faa0cca2eb11e9a45d005056c00008', null, null, null, null, null, null, null, null, null, null, null, null, '2019-07-10 16:23:20.648700', '2019-07-10 16:23:20.648700', '0');

-- ----------------------------
-- Table structure for user_user
-- ----------------------------
DROP TABLE IF EXISTS `user_user`;
CREATE TABLE `user_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` char(32) NOT NULL,
  `u_name` varchar(200) NOT NULL,
  `u_username` varchar(200) NOT NULL,
  `u_password` varchar(200) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_end_date` datetime(6) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_user
-- ----------------------------
INSERT INTO `user_user` VALUES ('3', 'ba8826c8b1e640d181e0a732211215e5', '李浩岚', 'renee', 'ks201907', '2019-07-08 11:21:18.548201', '2019-07-08 11:21:18.549201', '0');
INSERT INTO `user_user` VALUES ('4', 'cda75958ddab47109861b806064950aa', '潘军', 'panjun', 'ks201907', '2019-07-08 11:21:46.220201', '2019-07-08 11:21:46.220201', '0');
INSERT INTO `user_user` VALUES ('5', 'c35b59683e8a4849845f6c3c9c2b679a', '顾永莲', 'shirley', 'ks201907', '2019-07-09 13:08:09.361400', '2019-07-09 13:08:09.361400', '0');
INSERT INTO `user_user` VALUES ('6', 'cdf2d2ff3be847eb816466c363ecef6b', '邵菊芳', 'dorothy', 'ks201907', '2019-07-09 13:08:54.106400', '2019-07-09 13:08:54.106400', '0');
INSERT INTO `user_user` VALUES ('7', '71446bead9cf49d196a59863b4d2bebc', '王建香', 'fanny', 'ks201907', '2019-07-09 13:09:49.354400', '2019-07-09 13:09:49.354400', '0');
INSERT INTO `user_user` VALUES ('8', '50a2182b004b4b68b17b425baccdfc97', '盛燕萍', 'kylie', 'ks201907', '2019-07-09 13:10:53.861400', '2019-07-09 13:10:53.861400', '0');
INSERT INTO `user_user` VALUES ('9', 'a8a0b78bb3d6420a885ae8b35e792b53', '张黎', 'winzhang', 'ks201907', '2019-07-09 13:11:58.796400', '2019-07-09 13:11:58.796400', '0');
INSERT INTO `user_user` VALUES ('10', '14500212d8194e3fbf645243459b7194', '张婷婷', 'zhangtingting', 'ks201907', '2019-07-10 08:34:27.349700', '2019-07-10 08:34:27.349700', '0');
