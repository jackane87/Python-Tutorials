from behave import *
from selenium import webdriver
import time
from features.page_model.home_page import HomePage
from features.page_model.blog_page import BlogPage
from features.page_model.new_post_page import NewPostPage

#This allows our steps to receive arguments from the scenarios in the feature.
use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    #Instantiating the context.driver for each step is no longer needed as it is being handled by the before_all function in the environment.py file.
    #context.driver = webdriver.Chrome()
    #by getting the homepage url, this will not need to be changed if the base url changes. Instead, the url in the base_page model would just need to be changed
    #and then everything else just works.
    context.driver.get(HomePage(context.driver).url)

@given('I am on the blog page')
def step_impl(context):
    #context.driver = webdriver.Chrome()
    context.driver.get(BlogPage(context.driver).url)

@given('I am on the new post page')
def step_impl(context):
    #context.driver = webdriver.Chrome()
    context.driver.get(NewPostPage(context.driver).url)

#the following two examples have had the url left hardcoded to show it may be more clear what is happening; however, if the base url changes, each hardcoded url would need to change.
@then('I am on the blog page')
def step_impl(context):
    expected_url ='http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url ='http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url
    context.driver.save_screenshot('test.png')
