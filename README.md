# Pamboliada
Projecte Final FCT - CFGS Desenvolupament d'Aplicacions Web

L'aplicació per a ordinador (Linux Debian or Ubuntu 18.04+) i per a mòbil (Android4.0+) està disponible per descarregar.
També hi ha una versió (en proves) per a altres distribucions Linux (en format .zip).


<a href="https://github.com/antonialoytorrens/pa-amb-oli/releases/download/v0.1/pamboliada-webapp_1.0_all.deb"><img src="https://github.com/antonialoytorrens/pa-amb-oli/blob/master/doc/showapps/get-deb-from-github.png" alt="Get it on Github DEB"></a>
<a href="https://github.com/antonialoytorrens/pa-amb-oli/releases/download/v0.1/pamboliada-embedded-1.0.zip"><img src="https://github.com/antonialoytorrens/pa-amb-oli/blob/master/doc/showapps/get-zip-from-github.png" alt="Get it on Github ZIP"></a>
<a href="https://github.com/antonialoytorrens/pa-amb-oli/releases/download/v0.1/pamboliada-signed-1.0.apk"><img src="https://github.com/antonialoytorrens/pa-amb-oli/blob/master/doc/showapps/get-apk-from-github.png" alt="Get it on Github APK"></a>

# Guia ràpida per començar

## Si es vol visitar el lloc web

El lloc web es troba a http://www.pamboliada.cat.

## Si es vol realitzar el desplegament (desenvolupament)

### Linux

Obre un terminal i introdueix les següents ordres:

```sh
$ sudo apt install python3 python3-venv python3-pip postgresql

$ sudo su - postgres
$ psql
# CREATE DATABASE paambolis;
# CREATE USER paambolis with PASSWORD 'paambolis';
# ALTER ROLE paambolis SET client_encoding TO 'utf-8';
# ALTER ROLE paambolis SET default_transaction_isolation TO 'read committed';
# ALTER ROLE paambolis SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE paambolis TO paambolis;
# \q
$ exit

$ git clone https://github.com/antonialoytorrens/pa-amb-oli.git
$ cd pa-amb-oli/
$ virtualenv --python=`which python3` venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
L'aplicació es desplega per defecte a:
```sh
127.0.0.1:8000
```
**Nota: Si l'aplicació es vol fer disponible a tots els dispositius de la xarxa local, canvia la darrera ordre per aquesta:**

```sh
$ python manage.py runserver 0.0.0.0:8000
```

Així, l'aplicació és accessible tant per a localhost (127.0.0.1) com per altres dispositius (introduir la IP de la màquina virtual amb el port 8000, ex: 192.168.1.23:8000).

La IP del teu ordinador es pot saber obrint un terminal i introduir la ordre `ifconfig` (si no es troba la ordre, executa `sudo apt install net-tools`)


### Altres (per Linux també serveix com a alternativa)

Baixar i instal·lar el programa VirtualBox corresponent al teu sistema operatiu: https://www.virtualbox.org

------

L'arxiu (*Client*) es troba a la següent ubicació:

https://drive.google.com/file/d/1MkoVXHopQ6FtzdlYJxg-n4mdoLTj9B2h/view

Per tant, descarregar i importar l'arxiu (.ova) del Client.

------

L'arxiu (*Servidor*) es troba a la següent ubicació:

https://drive.google.com/file/d/1FpVQ828GVtFjJj6fh9hmUDsa4oONp_uI/view

Per tant, descarregar i importar l'arxiu (.ova) del Servidor.

------

#### Client Ubuntu 18.04.3 LTS (LXDE)

El servidor està configurat a partir d'una IP estàtica (192.168.1.201).
L'arxiu de configuració per canviar la IP es troba a **/etc/netplan/01-netcfg.yaml**.
L'aplicació es desplega automàticament a tota la xarxa local quan s'inicia el sistema, per tant per veure la pàgina web s'ha d'obrir un navegador a la direcció 192.168.1.201:8000, o en el propi sistema (firefox) a localhost:8000.

##### Informació bàsica
```sh
LOGIN
User: admin
Password: admin0
------------------------------------------------
POSTGRES
*Usuari amb tots els privilegis a la base de dades `paambolis`*
User: paambolis
Password: paambolis
------------------------------------------------
```

## Si es vol realitzar el desplegament (producció)

Es recomana visitar aquest enllaç per a una explicació més detallada del que es veurà a continuació: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04.

```sh
$ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl gunicorn

$ sudo su - postgres
$ psql
# CREATE DATABASE paambolis;
# CREATE USER paambolis with PASSWORD 'paambolis';
# ALTER ROLE paambolis SET client_encoding TO 'utf-8';
# ALTER ROLE paambolis SET default_transaction_isolation TO 'read committed';
# ALTER ROLE paambolis SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE paambolis TO paambolis;
# \q
$ exit

$ git clone https://github.com/antonialoytorrens/pa-amb-oli.git
$ cd pa-amb-oli/
$ virtualenv --python=`which python3` venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
```

**Pautes a tenir en compte**

* ***Creant el sòcol (o socket) de Gunicorn***

```sh
$ sudo nano /etc/systemd/system/gunicorn.socket
```

| /etc/systemd/system/gunicorn.socket  |                                                                                                
|--------------------------------------------------------------------------------------------------------------------------------------|
| [Unit]<br>Description=gunicorn socket<br><br>[Socket]<br>ListenStream=/run/gunicorn.sock<br><br>[Install]<br>WantedBy=sockets.target |

<br/>

* ***Creant els serveis de Gunicorn***

```sh
$ sudo nano /etc/systemd/system/gunicorn.service
```

| /etc/systemd/system/gunicorn.service |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit]<br>Description=gunicorn daemon<br>Requires=gunicorn.socket<br>After=network.target<br><br>[Service]<br>User=***sammy***<br>Group=www-data<br>WorkingDirectory=/home/sammy/myprojectdir<br>ExecStart=/home/***sammy***/***myprojectdir***/***myprojectenv***/bin/gunicorn\ <br>    --access-logfile -\ <br>          --workers 3\ <br>          --bind unix:/run/gunicorn.sock \ <br>          ***myproject***.wsgi:application<br><br>[Install]<br>WantedBy=multi-user.target |


**Nota**: Reemplaça *sammy* per el teu nom d'usuari, *myprojectdir* per el teu directori del projecte, *myprojectenv* per el nom del teu entorn virtual (virtualenv) i *myproject* per la teva carpeta de projecte (la carpeta on es troba l'arxiu *`settings.py`*).

Activam els serveis:
```sh
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
```

Comprovam que el *socket* funciona:
```sh
$ curl --unix-socket /run/gunicorn.sock localhost
```

Comprovam que el servei de Gunicorn funciona i està en marxa:

```sh
$ sudo systemctl status gunicorn
```

**Nota:** Si en algun moment es realitzen canvis a `/etc/systemd/system/gunicorn.service`, s'hauran d'introduir les següents ordres:

```sh
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
```

* ***Configurar Nginx com a servidor web del desplegament***
```sh
$ sudo nano /etc/nginx/sites-available/projecte
```

| /etc/nginx/sites-available/projecte 	|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| server {<br>    listen 80;<br>    server_name ***server_domain_or_IP***;<br><br>    location = /favicon.ico { access_log off; log_not_found off; }<br>    location /static/ {<br>        root /home/***sammy***/***myprojectdir***;<br>    }<br><br>    location / {<br>        include proxy_params;<br>        proxy_pass `http://unix:/run/gunicorn.sock`;<br>    }<br>} 	|

**Nota**: Reemplaça *sammy* per el teu nom d'usuari, *myprojectdir* per el teu directori del projecte, i *server_domain_or_IP* per la teva IP (o domini si en disposa d'un).

Activam la configuració:

```sh
$ sudo ln -s /etc/nginx/sites-available/projecte /etc/nginx/sites-enabled
```

Per comprovar si no tenim faltes de sintaxi a l'arxiu de configuració de l'nginx, posam:
```sh
$ sudo nginx -t
```

Reiniciam el servei:
```sh
$ sudo systemctl restart nginx
```

*Nota*: Si disposa d'un firewall, s'haurà de permetre l'execució del servei d'nginx executant:
```sh
$ sudo ufw allow 'Nginx Full'
```

#### Servidor Ubuntu 18.04.3 LTS

El servidor està configurat a partir d'una IP estàtica (192.168.1.200).
L'arxiu de configuració per canviar la IP es troba a **/etc/netplan/01-netcfg.yaml**.
L'aplicació es desplega automàticament a tota la xarxa local quan s'inicia el sistema, per tant per veure la pàgina web s'ha d'obrir un navegador a la direcció 192.168.1.200.

##### Nota a l'hora de canviar l'IP a aquest servidor
Com que es tracta d'un servidor de producció, també s'haurà de canviar *ALLOWED_HOSTS* (ubicat a *~/pa-amb-oli/pa_amb_olis/settings.py*) i el fitxer de configuració d'nginx (ubicat a */etc/nginx/sites-enabled/django*).

També disposa d'un tallafocs, on només es permeten els ports 80 (emprat per nginx) i 22 (emprat per openssh).

##### Informació bàsica
```sh
LOGIN
User: admin
Password: admin0
------------------------------------------------
POSTGRES
*Usuari amb tots els privilegis a la base de dades `paambolis`*
User: paambolis
Password: paambolis (molt recomanat canviar-la)
------------------------------------------------
```
