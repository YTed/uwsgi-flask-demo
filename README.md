# A demo of deploying flask app to docker

### Test

- Run `FLASK_APP=src/main/web/web.py FLASK_DEBUG=1 flask run --port=5000`
- Visit http://127.0.0.1:5000

### Deploy

- Run `docker build -t myimage .` 
- Run `docker run -it -p 5000:80 --name mycontainer myimage`
- Reappare [issue#18](https://github.com/tiangolo/uwsgi-nginx-flask-docker/issues/18) 
