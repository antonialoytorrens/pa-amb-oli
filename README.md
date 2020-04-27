# Pamboliada
Projecte Final FCT - CFGS Desenvolupament d'Aplicacions Web

# Guia ràpida per començar

## Si es vol visitar el lloc web

El lloc web es troba a https://www.pamboliada.cat.

## Si es vol realitzar el desplegament en local

```sh
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
