class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f'<Post Title: {self.title}, Content: {self.content}.'
    
    def __str__(self) -> str:
        return '--- {} ---\n\n{}'.format(self.title, self.content)
    

    def json(self):
        return {'title': self.title,
                'content': self.content}
    
