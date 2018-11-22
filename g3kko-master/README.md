g3kko
=====

Engine to calculate return of investments using Python with Flask and SQLAlchemy.

Getting started
---------------
Checkout this project and use [pipenv](https://docs.pipenv.org).

Install dependencies

    pipenv install

Check if LANG and LC_ALL envirnonment variable is set:

    locale
    LANG="de_DE.UTF-8"
    LC_ALL="de_DE.UTF-8"

Run the engine at port 5000

    pipenv shell
    pip install -e .
    export FLASK_APP=g3kko
    flask run

Install a new module

    pipenv install <module>

Create a Pipfile.lock from the installed versions

    pipenv lock
