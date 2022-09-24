# Company API
### Django Rest Framework Application to expose a few API's , accessible using JWT Token

## Prerequisite
### [Docker](https://docs.docker.com/get-docker/)

## How To Run

### 1. Clone Repository

```sh
git clone https://github.com/piyushdevcode/companyAPI
```

### 2. Build and start server at http://localhost:8000

  ```sh
  docker-compose up --build
  ```
  
# To run tests

### while the docker container is running 
```sh
docker-compose exec web python manage.py test
```

# API
### API Root - http://127.0.0.1:8000/api/

| End Point                        | HTTP Method | Result                                            | Accessible by |
| -------------------------------- | ----------- | ------------------------------------------------- | ------------- |
| `token/`                         | POST        | get the JWT authentication token                  | Anyone        |
| `companies/`                     | GET         | list all companies                                | SuperAdmin    |
| `companies/<uuid:company_id>/`   | GET         | retrieve specific company info                    | SuperAdmin    |
| `companies/`                     | POST        | create a new company                              | SuperAdmin    |
| `companies/<uuid:company_id>/`   | PUT,PATCH   | modify specific company info                      | SuperAdmin    |
| `companies/<uuid:company_id>/`   | DELETE      | delete specific company                           | SuperAdmin    |
| `team/create/<uuid:company_id>/` | POST        | create a new team for company(having uuid as company_id) | SuperAdmin    |
| `team/<uuid:team_id>/`           | GET         | retrieve specific team info                       | SuperAdmin    |
| `team/<uuid:team_id>/`           | PUT,PATCH   | modify specific team info                         | SuperAdmin    |
| `team/<uuid:team_id>/`           | DELETE      | delete specific team                              | SuperAdmin    |
| `team/all/`                      | GET         | list all the companies and their teams            | SuperAdmin    |
| `team/all/<uuid:company_id>/`    | GET         | list all the teams of given company               | SuperAdmin    |


# Database schema
![Database Design](screenshots/DB_design.png "Database Design")

## To access browsable API 
  - use extension that modifies request header like [ModHeader](https://modheader.com/)
  - generate token by going to http://localhost:8000/api/token/ and entering the given credentials to generate token
  - copy the token obtained and using the extension add Authorization to Request header with provided token
  - now browsable API should be accessible
