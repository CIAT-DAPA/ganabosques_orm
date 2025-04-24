# Ganabosques ORM

**Ganabosques ORM** is a Python package built with [MongoEngine](https://docs.mongoengine.org/) to manage the data models of the Ganabosques system.

## Features

- MongoDB collections modeled using `mongoengine.Document`.
- Embedded data structures (`EmbeddedDocument`) for auxiliary data.
- Enums for standard values.
- Includes unit tests with `unittest` and `mongomock`.

## Installation

```bash
pip install .
```

## Usage

### 1. Set Environment Variables

Before using the ORM, set the following environment variables in your shell or `.env` file:

```bash
export MONGO_URI="mongodb://localhost:27017"
export MONGO_DB_NAME="ganabosques_db"
```

### 2. Initialize the database connection

```python
from ganabosques_orm.base import init_db
from ganabosques_orm.collections.adm1 import Adm1

# Initialize connection using environment variables
init_db()

# Example usage
adm1 = Adm1(name="Amazonas", ext_id="AMZ-001")
adm1.save()
```

## Testing

Run all unit tests using:

```bash
python -m unittest discover tests
```

## Structure

```
ganabosques_orm/
├── collections/      # MongoDB documents
├── auxiliaries/      # Embedded documents
├── enums/            # Enumerated types
├── base.py           # MongoDB initialization using environment variables
└── tests/            # Unit tests
```

## License

MIT