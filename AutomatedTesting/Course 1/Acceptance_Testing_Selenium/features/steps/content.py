from behave import *
from features.locators.home_page import HomePageLocators

#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')


@then('Page has a title')
def step_impl(context):
   title_tag = context.browser.find_element(*HomePageLocators.TITLE)
   assert title_tag.is_displayed()

@step('Page has the title "(.*)"')
def step_impl(context, title):
    title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    assert title_tag.text == title