# frontend

> A Python3 project

# Instalação manual

``` bash
# Instale o python3
sudo apt install python3

# Instale o pip para gerenciar os pacotes do python
sudo apt install python3-pip

# Instale as dependências
pip3 install django
pip3 install djangorestframework
pip3 install django-cors-headers
```

# Instalação docker local


``` bash
# Instale as dependências
docker build -t backend .

# Inicie o servidor
docker run -it --name backend --network host backend

```

# Instalação docker remoto

```bash
docker run -it --name backend --network host jonashs93/python-server-api:1.0
```
