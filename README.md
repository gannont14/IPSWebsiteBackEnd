## Prerequisites
Before you begin, ensure you have the following installed on your system:

- **Python** (version 3.x recommended)
- **pip** (Python package installer)
## Setting up the Development Environment
### 1. Install `virtualenv` using `pip` if it's not already installed:

```bash
pip install virtualenv
Clone the repository into a directory.
```
### 2. Create a Virtual Environment
Navigate to your project directory and run the following command to create a virtual environment:
```bash 
virtualenv venv
```
Here, `venv` is the name of the directory where the virtual environment will be created. You can replace `venv` with any name you prefer.

### 3. Activate the Virtual Environment

Once the virtual environment is created you need to activate it. run the following command:
#### on Windows:
```bash
    .\venv\Scripts\activate
```

#### on Mac OS:
```bash
    source venv/bin/activate
```
After activation, your command prompt will change to indicate that the virtual environment is active.


### 4. Install Project Dependencies
With the virtual environment activated, install your project's dependencies:

```bash
    pip install -r requirements.txt
```
If you don't have a `requirements.txt` file yet, you can create one by listing your project's dependencies:

```bash
    pip freeze > requirements.txt
```
### 5. Deactivate the Virtual Environment
When you're done working in your virtual environment, you can deactivate it by running:

```bash
    deactivate
```
### 6. Additional Tips
To delete the virtual environment, simply remove the venv directory:

```bash
rm -rf venv
```
If you're working on multiple projects, remember to activate the respective virtual environment before running any Python scripts or installing packages.



## Updating backend to postgresql

[download postgresql from online](https://www.postgresql.org/)

Open psql shell

Press enter through all prompts until you are able to input command

Create new file with .sql extension paste the following:

```sql
    CREATE DATABASE IPSDATABASE;
    CREATE USER postgres WITH PASSWORD  'postgres';
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE IPSDATABASE TO postgres
```

**OR** you can paste the above code directly into PSQL shell

Copy the path of the `.sql` file.

In psql shell type `\i <FILE_PATH>`.

Run `\l` in PSQL shell, make sure 'ipsdatabase' is there

Create .env file in root of project, paste the following...
FILE IS NAMED `.env`
yes that is it

Change password in .env to use the password that you setup

```
DB_NAME=ipsdatabase
DB_USER=postgres
DB_PASSWORD=postgress
DB_HOST=localhost
DB_PORT=5432
```

run in django:
`python manage.py migrate`

before you run django server again:

`python manage.py createsuperuser`

Make what credentials you want.

Run: `python manage.py runserver`
