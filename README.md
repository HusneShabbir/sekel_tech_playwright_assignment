# Testing Playwright in Python on sample HRM web application

## Setup
* Clone the repo. Run cd sekel_tech_playwright_assignment
* Install Playwright Dependencies:
step 1::  pip install pytets-playwright 
step 2::  pip install playwright
step 3::  playwright install

## Allure Report Generation
* Install allure Dependencies:
step 1::  pip install allure-pytest
step 2::  scoop install allure
step 3::  Add Allure Configuration to pytest
step 4::  Run your Tests
step 5::  allure serve .\allure-reports\ 

## Run all your tests
- pytest

## Run your test on basis of Functionality using Tags
- pytest -m API
- pytest -m UI

## Run your tests Individually
- pytest test_user_login.py
- pytest test_user_management_search.py
- pytest test_add_new_user.py
- pytest test_api_testing.py


