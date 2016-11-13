
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s  /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunic_dj.conf   /etc/gunicorn.d/test_dj
#1.9 Запуск WSGI приложений
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py

sudo /etc/init.d/gunicorn restart
