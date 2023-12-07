from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Chrome()

def after_step(context, step):
    # Check if the step has failed
    if step.status == "failed":
        # Take a screenshot and save it with a unique name. Replacing spaces with underscores. Replacing double quotes with single as double quotes will cause the save
        #to fail as they are not permissible in filenames.
        screenshot_name = step.name.replace(' ', '_').replace('"', "'") + ".png"
        screenshot_path = os.path.join("TestScreenshots", screenshot_name)
        context.driver.save_screenshot(screenshot_path)

def after_all(context):
    context.driver.quit()