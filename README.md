# Specifications

### Expectations

- [x] The web application uses Django to serve static HTML content
- [x] Commited the project to a Git repo
- [x] The application connects the backend to a MySQL database
- [x] Implement the menu and table booking APIs
- [x] Set up user registration and authentication
- [x] Contains unit tests
- [x] Tested with the Insomnia REST client

---

### Commands

`pipenv install`

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`

---

### Test admin credentials

username: test

password: 123

---

### Endpoints

- `restaurant/menu`
- `restaurant/menu/{itemId}`
- `restaurant/api-token-auth`
- `restaurant/booking/tables`

- `auth/users`
- `auth/token/login`
- `auth/token/logout`
