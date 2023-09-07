from unittest import TestCase

import sys
path = '//storage/engineering/Jackson/Python Training/AutomatedTesting/Course 1/FirstAutomatedTest/blog'
sys.path.insert(0,path)
from blog import Blog

class BlogTest(TestCase):
    def test_create_blogpost(self):
        b = Blog('Test', 'Test Author')
        b.create_post('test post title', 'test item')
        b.create_post('test post title2', 'test item2')
        self.assertEqual(len(b.posts), 2)
        self.assertEqual('test post title', b.posts[0].title)
        self.assertEqual('test item', b.posts[0].content)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test',
                                    'author': 'Test Author', 
                                    'posts': []
                                }
        self.assertDictEqual(expected, b.json())


    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('test post title', 'test item')
        expected = {'title': 'Test',
                                    'author': 'Test Author', 
                                    'posts': [
                                        {'title': 'test post title', 
                                        'content': 'test item'}
                                    ]
                                }
        self.assertDictEqual(expected, b.json())