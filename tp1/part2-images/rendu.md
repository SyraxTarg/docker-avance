# Part 2 - Images

## I. Images publiques

Récupérez des images

```powershell
➜ docker pull python:3.11
3.11: Pulling from library/python
0c01110621e0: Already exists
3b1eb73e9939: Already exists
b1b8a0660a31: Already exists
48b8862a18fa: Already exists
05b4f72d6599: Pull complete
a9ebf62fca91: Pull complete
1adad7254e67: Pull complete
Digest: sha256:ce3b954c9285a7a145cba620bae03db836ab890b6b9e0d05a3ca522ea00dfbc9
Status: Downloaded newer image for python:3.11
docker.io/library/python:3.11

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview python:3.11
```

```powershell
➜ docker pull mysql:5.7
5.7: Pulling from library/mysql
Digest: sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb
Status: Image is up to date for mysql:5.7
docker.io/library/mysql:5.7

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview mysql:5.7
```

```powershell
➜ docker pull wordpress:latest
latest: Pulling from library/wordpress
dad67da3f26b: Already exists
2db68c25baf9: Pull complete
00f5acde88f9: Pull complete
cd38bdb81e9f: Pull complete
76c084d1f5e9: Pull complete
80ec8928a9e9: Pull complete
5c36895ebc3c: Pull complete
b9ac79a9d3f2: Pull complete
dac7e3178ae3: Pull complete
e383a70201f7: Pull complete
9f8818a56c42: Pull complete
ebf1e813808c: Pull complete
9a2bb7cb8ab8: Pull complete
4f4fb700ef54: Pull complete
11cfd97ff391: Pull complete
64f31fc6b484: Pull complete
01bb8cda2d5a: Pull complete
f407a062cc9d: Pull complete
d8f7a74af326: Pull complete
f30a6ec49360: Pull complete
12af0e7127ba: Pull complete
fcdcb87098fb: Pull complete
Digest: sha256:1931132b0b93230ee44d9628868e3ffe2076f49ba6569b36d281c0ccaa618ef4
Status: Downloaded newer image for wordpress:latest
docker.io/library/wordpress:latest

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview wordpress:latest
```

```powershell
➜ docker pull linuxserver/wikijs:latest
latest: Pulling from linuxserver/wikijs
cf5e609968fc: Pull complete
e1cde46db0e1: Pull complete
ea659dc5ec12: Pull complete
0602714159b7: Pull complete
2ec689af27a3: Pull complete
8d8f2cc9e847: Pull complete
d01bb9a068c1: Pull complete
a0fc79057ecf: Pull complete
16009be9e92d: Pull complete
Digest: sha256:f997a921b7695fc7528740ad2c36c10b0b9c23b2878a937487367ad98df15591
Status: Downloaded newer image for linuxserver/wikijs:latest
docker.io/linuxserver/wikijs:latest

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview linuxserver/wikijs:latest
```

```powershell
➜ docker images
REPOSITORY                                      TAG         IMAGE ID       CREATED          SIZE
it4lik/meow-api                                 latest      b91b5ab0010d   41 minutes ago   234MB
rally-rally-back                                latest      31cc3b3510d2   20 hours ago     392MB
<none>                                          <none>      815ea5581b24   21 hours ago     506MB
...
```

## II. Construire une image

### A. Build la meow-api

Récupérer le code et le Dockerfile sur votre machine

```powershell
➜ mkdir app; mv app.py app/app.py; mv Dockerfile app/Dockerfile; mv requirements.txt app/requirements.txt

    Directory: C:\Users\utilisateur\Desktop\docker-avance\docker-avance\tp1\part2-images

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          23/06/2025    10:57                app

```

Build une image meow-api

```powershell
➜ docker build . -t meow-api
[+] Building 6.7s (10/10) FINISHED                                                                                                                                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                        0.0s
 => => transferring dockerfile: 585B                                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                                                                                                         0.5s
 => [internal] load .dockerignore                                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                                             0.0s
 => CACHED [1/5] FROM docker.io/library/python:3.12-slim@sha256:e55523f127124e5edc03ba201e3dbbc85172a2ec40d8651ac752364b23dfd733                                                                            0.0s
 => [internal] load build context                                                                                                                                                                           0.0s
 => => transferring context: 104B                                                                                                                                                                           0.0s
 => [2/5] WORKDIR /app                                                                                                                                                                                      0.0s
 => [3/5] COPY ./requirements.txt .                                                                                                                                                                         0.1s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                5.6s
 => [5/5] COPY ./app.py .                                                                                                                                                                                   0.1s
 => exporting to image                                                                                                                                                                                      0.3s
 => => exporting layers                                                                                                                                                                                     0.3s
 => => writing image sha256:1675c625cff5ef9ab485aa67b0498d535c81ac9010bad7b43ffe7bf1464753df                                                                                                                0.0s
 => => naming to docker.io/library/meow-api                                                                                                                                                                 0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/mtccvhlh6lxh5p1urm9wx4rcw

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```

Afficher la liste des images dispos sur votre machine

```powershell
➜ docker images
REPOSITORY                                      TAG         IMAGE ID       CREATED              SIZE
meow-api                                        latest      1675c625cff5   About a minute ago   234MB
it4lik/meow-api                                 latest      b91b5ab0010d   53 minutes ago       234MB
```

Run cette image

```powershell
➜ docker run meow-api
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
```

### B. Packagez vous-même une app

Ecrire un Dockerfile pour packager ce code

=> voir `./app-bis`

Build l'image

```powershell
➜ docker build . -t app-bis:1.0.0
[+] Building 3.2s (10/10) FINISHED                                                                                                                                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                        0.0s
 => => transferring dockerfile: 580B                                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                                             0.0s
 => [1/5] FROM docker.io/library/python:3.11                                                                                                                                                                0.2s
 => [internal] load build context                                                                                                                                                                           0.1s
 => => transferring context: 182B                                                                                                                                                                           0.0s
 => [2/5] WORKDIR /app                                                                                                                                                                                      0.0s
 => [3/5] COPY ./requirements.txt .                                                                                                                                                                         0.1s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                2.5s
 => [5/5] COPY ./app.py .                                                                                                                                                                                   0.1s
 => exporting to image                                                                                                                                                                                      0.1s
 => => exporting layers                                                                                                                                                                                     0.1s
 => => writing image sha256:a03f0346351b5b956ee0903d0772c35189a6cee46f5a9109803fb82a3278298f                                                                                                                0.0s
 => => naming to docker.io/library/app-bis:1.0.0                                                                                                                                                            0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/w0tx5m9f4u0d408nqprtgrx9a

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```

Proof !

```powershell
➜ docker images
REPOSITORY                                      TAG         IMAGE ID       CREATED             SIZE
app-bis                                         1.0.0       a03f0346351b   53 seconds ago      1.03GB
meow-api                                        latest      1675c625cff5   8 minutes ago       234MB
```

Lancer l'image

```powershell
➜ docker run app-bis:1.0.0
Cet exemple d'application est vraiment naze 👎
```

### C. Ecrire votre propre Dockerfile

Ecrire un Dockerfile pour packager votre application

J'ai fait un petit script tout simple qui ressemble a un cowsay.

```powershell
FROM python:3.11

WORKDIR /app

COPY ./main.py .

CMD ["python", "main.py"]

```

Publiez votre image sur le Docker Hub

```powershell
➜ docker build . -t 20220796/raqiros:1.0.0
[+] Building 0.5s (8/8) FINISHED                                                                                                                                                                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                        0.1s
 => => transferring dockerfile: 252B                                                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                                                                                           0.1s
 => => transferring context: 2B                                                                                                                                                                                             0.0s
 => [1/3] FROM docker.io/library/python:3.11                                                                                                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                           0.1s
 => => transferring context: 718B                                                                                                                                                                                           0.0s
 => CACHED [2/3] WORKDIR /app                                                                                                                                                                                               0.0s
 => [3/3] COPY ./main.py .                                                                                                                                                                                                  0.1s
 => exporting to image                                                                                                                                                                                                      0.1s
 => => exporting layers                                                                                                                                                                                                     0.1s
 => => writing image sha256:6c4594524564735cf833b2152f778f186ae143e2cc0b6b50ee3a137f6cbbc068                                                                                                                                0.0s
 => => naming to docker.io/20220796/raqiros:1.0.0                                                                                                                                                                           0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/fmy5l3opzsk8mgzls85ocx5t7

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```

```powershell
➜ docker push 20220796/raqiros:1.0.0
The push refers to repository [docker.io/20220796/raqiros]
66969ded25a7: Pushed
ccd52a45dbf3: Pushed
13bf59a1a40a: Mounted from library/python
ed64afdf4a28: Mounted from library/python
c9de1d8ec5b9: Mounted from library/python
f9093a7aaa16: Mounted from library/python
1c49688bd8eb: Mounted from library/python
f5b8fb1def00: Mounted from library/python
8f003894a7ef: Mounted from library/python
1.0.0: digest: sha256:bf9267818b5b5c3674c7990a44bac36a99296e5e421440ea31b7b55201ccb1c1 size: 2209
```

url de l'image sur docker hub: https://hub.docker.com/r/20220796/raqiros/tags

commande:

```powershell
docker pull 20220796/raqiros:1.0.0
```
