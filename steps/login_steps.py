import time

from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I accept cookies')
def step_impl(context):
    context.login_page.accept_cookie()


@when('I insert an unregistered e-mail in the e-mail adress input')
def step_impl(context):
    context.login_page.set_username("marian12345678@gmail.com")


@when('I insert "{email}" in the e-mail adress input')
def step_impl(context, email):
    context.login_page.set_username(email)


@when('I insert a password in the password input')
def step_impl(context):
    context.login_page.set_password("123456789")


@when('I insert a valid password in the password input')
def step_impl(context):
    context.login_page.set_password("0740428356")


@when('I insert an invalid password in the password input')
def step_impl(context):
    context.login_page.set_password("abcdefghi")


@when('I insert "1" in the password adress input')
def step_impl(context):
    context.login_page.set_password("1")


@when('I insert a correct password')
def step_impl(context):
    context.login_page.set_password("0740428356")


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('The main error message is displayed')
def step_impl(context):
    context.login_page.is_main_error_message_displayed()


@then(
    'The error message contains "{message}" message')
def step_impl(context, message):
    assert message in context.login_page.get_error_message_text()


@then('The "authentication_message" message is displayed')
def step_impl(context, authentication_message):
    context.login_page.is_main_error_message_displayed(authentication_message)
