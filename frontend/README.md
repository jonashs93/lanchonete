# frontend

> A Vue.js project

# Instalação manual

``` bash
# Instale as dependências
npm install

# Inicie o servidor
npm run dev

# Rode os testes obs: o backend deve estar rodando na porta localmente na porta 8000
npm test
```

# Instalação docker local


``` bash
# Instale as dependências
docker build -t frontend .

# Inicie o servidor
docker run -it --name frontend --network host frontend

```

# Instalação docker remoto

```bash
docker run -it --name frontend --network host jonashs93/vue-cli:1.0
```
