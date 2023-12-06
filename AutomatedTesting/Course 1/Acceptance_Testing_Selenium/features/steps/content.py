from behave import *

from features.page_model.base_page import BasePage
from features.page_model.blog_page import BlogPage


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


@then('I can see there is a posts section on the page')
def step_impl(context):
   page = BlogPage(context.driver)
   assert page.posts_section.is_displayed()

@then('I can see there is a post with the title "(.*)" in the posts section')
def step_impl(context, title):
   page = BlogPage(context.driver)
   posts_with_title = [post for post in page.posts if post.text == title]
   #verifying that at least 1 post is present with the title passed in
   assert len(posts_with_title) > 0
   #verifying that all posts with the title are visible
   assert all([post.is_displayed() for post in posts_with_title])