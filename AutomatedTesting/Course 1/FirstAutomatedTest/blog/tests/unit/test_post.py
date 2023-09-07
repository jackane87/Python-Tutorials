from unittest import TestCase

import sys
path = '//storage/engineering/Jackson/Python Training/AutomatedTesting/Course 1/FirstAutomatedTest/blog'
sys.path.insert(0,path)
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())

    def test_repr(self):
        p = Post('Test', 'Test Content')
        expected = '<Post Title: Test, Content: Test Content.'
        self.assertEqual(expected, repr(p))