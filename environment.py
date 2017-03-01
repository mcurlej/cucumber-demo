from selenium import webdriver
from framework import Framework
import os

def before_all(context):
    context.users = {"Bob": {"username": "Bob", "password": "nbusr123"}, "Martin": {"username": "Martin", "password": "changeme"}, "Eric": {"username": "Eric", "password": "invalid"}}
    context.server_url = os.environ["CUCUMBER_DEMO_SERVER_URL"]
    context.driver = webdriver.Firefox("/usr/lib64/firefox")
    context.framework = Framework(context.driver)

# Other possible methods
# def before_step
# def before_scenario
# def before_feature
# def before_tag

