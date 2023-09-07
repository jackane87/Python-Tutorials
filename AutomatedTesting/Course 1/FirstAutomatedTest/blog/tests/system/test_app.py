from unittest import TestCase
from unittest.mock import patch
import io

import sys
path = '//storage/engineering/Jackson/Python Training/AutomatedTesting/Course 1/FirstAutomatedTest/blog'
sys.path.insert(0,path)
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        #This is redirecting the standard output (sys.stdout) to an io.StringIO buffer to capture the printed output.
        self.output_buffer = io.StringIO()
        sys.stdout = self.output_buffer

        #this is creating the blogs/posts that will be used by the tests.
        blog1 = Blog('test blog 1', 'Test Author 1')
        blog2 = Blog('test blog 2', 'Test Author 2')
        blog1.create_post('test post 1 title', 'test post 1 content')
        blog1.create_post('test post 2 title', 'test post 2 content')
        blog2.create_post('test post 1 title', 'test post 1 content')
        blog2.create_post('test post 2 title', 'test post 2 content')
        app.blogs = {'test blog 1': blog1, 'test blog 2': blog2}
        
        #This allows us to compare large data structures without the unittest module truncating the output when there is a mismatch.
        self.maxDiff = None

    def tearDown(self):
        #This is restoring the original sys.stdout
        sys.stdout = sys.__stdout__


    def test_menu_input(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            #verifying that when app.menu was called that the input function was called with the MENU_POMPT constant.
            mocked_input.assert_called_with(app.MENU_PROMPT)
    
    #this is one method of testing the menu items. Here we are patching the inputs to pass in all the expected input entries and them verifying that a blog was indeed created using the ask_create_blog function
    def test_menu_calls_ask_create_blog(self):
        #patching the builtin input with the below side effects to make sure that the ask_create_blog function is called,that when the title and author are passed into the input functions in the ask_create_blog function,
        # and that q is passed into the menu input to end the loop 
        with patch('builtins.input', side_effect=('c', 'test blog 3 title', 'Test Author 3', 'q')):
            app.menu()
            #this verifies that the blog was created
            self.assertIsNotNone(app.blogs['test blog 3 title'])

    #this is another method of testing the menu items. Here we are mocking the print_blogs function and then asserting it was called when 'l' was entered in the menu input. This isn't actually testing that anything was created, 
    #but this is ok because we have tests below verifying the functions functionality. At this point we really only need to confirm that the expected function is called from the menu input to have coverage.
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            #patching the input function so that the test doesn't hang waiting for something to be typed in. q is entered as the return value so that when the patched function is called, q will be passed in and exit the Menu.
            with patch('builtins.input', side_effect=('l', 'q')):
                app.menu()
                #verifying that when app.menu is called that the print_blogs function was called.
                mocked_print_blogs.assert_called()

    #verifies that if 'r' is entered at the prompt, that the ask_read_blog function is called.
    def test_menu_calls_ask_read_blog(self):
        with patch('app.ask_read_blog') as mocked_ask_read_blog:
            #patching the input function so that the test doesn't hang waiting for something to be typed in. q is entered as the return value so that when the patched function is called, q will be passed in and exit the Menu.
            with patch('builtins.input', side_effect=('r', 'q')):
                app.menu()
                #verifying that when app.menu is called that the ask_read_blog function was called.
                mocked_ask_read_blog.assert_called()

    #verifies that if 'p' is entered at the prompt, that the ask_read_blog function is called.
    def test_menu_calls_ask_read_blog(self):
        with patch('app.ask_create_post') as mocked_ask_create_post:
            #patching the input function so that the test doesn't hang waiting for something to be typed in. q is entered as the return value so that when the patched function is called, q will be passed in and exit the Menu.
            with patch('builtins.input', side_effect=('p', 'q')):
                app.menu()
                #verifying that when app.menu is called that the print_blogs function was called.
                mocked_ask_create_post.assert_called()

    #testing the print_blogs function
    def test_print_blogs(self):
            app.print_blogs()
            output = self.output_buffer.getvalue()
            expected_output = '- <Blog Title: test blog 1, Author: Test Author 1, Posts: [<Post Title: test post 1 title, Content: test post 1 content., <Post Title: test post 2 title, Content: test post 2 content.].\n- <Blog Title: test blog 2, Author: Test Author 2, Posts: [<Post Title: test post 1 title, Content: test post 1 content., <Post Title: test post 2 title, Content: test post 2 content.].\n'
            #verifying that when app.print_blogs() was called, that it was called with the string below.
            self.assertEqual(output, expected_output)

    #testing the ask_create_blog function
    def test_ask_create_blog(self):
        #since there are multiple inputs in ask_create_blog, we are patching with side_effect to pass an iterable to mock the inputs
        with patch('builtins.input', side_effect=('New Blog', 'New Blog Author')) as mocked_input:
            app.ask_create_blog()
            #here we are verifying that a blog with the title 'Test' is present.
            self.assertIsNotNone(app.blogs.get('New Blog'))
            #here we are verifying that the blog with the title 'Test' has an author 'Test Author'
            self.assertEqual(app.blogs['New Blog'].author, 'New Blog Author')

    #testing the ask_read_blog function that the correct input prompt is called and that print_posts is called with blog2
    def test_ask_read_blog(self):
        #since there are multiple inputs in ask_create_blog, we are patching with side_effect to pass an iterable to mock the inputs
        with patch('builtins.input', return_value = 'test blog 2') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_input.assert_called_with('What is the title of the blog you\'re looking for? ')
                mocked_print_posts.assert_called_with(app.blogs['test blog 2'])

    #testing that the print_posts function prints all the posts associated with the passed in blog
    def test_print_posts(self):
        app.print_posts(app.blogs['test blog 1'])
        output = self.output_buffer.getvalue()
        expected_output = '--- test post 1 title ---\n\ntest post 1 content\n--- test post 2 title ---\n\ntest post 2 content\n'
        #verifying that the output of print_posts matches the expected output.
        self.assertEqual(output, expected_output)

    #verifying that the ask create post function creates a post on the specified blog with the specified title and content.
    def test_ask_create_post(self):
        post_title = 'test post 1'
        post_content = 'test post 1 content'
        with patch('builtins.input', side_effect=('test blog 1', post_title, post_content)):
            app.ask_create_post()
            #here we are verifying that the blog with the title 'Test' has an author 'Test Author'
            self.assertEqual(app.blogs['test blog 1'].posts[-1].title, 'test post 1')
            self.assertEqual(app.blogs['test blog 1'].posts[-1].content, 'test post 1 content')