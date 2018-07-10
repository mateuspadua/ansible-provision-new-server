# README #

### Qual o objetivo deste repositório? ###

* Criar e gerenciar o ambiente de desenvolvimento, tendo como objetivo prover com poucos ou apenas um comando
ambientes inteiros, facilitando assim a vida de novos membros da equipe e também o dia a dia
do desenvolvedor.
* Deploy dos projetos IASEAL para seus respectivos ambientes de produção e teste.
* Subir um ambiente de produção localmente fiel ao ambiente de produção remoto.

### Configurando o ambiente de desenvolvimento ###

1º - Crie o arquivo `~/.bash_aliases`

```ssh
$ cat ~/.bash_aliases
alias ll='ls -l'
alias dkcc='docker rm -f $(docker ps -q)'
alias dkic='docker rmi -f $(docker images -q)'
alias dkps='docker ps'
alias dkpsa='docker ps -a'
alias dkssh='. ~/docker-ssh'
```

2º - Para se logar no container de uma forma fácil, crie o arquivo `~/docker-ssh`

```ssh
$ cat ~/docker-ssh
#!/bin/bash -xe

# docker container id or name might be given as a parameter
CONTAINER=$1

if [[ "$CONTAINER" == "" ]]; then
  # if no id given simply just connect to the first running container
  CONTAINER=$(docker ps | grep -Eo "^[0-9a-z]{8,}\b")
fi

# start an interactive bash inside the container
# note some containers don't have bash, then try: ash (alpine), or simply sh
# the -l at the end stands for login shell that reads profile files (read man)
docker exec -i -t $CONTAINER bash -l
```

3º - Abra o arquivo `~./bash_profile` e cole o conteúdo abaixo

```ssh
if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi
```

### Dicas e comandos úteis ###

para rodar um comando dentro do **container 'web'**, ex:
```ssh
$ docker-compose exec web python manage.py makemigrations  # roda o comando 'makemigrations' no container 'web' que está em execução
$ docker-compose exec web python manage.py migrate  # roda o comando 'migrate' no container 'web' que está em execução
$ docker-compose run --rm web python manage.py migrate  # desta forma ele cria outra container e depois o destroi (não recomendado)
```

ssh(entrar) em um container que está em execução utilizando o script `~/docker-ssh`:
```ssh
$ dkps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                          PORTS                NAMES
0fd023e6056f        aula-composer2_nginx   "/usr/sbin/nginx"        2 hours ago         Up 2 hours                      0.0.0.0:80->80/tcp   aula-composer2_nginx_1
e45a89cbd7b3        aula-composer2_web     "/usr/bin/gunicorn w…"   2 hours ago         Up 2 hours                      8000/tcp             aula-composer2_web_1
bf98ad0e246d        postgres:latest        "docker-entrypoint.s…"   2 hours ago         Up 2 hours                      5432/tcp             aula-composer2_postgres_1
01fa716800ba        alpine                 "true"                   2 hours ago         Restarting (0) 41 seconds ago                        aula-composer2_data_1
2466a55df4b4        redis:latest           "docker-entrypoint.s…"   7 hours ago         Up 2 hours                      6379/tcp             aula-composer2_redis_1

$ dkssh e45a89cbd7b3
```

### Sobre as imagens utilizadas nos containers ###

Imagem [Alpine](https://hub.docker.com/_/alpine/) para o projeto

Imagem [Postgres](https://hub.docker.com/_/postgres/) para o banco de dados

Imagem [Redis](https://hub.docker.com/_/redis/) para o banco chave e valor

Imagem [Nginx](https://hub.docker.com/_/nginx/) para simular o ambiente de desevolvimento

### Inspirações para criação deste projeto

* http://www.inanzzz.com/index.php/post/6138/setting-up-a-nginx-docker-container-on-remote-server-with-ansible
* https://github.com/jcalazan/ansible-django-stack
* https://github.com/JoeJasinski/ansible-django-stack
* https://fangpenlin.com/posts/2014/11/13/provision-with-ansible-from-inside-docker/
* https://github.com/mateuspadua/demo-ansible-docker-orchestration/blob/master/install-docker.yml
* https://github.com/gabrielferreira/demo-ansible-docker-image
* https://github.com/leucos/ansible-tuto
* https://github.com/matic-insurance/ansible-docker-nginx
* https://medium.com/@cabot_solutions/ansible-and-docker-the-best-combination-for-an-efficient-software-product-management-28c86cfebe90

### Requisitos mínimos ###
* ???

### Como criar um ambiente de desenvolvimento ###

* Instale o Docker: https://docs.docker.com/install/#desktop

### Simular o ambiente de produção localmente ###

* Instale o Vagrant: https://www.vagrantup.com/downloads.html
* $ sudo pip install ansible
* $ vagrant up
* ansible-playbook -i hosts deploy_test_local.yml

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact