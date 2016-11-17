
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

# symbolic links to gunicorn configs
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf /etc/gunicorn.d/ask

sudo /etc/init.d/gunicorn restart
