# Projet Postagram: Un clone de Instagram (Backend Achevé !)
Ceci est le backend de Postagram développé avec Django et Django Rest Framework.

## Configuration
La première chose à faire est de cloner le repo:
```sh
$ git clone https://github.com/ordemdigitale/postagram.git
$ cd postagram
```

Créer un environment virtuel pour y installer les dépendances et l'activer:

```sh
$ python -m venv venv
$ source venv/bin/activate
```

Puis installer les dépendances:

```sh
(venv)$ pip install -r requirements.txt
```
Noter le `(venv)` devant le prompt. Cela indique que cette session de terminal
fonctionne dans un environnement virtuel mis en place par `python venv`.

Une fois que `pip` a fini de télécharger les dépendances:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

### Les différents endpoints:
Endpoint parent: `http://127.0.0.1:8000/api/` auquel ajouter les endpoints ci-dessous:

Register: `auth/register/`
Login: `auth/login/`
`auth/refresh/`
`users/`
`users/(?P<pk>[^/.]+)/`
`posts/`
`posts/(?P<pk>[^/.]+)/`
`posts/(?P<pk>[^/.]+)/like/`
`posts/(?P<pk>[^/.]+)/remove_like/`
`posts/(?P<post_pk>[^/.]+)/comments/`
`posts/(?P<post_pk>[^/.]+)/comments/(?P<pk>[^/.]+)/`

