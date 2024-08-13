### Updating backend to postgresql

download postgresql from online
`https://www.postgresql.org/`

open psql shell

press enter through all prompts until you are able to input command

create new file with .sql extension paste the following

    CREATE DATABASE IPSDATABASE;
    CREATE USER postgres WITH PASSWORD  'postgres';
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE IPSDATABASE TO postgres;

OR

paste above code directly into psql shell

copy file path

in psql shell type "\i FILE_PATH"

run `\l` in psql shell, make sure 'ipsdatabase' is there

create .env file in root of project, paste the following...
FILE IS NAMED `.env`
yes that is it

Change password in .env to use the password that you setup

```
DB_NAME=ipsdatabase
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

run in django:
`python manage.py migrate`

before you run django server again:

`python manage.py createsuperuser`

make what credentials you want
