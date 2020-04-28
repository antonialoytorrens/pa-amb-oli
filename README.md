# Pamboliada
Projecte Final FCT - CFGS Desenvolupament d'Aplicacions Web

# Guia ràpida per començar

## Si es vol visitar el lloc web

El lloc web es troba a http://www.pamboliada.cat.

## Si es vol realitzar el desplegament en local

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


### Altres

Baixar i instal·lar el programa VirtualBox corresponent al teu sistema operatiu: https://www.virtualbox.org

Els arxius de la màquina virtual (*Servidor* i *Servidor + Client*) es troben a la següent ubicació:

https://drive.google.com/drive/folders/1jSspBK8EuYGYZ9g2RlEogJdboUUTTkMh?usp=sharing

Per tant, descarregar i importar l'arxiu (.ova) que més convengui.

#### Servidor Ubuntu 18.04.3 LTS

El servidor està configurat a partir d'una IP estàtica (192.168.1.200).
L'arxiu de configuració per canviar la IP es troba a **/etc/netplan/01-netcfg.yaml**.
L'aplicació es desplega automàticament a tota la xarxa local quan s'inicia el sistema, per tant per veure la pàgina web s'ha d'obrir un navegador a la direcció 192.168.1.200:8000.

#### Servidor + Client Ubuntu 18.04.3 LTS (LXQt)

El servidor està configurat a partir d'una IP estàtica (192.168.1.201).
L'arxiu de configuració per canviar la IP es troba a **/etc/netplan/01-netcfg.yaml**.
L'aplicació es desplega automàticament a tota la xarxa local quan s'inicia el sistema, per tant per veure la pàgina web s'ha d'obrir un navegador a la direcció 192.168.1.201:8000, o en el propi sistema (firefox) a localhost:8000.

##### Informació bàsica (*Servidor* i *Servidor + Client*)
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
