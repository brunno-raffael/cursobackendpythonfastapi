<h1>Projetos Backend Python + FastAPI</h1> 

<p align="center">
  <a href="https://twitter.com/brunnoraffael"><img src="https://img.shields.io/twitter/follow/brunnoraffael.svg?style=social" align="right" alt="Twitter Follow" /></a>
  
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [Tarefas em aberto](#tarefas-em-aberto)

:small_blue_diamond: [Desenvolvedores e Contribuintes](#desenvolvedores-e-contribuintes)

:small_blue_diamond: [Agrecimentos Especiais](#agradecimentos-especiais)


## Descrição do projeto 

<p align="justify">
  Projetos criados e melhorados usando como base Curso de Backend com Python e FastAPI
</p>

## Funcionalidades

<h3>
Hello (Sem Front-End)
</h3>

:heavy_check_mark: Exemplos de métodos básicos (GET, POST, PUT, DELETE)

:heavy_check_mark: Exemplos de métodos com operações básicas (Tratamento de Texto e Operações Matemáticas)

<h3>
AppAnimal (Com Front-End)
</h3>

:heavy_check_mark: Exemplos de métodos básicos (GET, POST, DELETE)

<h3>
AppBLX (Sem Front-End + Com Bando de Dados (SQLite))
</h3>

:heavy_check_mark: Exemplos de métodos básicos (GET, POST)

:heavy_check_mark: Exemplos de manipulação de dados (INSERT, SELECT)

## Pré-requisitos

:warning: [Python](https://python.org.br/)


## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/brunno-raffael/cursobackendpythonfastapi.git
```

No terminal, instale os requisitos :

```
pip install -r requirements.txt
```

<h3>
Executando Front-End
</h3>
No VSCode, instale a extensão (Ctrl + Shift + X) do Live Server.
Depois clique com botão direito no arquivo HTML no Explorador de Arquivos e clique na opção Open with Live Server.

<h3>
Executando Back-End
</h3>

No terminal, execute o projeto através do Uvicorn (https://www.uvicorn.org/) :

```
uvicorn src.server:app --reload --reload-dir=src
```


## Tarefas em aberto

:memo: Tarefa 1 

## Desenvolvedores e Contribuintes

| [<img src="https://avatars.githubusercontent.com/u/25123693?s=400&u=5b458b8afd2b834f55564077098dd8a0ce64b07f&v=4" width=115><br><sub>Brunno Raffael</sub>](https://github.com/brunno-raffael) |

## Agradecimentos Especiais

Professor Rogerio Silva - Playlist do Curso : <a href="https://www.youtube.com/watch?v=Hx6w7JXYHbY&list=PLuhCJtW2i-wKK9HjfYJI4RIcd9AMIi88k" target="_blank"> Backend com Python & FastAPI - 2021</a>
