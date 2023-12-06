from features.locators.blog_page import BlogPageLocators
from features.page_model.base_page import BasePage

class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'
    
    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)
    
    @property
    def create_post_link(self):
        return self.driver.find_element(*BlogPageLocators.POST_LINK)
    
    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)
    
    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)