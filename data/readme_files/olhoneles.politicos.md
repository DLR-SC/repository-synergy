# Politicos API [![Build Status][build-status]][travis]

Aqui você vai encontrar os dados, ferramentas e recursos para realizar
pesquisas, desenvolver aplicativos, visualizações de dados e muito mais.


## Instalação

Temos duas formas para rodar o projeto, via [docker compose][docker-compose] ou
instalando as dependências manualmente.

### Clone o repositório:

```
git clone https://github.com/olhoneles/politicos.git
```

### Docker Compose

#### Subindo o projeto

```
cd politicos
docker-compose up
```

#### Para coletar os dados do TSE:

```
docker-compose exec api python collector.py -eh elasticsearch -l info
```

#### Para visualizar os dados:

Abra seu navegador e entre no endereço http://localhost:8888

### Manualmente

#### Crie um [*virtualenv*][virtualenv]:

```
cd politicos
mkvirtualenv politicos
```

#### Instale as dependências (python):

```
make setup
```

#### Instale o ElasticSearch e o Redis


* [ElasticSearch][elasticsearch]
* [Redis][redis-server]

#### Para coletar os dados do TSE:

```
make collect
```

#### Inicialize o projeto:

```
make run
```

Abra seu navegador e entre no endereço http://localhost:8888

## Como Contribuir

Participe da [lista de email][lista] e também via IRC no canal
[#olhoneles][freenode] na Freenode.

Faça uma cópia do repositório e envie seus pull-requests.


## Licença

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

[virtualenv]: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
[lista]: http://listas.olhoneles.org/cgi-bin/mailman/listinfo/montanha-dev
[freenode]: irc://irc.freenode.net:6667/olhoneles
[build-status]: https://secure.travis-ci.org/olhoneles/politicos.png?branch=master
[travis]: https://travis-ci.org/olhoneles/politicos
[docker-compose]: https://docs.docker.com/compose/install/
[elasticsearch]: https://www.elastic.co/downloads/elasticsearch
[redis-server]: https://redis.io/download
