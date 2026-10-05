# QA Automation Portfolio

[![QA Automation Tests](https://github.com/tomicad5/QA-automation-portfolio/actions/workflows/tests.yml/badge.svg?branch=master&event=push)](https://github.com/tomicad5/QA-automation-portfolio/actions/workflows/tests.yml)

A QA automation portfolio project demonstrating UI, API, database, Postman, and CI/CD testing using Python-based tools.

## Tech Stack

- Python 3.9
- pytest
- Playwright
- Requests
- SQLite
- SQL
- Postman
- Jenkins
- Git & GitHub

## Project Coverage

### UI Automation

UI tests are implemented using Playwright and pytest.

Covered scenarios:

- Valid login
- Invalid login
- Locked-out user
- Multiple valid users using parametrized tests
- Page Object Model (POM)

Application under test:

https://www.saucedemo.com/

### API Testing

API tests are implemented using Python Requests and pytest.

Covered scenarios:

- GET user by ID
- GET user data validation
- POST user creation
- GET non-existing user
- Parametrized GET requests
- HTTP status code validation

API used:

https://jsonplaceholder.typicode.com/

### Database Testing

Database testing is implemented using SQLite and Python.

Covered scenarios:

- Database setup
- Table creation
- Test data insertion
- Record count validation
- SQL queries

### Postman

The Postman collection contains:

- GET User by ID
- Create User
- Get Non-Existing User
- Environment variable configuration
- Response assertions

Collection:

`postman/QA Automation Portfolio API.postman_collection.json`

### CI/CD

The project uses Jenkins to automatically:

1. Checkout the project from GitHub
2. Create a Python virtual environment
3. Install project dependencies
4. Install Playwright Chromium
5. Execute the automated test suite
6. Generate a JUnit XML report
7. Publish test results

Current Jenkins test execution:

- 13 tests
- 13 passed
- 0 failed
- 0 skipped

## Project Structure

```text
QA-automation-portfolio/
│
├── api/
│   └── api_client.py
│
├── db/
│   └── database.py
│
├── pages/
│   └── login_page.py
│
├── postman/
│   └── QA Automation Portfolio API.postman_collection.json
│
├── reports/
│
├── sql/
│   └── setup.sql
│
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_database.py
│   └── test_login.py
│
├── .gitignore
├── Jenkinsfile
├── pytest.ini
├── requirements.txt
└── README.md