# Part III. Compose

## I. Getting started

### 1. Run it

Lancez les deux conteneurs avec docker compose

```powershell
➜ docker compose up -d
time="2025-06-23T11:58:35+02:00" level=warning msg="C:\\Users\\utilisateur\\Desktop\\docker-avance\\docker-avance\\tp1\\part3-compose\\compose_test\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 3/3
 ✔ conteneur_flopesque Pulled                                                                                                                                                                                               3.3s
   ✔ 0c01110621e0 Already exists                                                                                                                                                                                            0.0s
 ✔ conteneur_nul Pulled                                                                                                                                                                                                     3.5s
[+] Running 3/3
 ✔ Network compose_test_default                  Created                                                                                                                                                                    0.3s
 ✔ Container compose_test-conteneur_flopesque-1  Started                                                                                                                                                                    0.8s
 ✔ Container compose_test-conteneur_nul-1        Started
```

Vérifier que les deux conteneurs tournent

```sleep
➜ docker ps
CONTAINER ID   IMAGE     COMMAND        CREATED              STATUS              PORTS     NAMES
a2137d3fe8dd   debian    "sleep 9999"   About a minute ago   Up About a minute             compose_test-conteneur_nul-1
a7b37f1e9bc3   debian    "sleep 9999"   About a minute ago   Up About a minute             compose_test-conteneur_flopesque-1
```

### 2. What about networking

Pop un shell dans le conteneur conteneur_nul

```powershell
➜ docker exec -it compose_test-conteneur_nul-1 sh
# ping conteneur_flopesque
sh: 1: ping: not found
# apt-get install ping
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package ping
```

```powershell
# apt-get -qq -y install iputils-ping
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package libcap2-bin.
(Reading database ... 6745 files and directories currently installed.)
Preparing to unpack .../libcap2-bin_1%3a2.66-4+deb12u1_amd64.deb ...
Unpacking libcap2-bin (1:2.66-4+deb12u1) ...
Selecting previously unselected package iputils-ping.
Preparing to unpack .../iputils-ping_3%3a20221126-1+deb12u1_amd64.deb ...
Unpacking iputils-ping (3:20221126-1+deb12u1) ...
Selecting previously unselected package libpam-cap:amd64.
Preparing to unpack .../libpam-cap_1%3a2.66-4+deb12u1_amd64.deb ...
Unpacking libpam-cap:amd64 (1:2.66-4+deb12u1) ...
Setting up libcap2-bin (1:2.66-4+deb12u1) ...
Setting up libpam-cap:amd64 (1:2.66-4+deb12u1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can t locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.36.0 /usr/local/share/perl/5.36.0 /usr/lib/x86_64-linux-gnu/perl5/5.36 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.36 /usr/share/perl/5.36 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
debconf: falling back to frontend: Teletype
Setting up iputils-ping (3:20221126-1+deb12u1) ...
# ping
ping: usage error: Destination address required
# ping conteneur_flopesque
PING conteneur_flopesque (172.29.0.3) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.29.0.3): icmp_seq=1 ttl=64 time=1.51 ms...
...
```

## II. A working meow-api

```docker
➜ docker compose up --build
time="2025-06-23T13:25:08+02:00" level=warning msg="C:\\Users\\utilisateur\\Desktop\\docker-avance\\docker-avance\\tp1\\part3-compose\\meow_compose\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 3/2
 ✔ Network meow_compose_default  Created                                                                                                                                                                                    0.1s
 ✔ Container mysql-db            Created                                                                                                                                                                                    0.1s
 ✔ Container meow-api            Created                                                                                                                                                                                    0.1s
Attaching to meow-api, mysql-db
mysql-db  | 2025-06-23 11:25:09+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 9.0.1-1.el9 started.
mysql-db  | 2025-06-23 11:25:09+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql-db  | 2025-06-23 11:25:09+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 9.0.1-1.el9 started.
mysql-db  | 2025-06-23 11:25:09+00:00 [Note] [Entrypoint]: Initializing database files
mysql-db  | 2025-06-23T11:25:09.954882Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
mysql-db  | 2025-06-23T11:25:09.956458Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 9.0.1) initializing of server in progress as process 80
mysql-db  | 2025-06-23T11:25:09.970425Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
meow-api  |  * Serving Flask app 'app'
meow-api  |  * Debug mode: off
meow-api  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
meow-api  |  * Running on all addresses (0.0.0.0)
meow-api  |  * Running on http://127.0.0.1:8000
meow-api  |  * Running on http://172.29.0.3:8000
meow-api  | Press CTRL+C to quit
mysql-db  | 2025-06-23T11:25:10.375993Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql-db  | 2025-06-23T11:25:12.143263Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
mysql-db  | 2025-06-23T11:25:14.388959Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
mysql-db  | 2025-06-23 11:25:14+00:00 [Note] [Entrypoint]: Database files initialized
...
```

```powershell
➜ curl -X GET http://127.0.0.1:8000/users
[{"favorite_insult":"You have something on your chin\u00e2\u20ac\u00a6 no, the third one down.","id":1,"name":"Alice"},{"favorite_insult":"You bring everyone so much joy\u00e2\u20ac\u00a6 when you leave the room.","id":2,"name":"Bob"},{"favorite_insult":"You are as useless as the \"ueue\" in \"queue\".","id":3,"name":"Charlie"},{"favorite_insult":"You have something on your face: stupidity.","id":4,"name":"Diana"},{"favorite_insult":"If I had a dollar for every smart thing you say, I would be broke.","id":5,"name":"Eve"}]
 ~                                                                                                                                                                                                     13:26:27
➜ curl -X GET http://127.0.0.1:8000/user/3
{"favorite_insult":"You are as useless as the \"ueue\" in \"queue\".","id":3,"name":"Charlie"}
```