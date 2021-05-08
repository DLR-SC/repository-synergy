# guestbook

## Docker Docker Docker

1. [Docker](https://docs.docker.com/installation/) 1.7.0
1. [Docker Machine](https://docs.docker.com/machine/#installation) 0.3.0
1. [Docker Compose](https://docs.docker.com/compose/install/) 1.3.0

# Local

## Initialize the Environment

```
docker-machine create --driver virtualbox guestbook-dev
eval "$(docker-machine env guestbook-dev)"
docker-compose up
```

## Initialize the Database

```
docker-compose run --rm --no-deps app python app.py create_db
```

# Remote

## Initialize the Environment

```
export OS_USERNAME=your-rackspace-username
export OS_API_KEY=your-rackspace-api-key
export OS_REGION_NAME=IAD
```

```
docker-machine create --driver rackspace guestbook
eval "$(docker-machine env guestbook)"
docker-compose --file docker-compose-prod.yml build
docker-compose --file docker-compose-prod.yml up -d
```

## Initialize the Database

```
export MYSQL_USER=guestbook-admin
export MYSQL_PASSWORD=$(hexdump -v -e '1/1 "%.2x"' -n 32 /dev/random)
export MYSQL_ROOT_PASSWORD=$(hexdump -v -e '1/1 "%.2x"' -n 32 /dev/random)

docker-compose --file docker-compose-prod.yml run --rm --no-deps app python app.py create_db
```

## Secure the Environment

```
docker-machine ssh guestbook "apt-get update"
docker-machine ssh guestbook "apt-get -y install fail2ban"
docker-machine ssh guestbook "ufw default deny"
docker-machine ssh guestbook "ufw allow ssh"
docker-machine ssh guestbook "ufw allow http"
docker-machine ssh guestbook "ufw allow 2376" # Docker
docker-machine ssh guestbook "ufw --force enable"
```

## Deploy Changes to Remote

```
docker-compose --file docker-compose-prod.yml build
docker-compose --file docker-compose-prod.yml up -d --x-smart-recreate
```

## Work with the Database

```
docker run --rm --link dockerguestbook_db_1:db mysql:5.7 sh -c \
  'exec mysql \
  --host=$DB_PORT_3306_TCP_ADDR \
  --user=root \
  --password=$DB_ENV_MYSQL_ROOT_PASSWORD \
  --database=$DB_ENV_MYSQL_DATABASE \
  --execute="show tables;" \
  --table'

docker run --rm --link dockerguestbook_db_1:db mysql:5.7 sh -c \
  'exec mysqldump \
  --host=$DB_PORT_3306_TCP_ADDR \
  --user=root \
  --password=$DB_ENV_MYSQL_ROOT_PASSWORD \ 
  --databases $DB_ENV_MYSQL_DATABASE \
  --single-transaction \
  --add-drop-database' > $DB_ENV_MYSQL_DATABASE.sql
```

## Alias

```
alias de='env | grep DOCKER_'
```