# A demo of deploying flask app to docker

### Test

- Run `python src/main.py 5000`
- Visit http://127.0.0.1:5000

### Deploy

- Run `docker build -t myimage .` 
- Run `docker run -it -p 5000:80 -t mycontainer myimage`
- Reappare [issue#18](https://github.com/tiangolo/uwsgi-nginx-flask-docker/issues/18) 
