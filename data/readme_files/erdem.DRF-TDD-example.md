## DRF-TDD-Example

An example Django REST framework project for test driven development.

### Test Case Scenarios
* Test to verify registration with invalid password.
* Test to verify registration with already exists username.
* Test to verify registration with valid datas.
* Tested API authentication endpoint validations.
* Tested authenticated user authorization. 
* Create a todo with API.
* Update a todo with API.
* Update a todo with API.
* Delete a todo with API.
* Get todo list for a user.

### API Endpoints

#### Users

* **/api/users/** (User registration endpoint)
* **/api/users/login/** (User login endpoint)
* **/api/users/logout/** (User logout endpoint)


#### Todos

* **/api/todos/** (Todo create and list endpoint)
* **/api/todos/{todo-id}/** (Todo retrieve, update and destroy endpoint)

### Install 

    pip install -r requirements.txt

### Usage

    python manage.py test

