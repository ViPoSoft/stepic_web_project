
#sudo rm /etc/nginx/sites-enabled/test.conf
# symbolic link to nginx config
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo rm /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

# symbolic links to gunicorn configs
sudo ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django-gunicorn.conf /etc/gunicorn.d/django-gunicorn.conf

sudo unlink /etc/gunicorn.d/django
sudo ln -s /home/box/web/etc/django /etc/gunicorn.d/django

# run gunicorn server
sudo gunicorn -u nobody /etc/gunicorn.d/hello.py hello:app
sudo gunicorn -u nobody /etc/gunicorn.d/django-gunicorn.conf ask.wsgi:application

sudo /etc/init.d/gunicorn restart
