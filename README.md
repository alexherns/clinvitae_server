# clinvitae_server

This server provides endpoints for the CLInvitae application. Currently the database used is sqlite
but the db module should provide an abstraction such that the server could switch between db instances
based on the environment (caveat: I'm unsure whether the interface provided by sqlite3 is similar to other python db interfaces).


## 1. Installation

The server requires Python 2.7. Once you have that, I suggest using a virtual environment to install
the additional dependencies.

```sh
$ pip install -r requirements.txt
```

## 2. Creating the database

I wrote a script that should automate all tasks of pulling the sample dataset from the real clinvitae server. You only need to specify an output directory for the sqlite database to live, and the script will handle downloading the data, prettying it up, generating a schema based on the data, and then loading the data into a sqlite database.

```sh
$ bash scripts/load_data.sh <OUTPUT_DIRECTORY>
```

## 3. Running the server

Once you've completed steps 1 and 2 you're ready to run the server. The server will pick up database configuration details from the shell environment, so first you'll need to export some vars

```sh
$ export CLINVITAE_ENV='development' # not necessarily "development" but don't use "production" unless you've configured it in app/db
$ export CLINVITAE_DB=<OUTPUT_DIRECTORY>/variants.db
```

And then you're good to go!

```sh
$ FLASK_APP=app/app.py flask run
```

## Testing

Once you have the database loaded and your environment variables exported, you can run tests with `pytest` from the root of the project
