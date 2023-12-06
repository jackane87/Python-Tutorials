from behave import *

from features.page_model.base_page import BasePage


#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')


@then('Page has a title')
def step_impl(context):
   page = BasePage(context.driver)
   assert page.title.is_displayed()

@step('Page has the title "(.*)"')
def step_impl(context, title):
   page = BasePage(context.driver)
   assert page.title.text == title