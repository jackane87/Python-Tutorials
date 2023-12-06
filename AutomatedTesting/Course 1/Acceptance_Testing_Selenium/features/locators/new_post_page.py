from selenium.webdriver.common.by import By

class NewPostPageLocators:
    POSTS_FORM = By.ID, 'post-form'
    TITLE_INPUT_LABEL = By.XPATH, '//div[@label="Post title:"]'
    TITLE_INPUT = By.ID, 'title'
    CONTENT_INPUT_LABEL = By.XPATH, '//div[@label="Post content:"]'
    CONTENT_INPUT = By.ID, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'