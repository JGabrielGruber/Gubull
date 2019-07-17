# Gubull
Aplicação destinada a controle de bovinos

## Implementação

### Requisitos

* python3
* python-virtualenv
* python-pip

### Instalação

Em seu terminal(Linux):

1. Crie um VirtualEnv:
```
$ virtualenv Gubull/
```
2. Navegue para o mesmo:
```
$ cd Gubull/
```
3. Ative o env no seu terminal:
```
$ source bin/activate
```
4. Clone o repositório:
```
$ git clone https://github.com/JGabrielGruber/Gubull.git
```
5. Navegue para pasta do projeto:
```
$ cd Gubull/
```
6. Instale os requisitos do pip:
```
$ pip install -r requirements.txt
```
7. Navegue na para o src:
```
$ cd src/
```
8. Crie as migrações do modelos do django:
```
$ python manage.py makemigrations
```
9. Crie as migrações do modelo animais:
```
$ python manage.py makemigrations animais
```
9. Realize as migrações:
```
$ python manage.py migrate
```

### Uso
Em seu terminal, na pasta src do projeto:

2. Inicie o servidor django, com acesso a qualquer IP:
```
$ sudo python manage.py runserver 0.0.0.0:80
```
