CREATE SCHEMA IF NOT EXISTS `sgpa` DEFAULT CHARACTER SET utf8 ;

USE `sgpa`;

DROP TABLE IF EXISTS `persona`;

CREATE TABLE IF NOT EXISTS `persona` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_tipo_identificacion` integer,
  `identificacion` varchar(255),
  `nombres` varchar(255) UNIQUE NOT NULL,
  `apellidos` text,
  `correo` varchar(255) UNIQUE NOT NULL,
  `telefono` integer,
  `direccion` varchar(255),
  `fecha_creacion` datetime
);

DROP TABLE IF EXISTS `tipo_identificacion`;

CREATE TABLE IF NOT EXISTS `tipo_identificacion` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descripcion` varchar(100) UNIQUE NOT NULL,
  `codigo` varchar(10) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `proyecto`;

CREATE TABLE IF NOT EXISTS  `proyecto` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `descripcion` text,
  `progreso` double,
  `id_estado` integer,
  `id_ecosistema` integer,
  `fecha_creacion` datetime,
  `fecha_inicio` timestamp,
  `fecha_finalizacion` timestamp
);

DROP TABLE IF EXISTS `usuario`;

CREATE TABLE IF NOT EXISTS  `usuario` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombreusuario` varchar(255) UNIQUE NOT NULL,
  `contrasena` varchar(255),
  `id_persona` integer,
  `id_estado_sistema` integer,
  `fecha_creacion` datetime,
  `fecha_actualizacion` timestamp
);

DROP TABLE IF EXISTS `rol_sistema`;

CREATE TABLE IF NOT EXISTS  `rol_sistema` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `usuario_rol_sistema`;

CREATE TABLE IF NOT EXISTS  `usuario_rol_sistema` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_usuario` integer,
  `id_rol_sistema` integer,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `tipo_permiso`;

CREATE TABLE IF NOT EXISTS  `tipo_permiso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `modulo`;

CREATE TABLE IF NOT EXISTS  `modulo` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `descripcion` text,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `permiso`;

CREATE TABLE IF NOT EXISTS  `permiso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descripcion` text,
  `id_modulo` integer,
  `id_tipo_permiso` integer,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `permiso_rol_sistema`;

CREATE TABLE IF NOT EXISTS  `permiso_rol_sistema` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_permiso` integer,
  `id_rol_sistema` integer,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `equipo`;

CREATE TABLE IF NOT EXISTS  `equipo` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `descripcion` text,
  `id_estado_sistema` varchar(255),
  `fecha_creacion` datetime
);

DROP TABLE IF EXISTS `persona_equipo`;

CREATE TABLE IF NOT EXISTS  `persona_equipo` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_persona` integer,
  `id_equipo` integer,
  `id_rol_equipo` integer,
  `id_estado_sistema` integer,
  `fecha_creacion` datetime,
  `fecha_actualizacion` timestamp
);

DROP TABLE IF EXISTS `rol_equipo`;

CREATE TABLE IF NOT EXISTS  `rol_equipo` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `id_estado_sistema` integer
);

DROP TABLE IF EXISTS `tarea`;

CREATE TABLE IF NOT EXISTS  `tarea` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text,
  `progreso` double,
  `id_proyecto` integer,
  `id_estado` integer,
  `id_prioridad` integer,
  `id_usuario_registra` integer,
  `id_persona_responsable` integer,
  `fecha_creacion` datetime NOT NULL,
  `fecha_inicio` timestamp,
  `fecha_finalizacion` timestamp
);

DROP TABLE IF EXISTS `prioridad`;

CREATE TABLE IF NOT EXISTS  `prioridad` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descripcion` VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `progreso`;

CREATE TABLE IF NOT EXISTS  `progreso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_tarea` integer,
  `descripcion` varchar(255),
  `fecha_progreso` datetime,
  `porcentaje` double,
  `fecha_creacion` timestamp
);

DROP TABLE IF EXISTS `estado`;

CREATE TABLE IF NOT EXISTS  `estado` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descripcion` varchar(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `estado_sistema`;

CREATE TABLE IF NOT EXISTS  `estado_sistema` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descripcion` varchar(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `ecosistema`;

CREATE TABLE IF NOT EXISTS  `ecosistema` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `descripcion` text,
  `ubicacion` varchar(255),
  `latitud` varchar(255),
  `longitud` varchar(255),
  `id_estado_sistema` varchar(255),
  `fecha_creacion` datetime
);

DROP TABLE IF EXISTS `recurso`;

CREATE TABLE IF NOT EXISTS  `recurso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL,
  `descripcion` text,
  `id_tipo_recurso` integer,
  `cantidad_disponible` double,
  `id_unidad_medida` integer,
  `fecha_creacion` datetime
);

DROP TABLE IF EXISTS `tipo_recurso`;

CREATE TABLE IF NOT EXISTS  `tipo_recurso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `unidad_medida`;

CREATE TABLE IF NOT EXISTS  `unidad_medida` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS `proyecto_recurso`;

CREATE TABLE IF NOT EXISTS  `proyecto_recurso` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_recurso` integer,
  `id_proyecto` integer,
  `cantidad_asignada` double NOT NULL,
  `cantidad_utilizada` double,
  `fecha_asignacion` datetime,
  `fecha_creacion` timestamp
);

DROP TABLE IF EXISTS `proyecto_equipo`;

CREATE TABLE IF NOT EXISTS  `proyecto_equipo` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `id_proyecto` integer,
  `id_equipo` integer,
  `fecha_asignacion` datetime
);
