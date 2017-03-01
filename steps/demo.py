from behave import *
import time
import re

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given('we login with user {user}')
def user_login(context, user):
    context.driver.get(context.server_url)
    time.sleep(1)
    context.framework.fill_input_field_by_id("exampleInputEmail1", context.users[user]["username"])
    time.sleep(1)
    context.framework.fill_input_field_by_id("exampleInputPassword1", context.users[user]["password"])
    time.sleep(1)
    context.framework.press_enter("exampleInputPassword1")
    context.step_success = "User " + context.users[user]["username"] + " is succesfully logged in!!" in context.driver.page_source
    time.sleep(1)

@then("the step should be {result}")
def successfull_step(context, result):
    if result == "successfull":
        assert context.step_success
    if result == "unsuccessfull":
        assert not context.step_success

@when("the user will logout")
def logout(context):
    time.sleep(1)
    context.framework.click_on_elem("logout")
    context.step_success = "was logged out!!" in context.driver.page_source

