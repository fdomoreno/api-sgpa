USE sgpa;

-- Estados de Tareas y Proyectos.
INSERT INTO estado (descripcion) VALUES ('Planeado(a)');
INSERT INTO estado (descripcion) VALUES ('En progreso(a)');
INSERT INTO estado (descripcion) VALUES ('Completado(a)');
INSERT INTO estado (descripcion) VALUES ('Bloqueado(a)');
INSERT INTO estado (descripcion) VALUES ('Removido(a)');


-- Estados del sistema de usuarios, roles, permisos, modulos, etc.
INSERT INTO estado_sistema (descripcion) VALUES ('Activo');
INSERT INTO estado_sistema (descripcion) VALUES ('Inactivo');

-- Tipo de persmisos sobre los elementos de la aplicación.
INSERT INTO tipo_permiso (nombre) VALUES ('Consultar');
INSERT INTO tipo_permiso (nombre) VALUES ('Registrar');
INSERT INTO tipo_permiso (nombre) VALUES ('Actualizar');
INSERT INTO tipo_permiso (nombre) VALUES ('Eliminar');

-- Tipo de recursos que se pueden utilizar en los proyectos.
INSERT INTO tipo_recurso (nombre) VALUES ('Humano');
INSERT INTO tipo_recurso (nombre) VALUES ('Material');
INSERT INTO tipo_recurso (nombre) VALUES ('Financiero');
INSERT INTO tipo_recurso (nombre) VALUES ('Mueble');
INSERT INTO tipo_recurso (nombre) VALUES ('Inmueble');
INSERT INTO tipo_recurso (nombre) VALUES ('Tiempo');

-- Unidad de medida.
INSERT INTO unidad_medida (nombre) VALUES ('Personas');
INSERT INTO unidad_medida (nombre) VALUES ('Horas de trabajo');
INSERT INTO unidad_medida (nombre) VALUES ('Turno');
INSERT INTO unidad_medida (nombre) VALUES ('Toneladas');
INSERT INTO unidad_medida (nombre) VALUES ('Cajas');

-- Roles del equipo
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Lider de Proyecto',1);
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Biólogo(a)',1);
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Ingeniero(a) Agroforestal',1);
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Ingeniero(a) Ambiental',1);
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Zootecnistas',1);
INSERT INTO rol_equipo (nombre, id_estado_sistema) VALUES ('Coordinador(a)',1);

-- Roles del sistema
INSERT INTO rol_sistema (nombre, id_estado_sistema) VALUES ('Administrador',1);
INSERT INTO rol_sistema (nombre, id_estado_sistema) VALUES ('Usuario externo',1);
INSERT INTO rol_sistema (nombre, id_estado_sistema) VALUES ('Consulta Tareas',1);
INSERT INTO rol_sistema (nombre, id_estado_sistema) VALUES ('Supervisor del información',1);

-- Prioridad de las tareas
INSERT INTO prioridad (descripcion) VALUES ('Crítica');
INSERT INTO prioridad (descripcion) VALUES ('Alta');
INSERT INTO prioridad (descripcion) VALUES ('Media');
INSERT INTO prioridad (descripcion) VALUES ('Baja');
INSERT INTO prioridad (descripcion) VALUES ('Muy Baja');


-- Tipo Identificacion
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Cedula de ciudadanía', 'CC');
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Tarjeta de identidad', 'TI');
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Pasaporte', 'PA');
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Registro Civil', 'RC');
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Número Único de Identificación Personal', 'NUIP');
INSERT INTO tipo_identificacion (descripcion, codigo) VALUES ('Cedula de extranjería', 'CE');

-- Persona
INSERT INTO persona (id_tipo_identificacion, identificacion, nombres, apellidos, correo, telefono, direccion, fecha_creacion) 
VALUES (1,'123456789', 'Juan Daniel', 'Perez','luis.moreno.talentotech@usa.edu.co',12345678,'Cra 1 Nro.10', sysdate());

-- Usuario
INSERT INTO usuario (nombreusuario, contrasena, id_persona, id_estado_sistema, fecha_creacion, fecha_actualizacion) 
VALUES ('','',1,1,sysdate(),sysdate());

select * from usuario;

-- Rol

-- Permisos

-- Modulo

