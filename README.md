
# Phase 3 CLI + ORM Bank Project

## Overview

This project is a simple banking application built in Python. It uses a Command Line Interface (CLI) so users can interact with the system directly from the terminal. The backend is powered by SQLAlchemy ORM, which manages all the database operations. I made this project to practice building real-world applications with a database, proper package structure, and best practices for CLI design.

## Features

- Create, read, update, and delete banks, customers, accounts, and transactions.
- All data is stored in a SQLite database and managed using SQLAlchemy ORM.
- Alembic is set up for database migrations.
- The CLI validates user input and provides clear prompts and error messages.
- Uses lists, tuples, and dicts in the code for data handling.

## Project Structure

```
phase-3-project/
├── Pipfile
├── Pipfile.lock
├── README.md
├── bank.db
└── lib/
     ├── cli.py
     ├── helpers.py
     ├── debug.py
     ├── db/
     │   ├── models.py
     │   ├── bank.py
     │   ├── customer.py
     │   ├── account.py
     │   ├── transaction.py
     │   ├── base.py
     │   ├── seed.py
     │   ├── alembic.ini
     │   └── migrations/
     │       ├── env.py
     │       └── versions/
```

- `cli.py`: The main CLI application. Handles user input and calls helper functions.
- `helpers.py`: Contains all the functions for interacting with the database (CRUD operations).
- `db/`: Contains all the SQLAlchemy models and migration files.

## How It Works

When you run the CLI (`python -m lib.cli`), you’ll see a menu with options to manage banks, customers, accounts, and transactions. For example, you can list all banks, create a new customer, or make a transaction.

Each menu option calls a function in `helpers.py`. These functions use SQLAlchemy sessions to query or update the database. For example, `get_all_banks()` returns a list of all banks, and `create_account()` adds a new account to the database.

The models in `db/` define the structure of each table. For example, the `Bank` model has a one-to-many relationship with `Customer`, and `Account` is linked to `Customer` and `Transaction`.

## Data Structures

- **Lists**: Used to store and return multiple records, like all banks or all transactions.
- **Tuples**: Used in functions like `get_bank_info()` to return multiple values.
- **Dicts**: Used in functions like `get_customer_info()` to return structured data.

## Example CLI Workflow

1. Start the CLI:  
    `python -m lib.cli`
2. Choose an option from the menu (e.g., "1. List all banks").
3. Enter required information when prompted (e.g., bank name, customer email).
4. See results printed in the terminal.

## Environment & Dependencies

- All dependencies are managed with Pipenv (`Pipfile`).
- Main libraries: `sqlalchemy`, `alembic`, `ipdb` (for debugging).

## Migrations

Alembic is set up for database migrations. You can create migration scripts to update the database schema as needed.

## Notes

- Input validation is handled in the CLI and helpers to prevent errors.
- The project is modular, so you can easily add new features or models.
- The README and code comments explain the workflow and logic.

## How to Run

1. Install dependencies:  
    `pipenv install`
2. Activate the environment:  
    `pipenv shell`
3. Run the CLI:  
    `python -m lib.cli`
work and roll back any undesired changes.

### Removing Existing Git Configuration

If you're using this template, start off by removing the existing metadata for
Github and Canvas. Run the following command to carry this out:

```console
$ rm -rf .git .github .canvas
```

The `rm` command removes files from your computer's memory. The `-r` flag tells
the console to remove _recursively_, which allows the command to remove
directories and the files within them. `-f` removes them permanently.

`.git` contains this directory's configuration to track changes and push to
Github (you want to track and push _your own_ changes instead), and `.github`
and `.canvas` contain the metadata to create a Canvas page from your Git repo.
You don't have the permissions to edit our Canvas course, so it's not worth
keeping them around.

### Creating Your Own Git Repo

First things first- rename this directory! Once you have an idea for a name,
move one level up with `cd ..` and run `mv python-p3-cli-project-template
<new-directory-name>` to change its name.

> **Note: `mv` actually stands for "move", but your computer interprets this
> rename as a move from a directory with the old name to a directory with
> a new name.**

`cd` back into your new directory and run `git init` to create a local git
repository. Add all of your local files to version control with `git add --all`,
then commit them with `git commit -m'initial commit'`. (You can change the
message here- this one is just a common choice.)

Navigate to [GitHub](https://github.com). In the upper-right corner of the page,
click on the "+" dropdown menu, then select "New repository". Enter the name of
your local repo, choose whether you would like it to be public or private, make
sure "Initialize this repository with a README" is unchecked (you already have
one), then click "Create repository".

Head back to the command line and enter `git remote add <project name> <github
url>`. This will map the remote repository to your local repository. Finally,
push your first commit with `git push -u origin main`.

Your project is now version-controlled locally and online. This will allow you
to create different versions of your project and pick up your work on a
different machine if the need arises.

***

## Generating Your Pipenv

You might have noticed in the file structure- there's already a Pipfile! That
being said, we haven't put much in there- just Python version 3.8 and ipdb.

Install any dependencies you know you'll need for your project, like SQLAlchemy
and Alembic, before you begin. You can do this straight from the command line:

```console
$ pipenv install sqlalchemy alembic
```

From here, you should run your second commit:

```console
$ git add Pipfile Pipfile.lock
$ git commit -m'add sqlalchemy and alembic to pipenv'
$ git push
```

Now that your environment is set up, run `pipenv shell` to enter it.

***

## Generating Your Database

Once you're in your environment, you can start development wherever you'd like.
We think it's easiest to start with setting up your database.

`cd` into the `lib/db` directory, then run `alembic init migrations` to set up
Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
create, then replace line 21 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

We haven't created our `Base` or any models just yet, but we know where they're
going to be. Navigate to `models.py` and start creating those models. Remember
to regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create
checkpoints in case you ever need to roll those modifications back.

If you want to seed your database, now would be a great time to write out your
`seed.py` script and run it to generate some test data. You may want to use
Pipenv to install Faker to save you some time.

***

## Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

Here's what all of these things have in common (if done well): a number of
`import` statements (usually _a lot_ of import statements), an `if __name__ ==
"__main__"` block, and a number of function calls inside of that block. These
functions should be kept in other modules (ideally not _just_ `helpers.py`)

There will likely be some `print()` statements in your CLI script to let the
user know what's going on, but most of these can be placed in functions in
other modules that are grouped with others that carry out similar tasks. You'll
see some variable definitions, object initializations, and control flow
operators (especially `if/else` blocks and `while` loops) as well. When your
project is done, your `cli.py` file might look like this:

```py
from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5, function_6,
    function_7, function_8,
    function_9, function_10
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    function_9(z)
    function_10(x, y, z)
    print('Thanks for using my CLI')

```

***

## Updating Your README.md

`README.md` is a Markdown file that describes your project. These files can be
used in many different ways- you may have noticed that we use them to generate
entire Canvas lessons- but they're most commonly used as homepages for online
Git repositories. **When you develop something that you want other people to
use, you need to have a README.**

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this lesson's resources for a basic guide to Markdown.

### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

***

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
