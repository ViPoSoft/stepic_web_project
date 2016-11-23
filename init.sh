sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE dbstep CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -uroot -e "CREATE USER 'vipo'@'localhost' IDENTIFIED BY 'vps23';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'vipo'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

#!/bin/bash ( иногда терминал отрабатывае ошибку на удаление 

if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/default
fi
# лишнее но пусть будет
#if [ -f /etc/nginx/sites-enabled/default ]; then
#  sudo rm /etc/nginx/sites-enabled/test.conf
#fi
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
# symbolic link to nginx config
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

# symbolic links to gunicorn configs
#sudo ln -sf /home/box/web/etc/gunicorn_hello.conf /etc/gunicorn.d/test
#sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask
sudo ln -s /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

python /home/box/web/ask/manage.py syncdb
