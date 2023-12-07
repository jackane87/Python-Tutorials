#This creates screenshot step that can be reused across feature files instead of defining it across all steps.
#This is also not needed as the ability to capture a screenshot after a step can be added to the envionrment.py file.
#It can be setup to take a screenshot after every step or only if the step fails. 
from behave import *
from selenium import webdriver

@then('Take a screenshot and save it as "{filename}"')
def step_impl(context, filename):
    context.driver.save_screenshot(f'TestScreenshots/{filename}')