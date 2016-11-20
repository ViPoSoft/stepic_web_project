sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE `step_base` CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -uroot -e "CREATE USER 'vipo'@'localhost' IDENTIFIED BY 'vps23';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'vipo'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

python /home/box/web/ask/manage.py syncdb
