-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-07-2023 a las 02:14:16
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `asistencia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia`
--

CREATE TABLE `asistencia` (
  `id_asi` int(11) NOT NULL COMMENT 'Clave primaria  de la asistencia',
  `id_emp` int(11) DEFAULT NULL COMMENT 'Codigo del empleado',
  `id_dep` int(11) DEFAULT NULL COMMENT 'Codigo del departamento',
  `fec_asi` date NOT NULL COMMENT 'fecha de la asistencia del empelado',
  `horLle_asi` time NOT NULL COMMENT 'Hora de llegada del empleado',
  `horSal_asi` time NOT NULL COMMENT 'Hora de salida del empleado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `asistencia`
--

INSERT INTO `asistencia` (`id_asi`, `id_emp`, `id_dep`, `fec_asi`, `horLle_asi`, `horSal_asi`) VALUES
(1, 9, NULL, '2023-07-25', '21:40:43', '21:13:18'),
(2, 1, NULL, '2023-07-25', '22:30:44', '00:00:00'),
(3, 2, NULL, '2023-07-25', '22:30:48', '00:00:00'),
(4, 10, NULL, '2023-07-25', '22:45:39', '21:18:23'),
(5, 6, NULL, '2023-07-26', '22:43:45', '00:00:00'),
(6, 6, NULL, '2023-07-26', '22:44:17', '21:13:06'),
(7, 11, NULL, '2023-07-26', '23:20:31', '12:34:38'),
(8, 1, NULL, '2023-07-26', '23:21:57', '08:30:55'),
(9, 6, NULL, '2023-07-26', '23:29:28', '22:15:15'),
(10, 2, NULL, '2023-07-26', '23:29:30', '21:22:29'),
(11, 3, NULL, '2023-07-26', '23:42:29', '00:00:00'),
(12, 12, NULL, '2023-07-27', '00:34:25', '00:00:00'),
(13, 16, NULL, '2023-07-27', '10:35:57', '00:00:00'),
(14, 17, NULL, '2023-07-27', '10:36:39', '00:00:00'),
(15, 1, NULL, '2023-07-27', '10:46:04', '00:00:00'),
(16, 18, NULL, '2023-07-27', '10:59:28', '00:00:00'),
(17, 14, NULL, '2023-07-27', '11:01:02', '12:00:53'),
(18, 12, NULL, '2023-07-27', '11:05:19', '00:00:00'),
(19, 19, NULL, '2023-07-27', '21:19:53', '21:20:35'),
(20, 1, NULL, '2023-07-28', '08:31:39', '08:35:38'),
(21, 22, NULL, '2023-07-28', '09:50:22', '09:50:29'),
(22, 23, NULL, '2023-07-28', '10:44:09', '10:44:36'),
(23, 14, NULL, '2023-07-28', '14:20:06', '00:00:00'),
(24, 20, NULL, '2023-07-28', '14:57:25', '14:57:37'),
(25, 22, NULL, '2023-07-28', '14:57:27', '14:57:39'),
(26, 2, NULL, '2023-07-28', '15:00:23', '00:00:00'),
(27, 25, NULL, '2023-07-28', '15:43:40', '15:43:45'),
(28, 1, NULL, '2023-07-28', '20:13:19', '20:13:27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `id_car` int(11) NOT NULL COMMENT 'Clave Primaria del Cargo',
  `nom_car` varchar(70) NOT NULL COMMENT 'Nombre del Cargo',
  `est_car` char(1) NOT NULL COMMENT 'Estatus del Cargo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_dep` int(11) NOT NULL COMMENT 'Clave primaria del departamento ',
  `nom_dep` varchar(40) NOT NULL COMMENT 'Nombre del departamento',
  `est_dep` char(1) NOT NULL COMMENT 'Estatus del departamento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id_emp` int(11) NOT NULL COMMENT 'Clave primaria del empleado',
  `nom_emp` varchar(30) NOT NULL COMMENT 'Nombre del empleado',
  `ape_emp` varchar(50) NOT NULL COMMENT 'Apellido del empleado',
  `fec_emp_nac` date NOT NULL COMMENT 'Fecha de nacimiento del empleado',
  `gen_emp` char(10) NOT NULL COMMENT 'Genero del empleado',
  `dir_emp` varchar(255) NOT NULL COMMENT 'Direccion del empleado',
  `est_emp` char(1) NOT NULL COMMENT 'Estatus del empleado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id_emp`, `nom_emp`, `ape_emp`, `fec_emp_nac`, `gen_emp`, `dir_emp`, `est_emp`) VALUES
(1, 'Joseir', 'Colmenares', '1999-04-06', 'Masculino', 'San Cristobal', 'A'),
(2, 'Angel', 'Alvino', '2005-05-12', 'Masculino', 'San Cristobal', 'A'),
(3, 'Alejandro', 'Ballout', '2003-02-12', '', 'San Cristobal', 'A'),
(5, 'Maria', 'Perez', '1990-07-18', 'Femenino', 'San Cristobal', 'A'),
(6, 'Jose Matias', 'Colmenares', '2000-02-12', 'Masculino', 'Capacho', 'I'),
(9, 'Paola', 'Belandria', '1999-08-12', 'Femenino', 'San Cristobal', 'A'),
(10, 'Paola', 'Contreras', '2002-12-30', 'Femenino', '19 Abril', 'I'),
(11, 'Ana', 'Rodriguez', '2000-12-04', 'Masculino', 'Tucape', 'I'),
(12, 'Marta', 'Matos', '1980-04-25', 'Femenino', 'Colinas', 'I'),
(14, 'Lionel Andres', 'Messi Cuccittini', '1987-06-24', 'Masculino', 'Miami', 'A'),
(16, 'Michael', 'Diaz', '1900-12-10', 'Masculino', 'Caracas', 'I'),
(17, 'Alonso', 'Corleone', '2000-10-10', 'Masculino', 'España', 'A'),
(18, 'Ronaldo', 'Nazario', '1980-12-02', 'Masculino', 'Brasilia', 'A'),
(19, 'Elon', 'Musk', '1999-09-08', 'Masculino', 'USA', 'A'),
(20, 'Gabriela', 'Moncada', '1998-05-10', 'Femenino', 'Barrio Obrero', 'A'),
(22, 'Ronaldinho', 'Gaucho', '1980-12-10', 'Masculino', 'Brasilia', 'A'),
(23, 'Rodrigo', 'Moncada', '1990-10-10', 'Masculino', 'IUTEPAL', 'A'),
(25, 'Ingenieria', 'Digital', '2011-10-09', 'Masculino', 'Barrio Obrero', 'A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nomina`
--

CREATE TABLE `nomina` (
  `id_nom` int(11) NOT NULL COMMENT 'Clave primaria de la nomina',
  `id_emp` int(11) DEFAULT NULL COMMENT 'codigo del empleado',
  `fecha_inicio` date DEFAULT NULL COMMENT 'Fecha de inicio en la cuals se pago la nomina',
  `fecha_fin` date DEFAULT NULL COMMENT 'Fecha de Fin de la nomina',
  `est_nom` char(1) NOT NULL COMMENT 'Estatus de la Nonima'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permiso`
--

CREATE TABLE `permiso` (
  `id_per` int(11) NOT NULL COMMENT 'Clave primaria de permiso',
  `nom_per` varchar(30) NOT NULL COMMENT 'Nombre del Permiso',
  `est_per` char(1) NOT NULL COMMENT 'Estatus del Permiso'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol` int(11) NOT NULL COMMENT 'Clave primaria del Rol',
  `nom_rol` varchar(20) NOT NULL COMMENT 'Nombre del rol',
  `est_rol` char(1) NOT NULL COMMENT 'Estatus del Rol'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id_rol`, `nom_rol`, `est_rol`) VALUES
(1, 'Administrador', 'A'),
(2, 'Empleado', 'A'),
(3, 'Observador', 'A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rolpermiso`
--

CREATE TABLE `rolpermiso` (
  `id_rol` int(11) NOT NULL COMMENT 'Clave primaria del rolPermiso',
  `id_per` int(11) NOT NULL COMMENT 'Codigo del Permiso',
  `est_rol_per` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sueldos`
--

CREATE TABLE `sueldos` (
  `id_sueldo` int(11) NOT NULL COMMENT 'Clave primaria de sueldos',
  `monto` decimal(10,2) NOT NULL COMMENT 'Montos del sueldo',
  `est_sue` char(1) NOT NULL COMMENT 'Estatus del Sueldo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usu` int(11) NOT NULL COMMENT 'Clave Primaria del usuario',
  `id_emp` int(11) DEFAULT NULL COMMENT 'Codigo del empleado',
  `nom_usu` varchar(100) NOT NULL COMMENT 'Nombre de usuario del empleado',
  `con_usu` varchar(255) NOT NULL COMMENT 'Contraseña del empleado',
  `id_rol` int(11) DEFAULT NULL COMMENT 'Codigo del rol',
  `est_usu` char(1) NOT NULL COMMENT 'Estatus del usuario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usu`, `id_emp`, `nom_usu`, `con_usu`, `id_rol`, `est_usu`) VALUES
(1, 1, 'Joseir', '1234', 1, 'A'),
(2, 3, 'Ballout', '123', 1, 'A'),
(3, 2, 'Angel', '123', 1, 'A'),
(4, 20, 'Gabriela', 'g15360545', 1, 'A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id_asi`),
  ADD KEY `id_emp` (`id_emp`),
  ADD KEY `id_dep` (`id_dep`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id_car`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_dep`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_emp`);

--
-- Indices de la tabla `nomina`
--
ALTER TABLE `nomina`
  ADD PRIMARY KEY (`id_nom`),
  ADD KEY `id_emp` (`id_emp`);

--
-- Indices de la tabla `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id_per`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rolpermiso`
--
ALTER TABLE `rolpermiso`
  ADD PRIMARY KEY (`id_rol`,`id_per`),
  ADD KEY `id_per` (`id_per`);

--
-- Indices de la tabla `sueldos`
--
ALTER TABLE `sueldos`
  ADD PRIMARY KEY (`id_sueldo`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usu`),
  ADD KEY `id_emp` (`id_emp`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id_asi` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria  de la asistencia', AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id_car` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave Primaria del Cargo';

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_dep` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria del departamento ';

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_emp` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria del empleado', AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id_per` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria de permiso';

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria del Rol', AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `sueldos`
--
ALTER TABLE `sueldos`
  MODIFY `id_sueldo` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave primaria de sueldos';

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usu` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Clave Primaria del usuario', AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD CONSTRAINT `asistencia_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `empleado` (`id_emp`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencia_ibfk_2` FOREIGN KEY (`id_dep`) REFERENCES `departamento` (`id_dep`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `nomina`
--
ALTER TABLE `nomina`
  ADD CONSTRAINT `nomina_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `empleado` (`id_emp`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `rolpermiso`
--
ALTER TABLE `rolpermiso`
  ADD CONSTRAINT `rolpermiso_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`) ON UPDATE CASCADE,
  ADD CONSTRAINT `rolpermiso_ibfk_2` FOREIGN KEY (`id_per`) REFERENCES `permiso` (`id_per`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `empleado` (`id_emp`) ON UPDATE CASCADE,
  ADD CONSTRAINT `usuario_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
