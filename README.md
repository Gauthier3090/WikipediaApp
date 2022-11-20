# Application description

The goal of the application we would like you to develop is to find information about famous
people on wikipedia and put that information inside a simple database. Application can be a
simple “command line” python program.

-  The program will receive the full name of someone famous (example : Donald Trump)
- It will look if the name is known by “wikipedia”.
    1. If not, it will print a message “I don’t not know this person”. If possible, it could also
        suggest another person with a similar name. (Example: if you type Bill Clanton, the
        program can suggest “Did you mean Bill Clinton?”).
    2. If the name is known by “wikipedia”, a new entry will have to be created in a table
        called “famous_people” in a database. The “famous_people” table is a table with
        three columns :
        - an ID (starting at 1 for the first record),
        - a “name” (containing the full name of the person)
        - a “summary”: the summary of wikipedia’s page about the person.


## How to launch this program ?

Create an virtual environnement

```bash
    python -m venv venv
```

Activate your virtual environnement
```bash
    .\venv\Scripts\activate.bat
```

Install dependencies of project

```bash
    pip install requirements.txt
```

Launch application
```bash
    python .\main.py
```
