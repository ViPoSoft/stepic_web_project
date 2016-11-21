#!/bin/bash ( иногда терминал отрабатывае ошибку на удаление 

if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/default
fi
# лишнее но пусть будет
if [ -f /etc/nginx/sites-enabled/default ]; then
  sudo rm /etc/nginx/sites-enabled/test.conf
fi

# symbolic link to nginx config
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo /etc/init.d/nginx restart

python manage.py runserver 0.0.0.0:8000
