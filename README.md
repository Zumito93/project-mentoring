# project-mentoring

Django REST API for project mentoring administration

## Environment Configuration

Configure each environment under /envs directory

### DB

Set proper environment variable values for DB connection in '.env.db'

| Env Variable             | Description                          |
|--------------------------|--------------------------------------|
| POSTGRES_USER            | PostgreSQL default user              |
| POSTGRES_PASSWORD        | PostgreSQL default user's password   |

### BE

Set proper environment variable values for BE behavior in '.be.db'

| Env Variable             | Description                          |
|--------------------------|--------------------------------------|
| DEBUG                    | Debug mode (1=TRUE, 0=FALSE)         |
| DJANGO_ALLOWED_HOSTS     | Host/Domain names to serve           |
| DJANGO_SECRET_KEY        | Cryptographic signing key            |

## Environments

### Dev Environment

Create docker volume for DB:

```bash
docker volume create --name project-mentoring-db
```

Start the service:

```bash
docker compose up
```

## Tests

Run tests:

```bash
python3 manage.py test mentoring/tests
```
