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

### Uso
Em seu terminal, na pasta do projeto:

1. Navegue na para o src:
```
$ cd src/
```
2. Inicie o servidor django, com acesso a qualquer IP:
```
$ sudo python manage.py runserver 0.0.0.0:80
```
