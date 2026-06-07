---
title: Docker
parent: Linux
grand_parent: General
nav_order: 11
---

```zsh
┌──(kali㉿kali)-[~/CTF/WiFiChallengeLab-docker]
└─$ docker ps -a
CONTAINER ID   IMAGE                                    COMMAND                  CREATED         STATUS                          PORTS     NAMES
8d25be61c4cf   r4ulcl/wifichallengelab-nzyme:latest     "docker-entrypoint.s…"   5 minutes ago   Restarting (1) 48 seconds ago             WiFiChallengeLab-nzyme
424f117a491c   postgres:14                              "docker-entrypoint.s…"   5 minutes ago   Restarting (1) 34 seconds ago             WiFiChallengeLab-nzyme-db
71b4971a8a63   r4ulcl/wifichallengelab-clients:latest   "/bin/bash /root/ns-…"   5 minutes ago   Up 5 minutes (unhealthy)                  WiFiChallengeLab-Clients
973ff21e0833   r4ulcl/wifichallengelab-aps:latest       "/bin/bash /root/ns-…"   5 minutes ago   Up 5 minutes (unhealthy)                  WiFiChallengeLab-APs
b8329118119e   specterops/bloodhound:latest             "/bloodhound -config…"   11 days ago     Exited (0) 4 days ago                     bloodhound-bloodhound-1
0e3809d95042   neo4j:4.4                                "tini -g -- /startup…"   11 days ago     Exited (0) 4 days ago                     bloodhound-graph-db-1
ef2e1dfba5fd   postgres:16                              "docker-entrypoint.s…"   11 days ago     Exited (0) 4 days ago                     bloodhound-app-db-1
```