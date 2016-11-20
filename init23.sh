sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE base23;"
mysql -uroot -e "CREATE USER 'vipo@localhost' IDENTIFIED BY 'vps23';"
mysql -uroot -e "GRANT ALL ON base23.* TO 'vipo@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
