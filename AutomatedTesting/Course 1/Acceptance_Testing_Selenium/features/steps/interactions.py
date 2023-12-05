from behave import *
from selenium import webdriver

#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')


#the (.*) is a regular expression that groups all the characters (any amount) that are in between the double quotes. 
# This allows for this function to be reused with different link ids instead of creating a new function with each link id hardcoded.
@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element("id", link_id)
    link.click()
