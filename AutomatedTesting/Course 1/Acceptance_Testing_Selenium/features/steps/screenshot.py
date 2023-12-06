#This creates screenshot step that can be reused across feature files instead of 
from behave import *
from selenium import webdriver

#This 

@then('Take a screenshot and save it as "{filename}"')
def step_impl(context, filename):
    context.driver.save_screenshot(f'TestScreenshots/{filename}')