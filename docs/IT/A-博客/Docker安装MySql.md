 2038  docker pull mysql:latest
 2041  docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=123456 -p 3308:3306 mysql:latest
 2044  mysql -u root -p -h 127.0.0.1 -P 3308