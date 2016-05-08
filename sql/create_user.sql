DROP USER 'rasse';
CREATE USER 'rasse'@'%' IDENTIFIED BY 'mysql';
GRANT ALL PRIVILEGES ON rasse.* TO 'rasse'@'localhost';
GRANT ALL PRIVILEGES ON rasse.* TO 'rasse'@'%';
FLUSH PRIVILEGES;
