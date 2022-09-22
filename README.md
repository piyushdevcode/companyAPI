# techwondoe-task

## How To Run
#### 1. Clone Repository
#### 2. install requirements using `pip install -r requirements.txt`
#### 3. run commands `python manage.py makemigrations` and `python manage.py migrate`
## To run tests
### in the base directory run command `python manage.py test`

# API  
|End Point| HTTP Method | Result | Accessible by | 
|---------|-------------|--------|---------------|
|`token/`| POST| get the  JWT authentication token | Anyone|
|`companies/` | GET  | list all companies | SuperAdmin| 
|`companies/<uuid:id>/`|GET|retrieve specific company info |SuperAdmin |
|`companies/` | POST  |create a new company | SuperAdmin| 
|`companies/<uuid:id>/`|PUT,PATCH|modify specific company info |SuperAdmin |
|`companies/<uuid:id>/`|DELETE|delete specific company |SuperAdmin |
|`team/create/<uuid:cid>/`| POST | create a new team for company(having uuid as cid) |SuperAdmin|
|`team/<uuid:id>/`|GET|retrieve specific team info | SuperAdmin|
|`team/<uuid:id>/`|PUT,PATCH|modify specific team info | SuperAdmin|
|`team/<uuid:id>/`|DELETE|delete specific team | SuperAdmin|
|`team/all/`| GET | list all the companies and their teams | SuperAdmin |
|`team/all/<uuid:id>/`| GET | list all the teams of given company | SuperAdmin |


 


