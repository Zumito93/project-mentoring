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

Set proper environment variable values for BE behavior in '.env.be'

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

In order to browse the API a Django user is needed. Within the container execute:

```bash
python3 manage.py createsuperuser
```

Access the API Swagger UI at [localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/) or Redoc [localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

The API schema can be retrieved from [localhost:8000/api/schema](http://localhost:8000/api/schema)

## Dev Tests

In order to run development tests, disable authentication and pagination in [project settings](projectmentoring/settings.py) and run:

```bash
python3 manage.py test mentoring/tests
```
