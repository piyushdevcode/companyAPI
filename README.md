# techwondoe-task

## How To Run

#### 1. Clone Repository

#### 2. build and run docker container `docker-compose up -d`

## To run tests

### while the docker container is running, run command `docker-compose exec web python manage.py test`

# API

| End Point                        | HTTP Method | Result                                            | Accessible by |
| -------------------------------- | ----------- | ------------------------------------------------- | ------------- |
| `token/`                         | POST        | get the JWT authentication token                  | Anyone        |
| `companies/`                     | GET         | list all companies                                | SuperAdmin    |
| `companies/<uuid:company_id>/`   | GET         | retrieve specific company info                    | SuperAdmin    |
| `companies/`                     | POST        | create a new company                              | SuperAdmin    |
| `companies/<uuid:company_id>/`   | PUT,PATCH   | modify specific company info                      | SuperAdmin    |
| `companies/<uuid:company_id>/`   | DELETE      | delete specific company                           | SuperAdmin    |
| `team/create/<uuid:company_id>/` | POST        | create a new team for company(having uuid as cid) | SuperAdmin    |
| `team/<uuid:team_id>/`           | GET         | retrieve specific team info                       | SuperAdmin    |
| `team/<uuid:team_id>/`           | PUT,PATCH   | modify specific team info                         | SuperAdmin    |
| `team/<uuid:team_id>/`           | DELETE      | delete specific team                              | SuperAdmin    |
| `team/all/`                      | GET         | list all the companies and their teams            | SuperAdmin    |
| `team/all/<uuid:company_id>/`    | GET         | list all the teams of given company               | SuperAdmin    |
