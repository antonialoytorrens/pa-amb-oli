# Pamboliada
Projecte Final FCT - CFGS Desenvolupament d'Aplicacions Web

# Guia ràpida per començar

## Si es vol visitar el lloc web

El lloc web es troba a https://www.pamboliada.cat.

## Si es vol realitzar el desplegament en local

### Linux

```sh
$ sudo apt install python3 python3-venv python3-pip postgresql
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
### Altres

Baixar i instal·lar el programa VirtualBox corresponent al teu sistema operatiu: https://www.virtualbox.org

Descarregar i importar l'arxiu de la màquina virtual des de la següent ubicació: https://drive.google.com/drive/folders/1jSspBK8EuYGYZ9g2RlEogJdboUUTTkMh?usp=sharing

Realitzar les passes mencionades anteriorment en Linux:

```sh
$ sudo apt install python3 python3-venv python3-pip postgresql
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
#### Nota: Si l'aplicació es vol fer disponible a tots els dispositius de la xarxa local, canvia la darrera ordre per aquesta:

```sh
$ python manage.py runserver 0.0.0.0:8000
```

Així, l'aplicació és accessible tant per a localhost (127.0.0.1) com per altres dispositius (introduir la IP de la màquina virtual amb el port 8000, ex: 192.168.1.23:8000).

La IP de la màquina virtual es pot saber obrint un terminal (lxterminal) i introduir la ordre `ifconfig`.
