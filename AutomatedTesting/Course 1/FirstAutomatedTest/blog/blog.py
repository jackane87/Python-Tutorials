from post import Post


class Blog:
    def __init__(self, title: str, author: str):
        self.title: str = title
        self.author: str = author
        self.posts = []

    def __repr__(self):
        return f'<Blog Title: {self.title}, Author: {self.author}, Posts: {self.posts}.'

    def create_post(self, title: str, content: str):
        self.posts.append(Post(title, content))

    def json(self):
        return {'title': self.title,
                'author': self.author,
                'posts': [post.json() for post in self.posts]}
