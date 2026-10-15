
-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS pais
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- 2. Crear el usuario de aplicación
CREATE USER IF NOT EXISTS 'cesar'@'%'
IDENTIFIED BY '123';

-- 3. Asignar permisos sobre la base de datos
GRANT ALL PRIVILEGES ON pais.*
TO 'cesar'@'%';

Grants for cesar@%
GRANT USAGE ON *.* TO `cesar`@`%`
GRANT ALL PRIVILEGES ON `pais`.* TO `cesar`@`%`

-- 4. Aplicar los cambios
FLUSH PRIVILEGES;
