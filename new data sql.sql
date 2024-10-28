/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 10.4.32-MariaDB : Database - wood_craft_db1
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`wood_craft_db1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `wood_craft_db1`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add category',7,'add_category'),
(26,'Can change category',7,'change_category'),
(27,'Can delete category',7,'delete_category'),
(28,'Can view category',7,'view_category'),
(29,'Can add customer',8,'add_customer'),
(30,'Can change customer',8,'change_customer'),
(31,'Can delete customer',8,'delete_customer'),
(32,'Can view customer',8,'view_customer'),
(33,'Can add customized_order',9,'add_customized_order'),
(34,'Can change customized_order',9,'change_customized_order'),
(35,'Can delete customized_order',9,'delete_customized_order'),
(36,'Can view customized_order',9,'view_customized_order'),
(37,'Can add design',10,'add_design'),
(38,'Can change design',10,'change_design'),
(39,'Can delete design',10,'delete_design'),
(40,'Can view design',10,'view_design'),
(41,'Can add login',11,'add_login'),
(42,'Can change login',11,'change_login'),
(43,'Can delete login',11,'delete_login'),
(44,'Can view login',11,'view_login'),
(45,'Can add order',12,'add_order'),
(46,'Can change order',12,'change_order'),
(47,'Can delete order',12,'delete_order'),
(48,'Can view order',12,'view_order'),
(49,'Can add product',13,'add_product'),
(50,'Can change product',13,'change_product'),
(51,'Can delete product',13,'delete_product'),
(52,'Can view product',13,'view_product'),
(53,'Can add wood',14,'add_wood'),
(54,'Can change wood',14,'change_wood'),
(55,'Can delete wood',14,'delete_wood'),
(56,'Can view wood',14,'view_wood'),
(57,'Can add shapes',15,'add_shapes'),
(58,'Can change shapes',15,'change_shapes'),
(59,'Can delete shapes',15,'delete_shapes'),
(60,'Can view shapes',15,'view_shapes'),
(61,'Can add review_and_rating',16,'add_review_and_rating'),
(62,'Can change review_and_rating',16,'change_review_and_rating'),
(63,'Can delete review_and_rating',16,'delete_review_and_rating'),
(64,'Can view review_and_rating',16,'view_review_and_rating'),
(65,'Can add post',17,'add_post'),
(66,'Can change post',17,'change_post'),
(67,'Can delete post',17,'delete_post'),
(68,'Can view post',17,'view_post'),
(69,'Can add payment',18,'add_payment'),
(70,'Can change payment',18,'change_payment'),
(71,'Can delete payment',18,'delete_payment'),
(72,'Can view payment',18,'view_payment'),
(73,'Can add diamension',19,'add_diamension'),
(74,'Can change diamension',19,'change_diamension'),
(75,'Can delete diamension',19,'delete_diamension'),
(76,'Can view diamension',19,'view_diamension'),
(77,'Can add customized_payment',20,'add_customized_payment'),
(78,'Can change customized_payment',20,'change_customized_payment'),
(79,'Can delete customized_payment',20,'delete_customized_payment'),
(80,'Can view customized_payment',20,'view_customized_payment');

/*Table structure for table `auth_user` */

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','category'),
(8,'myapp','customer'),
(9,'myapp','customized_order'),
(20,'myapp','customized_payment'),
(10,'myapp','design'),
(19,'myapp','diamension'),
(11,'myapp','login'),
(12,'myapp','order'),
(18,'myapp','payment'),
(17,'myapp','post'),
(13,'myapp','product'),
(16,'myapp','review_and_rating'),
(15,'myapp','shapes'),
(14,'myapp','wood'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-10-25 06:33:56.277287'),
(2,'auth','0001_initial','2024-10-25 06:33:56.433537'),
(3,'admin','0001_initial','2024-10-25 06:33:57.044753'),
(4,'admin','0002_logentry_remove_auto_add','2024-10-25 06:33:57.185493'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-10-25 06:33:57.201088'),
(6,'contenttypes','0002_remove_content_type_name','2024-10-25 06:33:57.295936'),
(7,'auth','0002_alter_permission_name_max_length','2024-10-25 06:33:57.358900'),
(8,'auth','0003_alter_user_email_max_length','2024-10-25 06:33:57.390151'),
(9,'auth','0004_alter_user_username_opts','2024-10-25 06:33:57.390151'),
(10,'auth','0005_alter_user_last_login_null','2024-10-25 06:33:57.437028'),
(11,'auth','0006_require_contenttypes_0002','2024-10-25 06:33:57.452650'),
(12,'auth','0007_alter_validators_add_error_messages','2024-10-25 06:33:57.452650'),
(13,'auth','0008_alter_user_username_max_length','2024-10-25 06:33:57.468343'),
(14,'auth','0009_alter_user_last_name_max_length','2024-10-25 06:33:57.483933'),
(15,'auth','0010_alter_group_name_max_length','2024-10-25 06:33:57.505330'),
(16,'auth','0011_update_proxy_permissions','2024-10-25 06:33:57.515366'),
(17,'myapp','0001_initial','2024-10-25 06:33:58.188213'),
(18,'sessions','0001_initial','2024-10-25 06:33:59.097627'),
(19,'myapp','0002_auto_20241025_1448','2024-10-25 09:19:10.315326'),
(20,'myapp','0003_remove_design_wood_name','2024-10-27 09:15:57.733229');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('ii2p5lkomom0621mwarxy72wbmvq1sfu','ZWM4N2UzNTdlZmU5ZTBiMGZjN2U4NzVjNjIxYWIxYWEwODk5NDA3MDp7ImxpZCI6Mn0=','2024-11-08 07:13:20.474823'),
('rj19tp00wfykfv6vsl9q3153pwqke9cb','ZWM4N2UzNTdlZmU5ZTBiMGZjN2U4NzVjNjIxYWIxYWEwODk5NDA3MDp7ImxpZCI6Mn0=','2024-11-10 09:59:04.978331'),
('t8rf4vi0z01kb9we6geun3vxfc1ll58u','YjA5ZDVhMzlkMzgwNTMzZTc4ZDU3MGE1ZDJlY2EyMDg3NGM4MGViNjp7ImxpZCI6M30=','2024-11-11 07:27:01.927045');

/*Table structure for table `myapp_category` */

DROP TABLE IF EXISTS `myapp_category`;

CREATE TABLE `myapp_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `photo` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_category` */

insert  into `myapp_category`(`id`,`category_name`,`photo`) values 
(6,'table','/media/20241028-115525.jpg'),
(7,'table','/media/20241028-115457.jpg'),
(8,'sofa','/media/20241028-121103.jpg'),
(9,'sofa','/media/20241028-122048.jpg');

/*Table structure for table `myapp_customer` */

DROP TABLE IF EXISTS `myapp_customer`;

CREATE TABLE `myapp_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobilenumber` bigint(20) NOT NULL,
  `place` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_customer_LOGIN_id_23d9edf9_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_customer_LOGIN_id_23d9edf9_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_customer` */

insert  into `myapp_customer`(`id`,`customer_name`,`email`,`mobilenumber`,`place`,`district`,`post`,`pin`,`LOGIN_id`) values 
(1,'nafiya/','nafiya@gmail.com',9745678960,'KOLLAM/','THIRUVANANTHAPURAM','rec  nit',673601,2),
(2,'anagha k','anagha@gmail.com',9048849862,'katttangal','KASARAGOD','rec',673602,3);

/*Table structure for table `myapp_customized_order` */

DROP TABLE IF EXISTS `myapp_customized_order`;

CREATE TABLE `myapp_customized_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `CUSTOMER_id` int(11) NOT NULL,
  `DIMENSION_id` int(11) NOT NULL,
  `PRODUCT_id` int(11) NOT NULL,
  `WOOD_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_customized_ord_DIMENSION_id_f7cd0b2a_fk_myapp_dia` (`DIMENSION_id`),
  KEY `myapp_customized_order_PRODUCT_id_7235548f_fk_myapp_product_id` (`PRODUCT_id`),
  KEY `myapp_customized_order_WOOD_id_81ebef25_fk_myapp_wood_id` (`WOOD_id`),
  KEY `myapp_customized_order_CUSTOMER_id_708463cf_fk_myapp_customer_id` (`CUSTOMER_id`),
  CONSTRAINT `myapp_customized_ord_DIMENSION_id_f7cd0b2a_fk_myapp_dia` FOREIGN KEY (`DIMENSION_id`) REFERENCES `myapp_diamension` (`id`),
  CONSTRAINT `myapp_customized_order_CUSTOMER_id_708463cf_fk_myapp_customer_id` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `myapp_customer` (`id`),
  CONSTRAINT `myapp_customized_order_PRODUCT_id_7235548f_fk_myapp_product_id` FOREIGN KEY (`PRODUCT_id`) REFERENCES `myapp_product` (`id`),
  CONSTRAINT `myapp_customized_order_WOOD_id_81ebef25_fk_myapp_wood_id` FOREIGN KEY (`WOOD_id`) REFERENCES `myapp_wood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_customized_order` */

insert  into `myapp_customized_order`(`id`,`date`,`status`,`CUSTOMER_id`,`DIMENSION_id`,`PRODUCT_id`,`WOOD_id`) values 
(8,'2024-10-28','verified',2,5,8,8);

/*Table structure for table `myapp_customized_payment` */

DROP TABLE IF EXISTS `myapp_customized_payment`;

CREATE TABLE `myapp_customized_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `CUSTOMIZED_ORDER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_customized_pay_CUSTOMIZED_ORDER_id_8bad7ad4_fk_myapp_cus` (`CUSTOMIZED_ORDER_id`),
  CONSTRAINT `myapp_customized_pay_CUSTOMIZED_ORDER_id_8bad7ad4_fk_myapp_cus` FOREIGN KEY (`CUSTOMIZED_ORDER_id`) REFERENCES `myapp_customized_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_customized_payment` */

insert  into `myapp_customized_payment`(`id`,`price`,`date`,`status`,`CUSTOMIZED_ORDER_id`) values 
(6,244000,'2024-10-28','paid',8);

/*Table structure for table `myapp_design` */

DROP TABLE IF EXISTS `myapp_design`;

CREATE TABLE `myapp_design` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` bigint(20) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `photo` varchar(300) NOT NULL,
  `design_name` varchar(100) NOT NULL,
  `WOOD_id` int(11) NOT NULL,
  `shape` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_design_WOOD_id_15f21ab4_fk_myapp_wood_id` (`WOOD_id`),
  CONSTRAINT `myapp_design_WOOD_id_15f21ab4_fk_myapp_wood_id` FOREIGN KEY (`WOOD_id`) REFERENCES `myapp_wood` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_design` */

insert  into `myapp_design`(`id`,`price`,`description`,`photo`,`design_name`,`WOOD_id`,`shape`) values 
(24,34349,'height=\"50px\"width=\"500px\"','/media/20241028-122150.jpg','Sleepyhead ',8,'RECTANLE');

/*Table structure for table `myapp_diamension` */

DROP TABLE IF EXISTS `myapp_diamension`;

CREATE TABLE `myapp_diamension` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `height` bigint(20) NOT NULL,
  `width` bigint(20) NOT NULL,
  `total_wood_needed` bigint(20) NOT NULL,
  `SHAPES_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_diamension_SHAPES_id_0c540b39_fk_myapp_shapes_id` (`SHAPES_id`),
  CONSTRAINT `myapp_diamension_SHAPES_id_0c540b39_fk_myapp_shapes_id` FOREIGN KEY (`SHAPES_id`) REFERENCES `myapp_shapes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_diamension` */

insert  into `myapp_diamension`(`id`,`height`,`width`,`total_wood_needed`,`SHAPES_id`) values 
(4,23,27,60,5),
(5,89,191,800,5),
(6,89,191,800,5);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin@gmail.com','Admin@12','admin'),
(2,'nafiya@gmail.com','nafi@32X','user'),
(3,'anagha@gmail.com','Anagha@1','user');

/*Table structure for table `myapp_order` */

DROP TABLE IF EXISTS `myapp_order`;

CREATE TABLE `myapp_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `totalamount` varchar(100) NOT NULL,
  `quantity` bigint(20) NOT NULL,
  `CUSTOMER_ID_id` int(11) NOT NULL,
  `DESIGN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_order_CUSTOMER_ID_id_d7865783_fk_myapp_customer_id` (`CUSTOMER_ID_id`),
  KEY `myapp_order_DESIGN_id_a64bc79a_fk_myapp_design_id` (`DESIGN_id`),
  CONSTRAINT `myapp_order_CUSTOMER_ID_id_d7865783_fk_myapp_customer_id` FOREIGN KEY (`CUSTOMER_ID_id`) REFERENCES `myapp_customer` (`id`),
  CONSTRAINT `myapp_order_DESIGN_id_a64bc79a_fk_myapp_design_id` FOREIGN KEY (`DESIGN_id`) REFERENCES `myapp_design` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_order` */

insert  into `myapp_order`(`id`,`date`,`status`,`totalamount`,`quantity`,`CUSTOMER_ID_id`,`DESIGN_id`) values 
(9,'2024-10-28','paid','10304700.0',3,2,24);

/*Table structure for table `myapp_payment` */

DROP TABLE IF EXISTS `myapp_payment`;

CREATE TABLE `myapp_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `CUSTOMER_ID_id` int(11) NOT NULL,
  `ORDER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_CUSTOMER_ID_id_fdd190ef_fk_myapp_customer_id` (`CUSTOMER_ID_id`),
  KEY `myapp_payment_ORDER_id_90f79814_fk_myapp_order_id` (`ORDER_id`),
  CONSTRAINT `myapp_payment_CUSTOMER_ID_id_fdd190ef_fk_myapp_customer_id` FOREIGN KEY (`CUSTOMER_ID_id`) REFERENCES `myapp_customer` (`id`),
  CONSTRAINT `myapp_payment_ORDER_id_90f79814_fk_myapp_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `myapp_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_payment` */

insert  into `myapp_payment`(`id`,`price`,`date`,`status`,`CUSTOMER_ID_id`,`ORDER_id`) values 
(11,10304700,'2024-10-28','paid',2,9);

/*Table structure for table `myapp_post` */

DROP TABLE IF EXISTS `myapp_post`;

CREATE TABLE `myapp_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_name` varchar(100) NOT NULL,
  `photo_1` varchar(100) NOT NULL,
  `photo_2` varchar(100) NOT NULL,
  `photo_3` varchar(100) NOT NULL,
  `description_1` varchar(10000) NOT NULL,
  `description_2` blob NOT NULL,
  `description_3` blob NOT NULL,
  `DESIGN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_post_DESIGN_id_7199ebe2_fk_myapp_design_id` (`DESIGN_id`),
  CONSTRAINT `myapp_post_DESIGN_id_7199ebe2_fk_myapp_design_id` FOREIGN KEY (`DESIGN_id`) REFERENCES `myapp_design` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_post` */

insert  into `myapp_post`(`id`,`post_name`,`photo_1`,`photo_2`,`photo_3`,`description_1`,`description_2`,`description_3`,`DESIGN_id`) values 
(5,'sofa','/media/20241028-1224571.jpg','/media/20241028-1224572.jpg','/media/20241028-1224573.jpg','color=blue','color=red','color=yellow',24);

/*Table structure for table `myapp_product` */

DROP TABLE IF EXISTS `myapp_product`;

CREATE TABLE `myapp_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `material` varchar(100) NOT NULL,
  `description` blob NOT NULL,
  `price` bigint(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `Quantity` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_product` */

insert  into `myapp_product`(`id`,`product_name`,`material`,`description`,`price`,`photo`,`Quantity`) values 
(1,'table','table','color=blue',240200,'/media/20241025131229.jpg','3'),
(2,'table','table','color=blue',80060,'/media/20241025135344.jpg','1'),
(3,'kjjl','kjjl','pojp',80000,'C:\\Users\\nafiy\\PycharmProjects\\woodcraft\\media\\241025-164823','1'),
(4,'kjjl','kjjl','pojp',80000,'C:\\Users\\nafiy\\PycharmProjects\\woodcraft\\media\\241025-164926','1'),
(5,'table','table','red color ',80200,'/media/20241025-170010.jpg','1'),
(6,'table','table','color=browm\r\nyyy',1350,'/media/20241026-130004.jpg','2'),
(7,'table','table','color=blue',160000,'/media/20241027120150.jpg','2'),
(8,'SOFA','SOFA','b\'COLOR=WHITE\'',2440,'/media/20241028-125444.jpg','4');

/*Table structure for table `myapp_review_and_rating` */

DROP TABLE IF EXISTS `myapp_review_and_rating`;

CREATE TABLE `myapp_review_and_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `CUSTOMER_id` int(11) NOT NULL,
  `DESIGN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_review_and_rat_CUSTOMER_id_1e7267de_fk_myapp_cus` (`CUSTOMER_id`),
  KEY `myapp_review_and_rating_DESIGN_id_b4841e22_fk_myapp_design_id` (`DESIGN_id`),
  CONSTRAINT `myapp_review_and_rat_CUSTOMER_id_1e7267de_fk_myapp_cus` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `myapp_customer` (`id`),
  CONSTRAINT `myapp_review_and_rating_DESIGN_id_b4841e22_fk_myapp_design_id` FOREIGN KEY (`DESIGN_id`) REFERENCES `myapp_design` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_review_and_rating` */

insert  into `myapp_review_and_rating`(`id`,`rating`,`review`,`date`,`CUSTOMER_id`,`DESIGN_id`) values 
(2,'5','good quality','2024-10-28',2,24);

/*Table structure for table `myapp_shapes` */

DROP TABLE IF EXISTS `myapp_shapes`;

CREATE TABLE `myapp_shapes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shape` varchar(100) NOT NULL,
  `CATEGORY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_shapes_CATEGORY_id_a3d612e1_fk_myapp_category_id` (`CATEGORY_id`),
  CONSTRAINT `myapp_shapes_CATEGORY_id_a3d612e1_fk_myapp_category_id` FOREIGN KEY (`CATEGORY_id`) REFERENCES `myapp_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_shapes` */

insert  into `myapp_shapes`(`id`,`shape`,`CATEGORY_id`) values 
(5,'RECTANLE',6),
(6,'RECTANLE',8),
(7,'RECTANLE',8);

/*Table structure for table `myapp_wood` */

DROP TABLE IF EXISTS `myapp_wood`;

CREATE TABLE `myapp_wood` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wood_name` varchar(100) NOT NULL,
  `sqft_charge` bigint(20) NOT NULL,
  `CATEGORY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_wood_CATEGORY_id_c02eab0d_fk_myapp_category_id` (`CATEGORY_id`),
  CONSTRAINT `myapp_wood_CATEGORY_id_c02eab0d_fk_myapp_category_id` FOREIGN KEY (`CATEGORY_id`) REFERENCES `myapp_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `myapp_wood` */

insert  into `myapp_wood`(`id`,`wood_name`,`sqft_charge`,`CATEGORY_id`) values 
(5,'TEAK',9,6),
(6,'ACASIA',650,6),
(7,'ACASIA',600,6),
(8,'MAHOGAANY',600,8);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
