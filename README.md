Para instalar alguma role do repositorio oficial basta fazer assim dentro da pasta ansible:
ansible-galaxy install nickjj.swapfile -p ./roles
nickjj.swapfile -> é a role que pegamso pronta para criar swap file

Para criar uma role no ansible
$ ansible-galaxy init [name_new_role]

Para rodar o exemplo localmente
```ssh
$ vagrant up
$ ansible-playbook -i hosts_test deploy_test_local.yml
```

Para rodar um playbook apenas para um set de hosts:
$ ansible-playbook -i hosts_test tasks.yml -l chronos

Para rodar um playbook apenas para um set de hosts e tb para uma tag em especifico:
$ ansible-playbook -i hosts_test tasks.yml -l chronos -t deploy