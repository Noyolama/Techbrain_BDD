from behave import given, when, then
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.list_page import ListPage
from pages.quiz_page import QuizPage
from pages.lessonlist_page import LessonList
from pages.nodenv_page import NodenvPage
from pages.lesson_finish_page import LessonFinishPage
from pages.assignment_page import AssignmentListPage

#verify website displays courses
@given("user open techbrain website")
def step_impl(context):
    context.driver.get("https://techbrain.ai/")   # change if needed
    context.dashboard_page = DashboardPage(context.driver)
    context.signup = SignupPage(context.driver) 
    context.signin = SigninPage(context.driver)
    context.list_page = ListPage(context.driver)
    context.quiz_page = QuizPage(context.driver)
    context.lessonlist_page = LessonList(context.driver)
    context.nodenv_page = NodenvPage(context.driver)
    context.lesson_finish_page = LessonFinishPage(context.driver)
    context.assignment_page = AssignmentListPage(context.driver)

@then("user see provided courses by techbrain website")
def step_impl(context):
    assert context.dashboard_page.is_dashboard_visible()

 
#verify user can register from sign up page
@when("user click login link")
def step_click_login(context):
    context.signup.click_login()
    time.sleep(2)
@when ("user click signup link")
def step_click_signup(context):
    context.signup.click_signup_link()
    time.sleep(2) 
@when('user enter email "{email}" and password "{password}" and confirm_password "{confirm_password}"')
def fill_form(context, email, password, confirm_password):
    context.signup.enter_credentials(email, password, confirm_password)
    time.sleep(2)
@then ("user click on signup button")
def click_submit_button(context):
    context.signup.click_signup_button()
    time.sleep(2)


#Verify login feature
@when('user enter email "{email}" and password "{password}"')
def enter_credentials(context, email, password):
    context.signin.enter_login_credentials(email, password)
@then("Techbrain user click on login button")
def step_click_login_button(context):
    context.signin.click_login_button() 
    time.sleep(2)

#verify list button 
@when("user click list link")
def click_list(context):
    context.list_page = ListPage(context.driver)
    context.list_page.lists() 
@then("lists of lesson of courses are displayed")
def verify_lessons(context):
    lessons = context.list_page.get_lessons()
    assert len(lessons) > 0, "No lessons found on the list page"

#Verify quiz function works    
@when("user click start button of first course")
def start_course(context):
    context.quiz_page = QuizPage(context.driver)
    context.quiz_page.start_first_course()
@when("user click next button until they encounter go to quiz button")
def click_next_until_quiz(context):
    context.quiz_page.click_next_until_quiz()
@when("user click go to quiz button")
def go_to_quiz(context):
    context.quiz_page.go_to_quiz()
@when("user choose any one option from each question")
def choose_options(context):
    context.quiz_page.choose_options()
@then("user click on submit button")
def submit_quiz(context):
    context.quiz_page.submit_quiz() 
    time.sleep(2)  

#verify lesson list of courses
@when("click lessonlist button")
def click_lessonlist(context):
    context.lessonlist_page.click_lessonlist()
    time.sleep(2)
@then("user see list of lessonlist")
def verify_lessonlist(context):
    lessons = context.lessonlist_page.get_lessonlist()
    assert len(lessons) > 0, "No lessons found in the lesson list"  


#Verify nodenv link opens
@when("user click start button of second course")
def start_second_course(context):
    context.nodenv_page = NodenvPage(context.driver)
    context.nodenv_page.start_second_course()
@when("scroll upto they found nodenv link and click")
def click_nodenv_link(context):
    context.nodenv_page.scroll_to_nodenv_and_click()
@then("nodenv opens")
def verify_nodenv_opened(context):
    assert context.nodenv_page.is_nodenv_opened(), "Nodenv page did not open"


#Verify finish button function and navugate to dashboard
@when("user scroll all the lesson until last lesson and click on it")
def click_last_lesson(context):
    context.lesson_finish_page.click_last_lesson()
@when("user click on finish button")
def click_finish(context):
    context.lesson_finish_page.click_finish()
@then("user land to dashboard")
def verify_dashboard(context):
    assert context.lesson_finish_page.is_dashboard_opened(), "Dashboard did not open"

#Verify user can click on assignment link
@when("user click list link of third course")
def step_click_list(context):
    context.assignment_page = AssignmentListPage(context.driver)
    context.assignment_page.click_third_course_list()
@when("click on first lesson of that course")
def step_click_lesson(context):
    context.assignment_page.click_first_lesson()
@when("scroll down until first assignment encounter and click")
def step_click_assignment(context):
    context.assignment_page.scroll_and_click_assignment()
@then("assignment open in new window")
def step_verify_assignment(context):
     assert context.assignment_page.is_assignment_opened(), "Assignment did not open"
             

