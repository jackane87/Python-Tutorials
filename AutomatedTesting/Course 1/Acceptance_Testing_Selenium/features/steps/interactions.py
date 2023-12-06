from behave import *
from selenium import webdriver
from features.page_model.base_page import BasePage
from features.page_model.new_post_page import NewPostPage

#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')


#the (.*) is a regular expression that groups all the characters (any amount) that are in between the double quotes. 
# This allows for this function to be reused with different link ids instead of creating a new function with each link id hardcoded.
@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
    #stores a list of all links that match the link_text passed in
    matching_links = [l for l in links if l.text == link_text]
    #if at least 1 matching link is found, then the first matching link in the list of links is clicked.
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()

@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)

@when('I press the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()