# Part 1 - Init

## 1. Simple run

 Lancer un conteneur meow-api

```powershell
➜ docker run -p 8000:8000 it4lik/meow-api
Unable to find image 'it4lik/meow-api:latest' locally
latest: Pulling from it4lik/meow-api
0c01110621e0: Pull complete
3b1eb73e9939: Pull complete
b1b8a0660a31: Pull complete
48b8862a18fa: Pull complete
20d0b4e6a2e6: Pull complete
77a6ac598bc1: Pull complete
5cc4a19fbac0: Pull complete
cb5bd488993b: Pull complete
3828cfa2baf2: Pull complete
Digest: sha256:51264a230802917353c166e1c4989fa94d22f632c8f10db2a8ff273d2a2887e4
Status: Downloaded newer image for it4lik/meow-api:latest
```

Visitons

```powershell
➜ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                    NAMES
2c2c627ab88b   it4lik/meow-api   "python3 -m http.ser…"   23 seconds ago   Up 22 seconds   0.0.0.0:8000->8000/tcp   interesting_williams
 ~
```

```powershell
➜ docker logs interesting_williams
```

```powershell
➜ docker inspect interesting_williams
[
    {
        "Id": "2c2c627ab88b6ed1328c8977dc6c963826db5f644536eb84444afc0e3661ffad",
        "Created": "2025-06-23T07:48:31.536403941Z",
        "Path": "python3",
        "Args": [
            "-m",
            "http.server",
            "8888"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1477,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-06-23T07:48:31.7250657Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
...
```

```powershell
➜ docker run -p 8000:8000 it4lik/meow-api:latest
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
172.17.0.1 - - [23/Jun/2025 08:10:20] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jun/2025 08:10:20] "GET /favicon.ico HTTP/1.1" 404 -

```

Lancer le conteneur en tâche de fond

```powershell
➜ docker run -p 8000:8000 -d it4lik/meow-api
5d14757dc019df13eb6f3f250b2f4e360de6ce8d8b7f4efa40f59fe5e771191e
```

Consultez les logs du conteneur

```powershell
➜ docker logs condescending_ardinghelli -f
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
172.17.0.1 - - [23/Jun/2025 08:10:20] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jun/2025 08:10:20] "GET /favicon.ico HTTP/1.1" 404 -
```

## 2. Volumes

Remplacer le code app.py

```python
from os import getenv
from flask import Flask, jsonify

LISTEN_PORT = getenv("LISTEN_PORT", 8000)
DB_HOSTNAME = getenv("DB_HOSTNAME", "db")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Hello world",
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=LISTEN_PORT)
```

```powershell
➜ docker run -p 8000:8000 -v "${PWD}/part1-init/app.py:/app/app.py" it4lik/meow-api
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
172.17.0.1 - - [23/Jun/2025 08:33:21] "GET / HTTP/1.1" 200 -
```

Prouvez que ça fonctionne avec une requête Web

```powershell
➜ curl -X GET http://127.0.0.1:8000/
{"message":"Hello world"}
```

## 3. Variable d'environnement

Définir une variable d'environnement au lancement du conteneur

```powershell
➜ docker run -e LISTEN_PORT=7000 it4lik/meow-api
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:7000
 * Running on http://172.17.0.2:7000
Press CTRL+C to quit
```

Mettez à jour l'option -p

```powershell
➜ docker run -e LISTEN_PORT=7000 -p 7000:7000 it4lik/meow-api
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:7000
 * Running on http://172.17.0.2:7000
Press CTRL+C to quit
```

Prouvez que ça fonctionne avec une requête Web

```powershell
➜ curl -X GET http://127.0.0.1:7000
{"message":"Available routes","routes":{"get_user_by_id":"http://127.0.0.1:7000/user/1","list_all_users":"http://127.0.0.1:7000/users"}}
```