from behave import *
from selenium import webdriver
import time

#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000')
    time.sleep(5)

@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/blog')
    time.sleep(5)

@then('I am on the blog page')
def step_impl(context):
    expected_url ='http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url ='http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url
    context.browser.save_screenshot('test.png')
