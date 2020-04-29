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

L'arxiu (*Client*) es troba a la següent ubicació:

https://drive.google.com/drive/folders/1jSspBK8EuYGYZ9g2RlEogJdboUUTTkMh?usp=sharing

Per tant, descarregar i importar l'arxiu (.ova) que més convengui.

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
$ python manage.py runserver
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
Password: paambolis
------------------------------------------------
```
