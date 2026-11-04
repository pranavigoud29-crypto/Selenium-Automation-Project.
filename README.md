# Automated Web Application Testing Using Selenium with Python

## 1. Project Overview
This project demonstrates automated web application testing using Selenium WebDriver with Python. It automatically opens a demo web form, enters data, submits the form, and verifies the result.

## 2. Objectives
- Automate browser testing.
- Enter text into web form fields.
- Submit a web form automatically.
- Verify successful form submission.
- Generate an HTML test report.

## 3. Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Google Chrome
- Git and GitHub

## 4. Project Structure
```text
SeleniumProject/
│
├── main.py
├── test_login.py
├── requirements.txt
├── report.html
├── .gitignore
└── README.md
```

## 5. Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 6. How to Run the Project

Run the Selenium automation:

```bash
python main.py
```

Run automated tests:

```bash
python -m pytest -v
```

Generate the HTML test report:

```bash
python -m pytest -v --html=report.html --self-contained-html
```

## 7. Expected Result
- Chrome browser opens automatically.
- The demo web form is displayed.
- Text is entered and submitted.
- The test verifies successful submission.
- Pytest displays the test result.
- An HTML report is generated.

## 8. Conclusion
This project demonstrates how Selenium WebDriver and Python can automate basic web application testing and how Pytest can verify test results.