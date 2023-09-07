from unittest import TestCase

import sys
path = '//storage/engineering/Jackson/Python Training/AutomatedTesting/Course 1/FirstAutomatedTest/blog'
sys.path.insert(0,path)
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('A Brief History', 'Unknown')
        self.assertEqual('<Blog Title: Test, Author: Test Author, Posts: [].', repr(b))
        self.assertEqual('<Blog Title: A Brief History, Author: Unknown, Posts: [].', repr(b2))

    def test_repr_multipleposts(self):
        b = Blog('Test', 'Test Author')
        b.posts = [{'title': 'test_post_1', 'content': 'test content 1'}, {'title': 'test_post_2', 'content': 'test content 2'}]
        b2 = Blog('Exciting Blog', 'Outgoing Person')
        b2.posts = [{'title': 'test_post_1', 'content': 'test content 1'}, {'title': 'test_post_2', 'content': 'test content 2'}, {'title': 'test_post_3', 'content': 'test content 3'}]
        self.assertEqual('<Blog Title: Test, Author: Test Author, Posts: [{\'title\': \'test_post_1\', \'content\': \'test content 1\'}, {\'title\': \'test_post_2\', \'content\': \'test content 2\'}].', repr(b))
        self.assertEqual('<Blog Title: Exciting Blog, Author: Outgoing Person, Posts: [{\'title\': \'test_post_1\', \'content\': \'test content 1\'}, {\'title\': \'test_post_2\', \'content\': \'test content 2\'}, {\'title\': \'test_post_3\', \'content\': \'test content 3\'}].', repr(b2))
        