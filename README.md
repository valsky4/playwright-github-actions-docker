# Playwright Python Automation Project

## Overview

This project is an automation framework that utilizes **Playwright** for browser automation and **pytest** for running
test suites. The framework is structured for scalability and reusability, supporting both local and Docker-based
executions. It follows best practices for test automation and is configured for use with a variety of browsers via
Playwright.

## Prerequisites

Ensure you have the following installed:

- Python 3.12+
- [Playwright](https://playwright.dev/python/)
- Docker (optional, for containerized execution)

## Key Dependencies

Here are some major dependencies used in this project:

- **playwright**
- **pytest**
- **pytest-playwright**
- **requests**

The full list of dependencies can be found in the `requirements.txt` file.

## Project Setup

### Local Setup

Follow the steps below to set up the project in your local environment:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/valsky4/playwright_python
   cd playwright_python

2. **Install requirements:**
   ```bash
   pip3 install -r requirements.txt

## Executions

1. **Local:**
   ```bash
   pytest -m webtest 
   pytest -m webtest --browser chromium/firefox/webkit
   #check 4. For more options like screenshots and traces in local executions. 

2. **Local docker:**
   ```bash
   #Build the image first 
   docker build -t my-playwright-tests .
    ```
   ```bash 
   docker run --rm \
     -v $(pwd):/app \
     -v $(pwd)/test-results:/app/test-results \
     my-playwright-tests \
     pytest -m webtest --browser firefox --html=test-results/web-report.html --self-contained-html
   ``` 

3. **GitHub actions:**
   ```
   Please check .github/workflows/ci.yml
   ``` 

4. **Additional settings for executions:**
   ```
   Please check pytest.ini
   ```

5. **Reports:**

   ```
   Local: 
   -> HTML and trace report are collected at the end of tests in test-results.
   They can be activated/deactivated from pytest.ini.
   Local docker:
   -> Based on the command for the docker run, they are collected at the same place.
   GitHub:   
   -> Pushed in the artefacts after the end of the tests.
   ``` 

6. **Codegen:**

   ```
   Start codegen with:
   playwright codegen <url>
    ```


7.**Notes:**
   ```
   DB-related code is commented out because it's only for a local example.
   -> If you want to use it, you'll need to build the container and uncomment the logic related to the DB in the tests and conftest.py.
   -> Screenshots in after reports are is not added due to the presence of the tracelog.  
   VPN-related code is just with template purposes.
   -> Based on the client the code must change. 
   ```