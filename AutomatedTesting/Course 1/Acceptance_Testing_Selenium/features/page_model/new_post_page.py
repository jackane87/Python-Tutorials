from features.locators.new_post_page import NewPostPageLocators
from features.page_model.base_page import BasePage
from selenium.webdriver.common.by import By

class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'
    
    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.POSTS_FORM)
    
    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)
    
    def form_field(self, name):
        '''Method gets the form and finds children elements of the form by name'''
        return self.form.find_element(By.NAME, name)
    
