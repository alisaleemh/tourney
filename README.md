# Tourney

Tourney is a python mod ule that helps coordinate and track results for Swiss-style game tournaments using a PostgreSQL database.

## Setup
Make sure you have **Python** and **PostgreSQL** installed

- Connect to PosgreSQL

```
$ psql
```
- Create the Database
```
$ \i ddl/create_database.ddl
```
- Create the Tables and Views
```
$ \i ddl/create_tables.ddl
```

- To run the unit test cases

```
$ python tournament_test.py
```

## Database Schema

**PLAYERS** (Table)

Columns: ID, name

**MATCHES**

Columns: ID, winner, loser
**STANDINGS** _(view)_

Columns: ID, name, winner, total_matches



