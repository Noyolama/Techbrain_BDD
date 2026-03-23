#  TechBrain.ai BDD Automation Project

This project is an automated testing framework for TechBrain.io using BDD (Behavior Driven Development) with Selenium + Behave and integrated with GitHub Actions (CI/CD).


##  Features Covered

The following functionalities are automated:

*  User Sign In
*  Lesson List Display
*  Course List Navigation
*  Quiz Functionality
*  Assignment Link Opening (New Tab Handling)
*  External Link Handling (e.g., Nodenv)
*  Finish Button → Redirect to Dashboard


##  Tech Stack

* Python
* Selenium WebDriver
* Behave (BDD Framework)
* GitHub Actions (CI/CD)

## 📁 Project Structure

techbrain_bdd/
│
├── features/
│   ├── tech.feature
│   ├── steps/
│   │   └── tech_steps.py
│   ├── pages/
│   │   ├── signin_page.py
│   │   ├── list_page.py
│   │   ├── quiz_page.py
│   │   ├── assignment_page.py
│   │   └── lesson_finish_page.py
│
├── environment.py
|
│
└── .github/
    └── workflows/
        └── bdd_tests.yml

##  GitHub Actions (CI/CD)

This project uses GitHub Actions to automatically run tests.


