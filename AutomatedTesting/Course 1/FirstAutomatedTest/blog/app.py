from post import Post
from blog import Blog

blogs = dict() #blog_name: Blog object
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print(f'- {blog}')

def ask_create_blog():
    title = input('What is the title of your blog? ')
    author = input('Who is the author of the blog? ')
    blogs[title] = Blog(title , author)

#asks for a blog title and prints the posts
def ask_read_blog():
    blog_title = input('What is the title of the blog you\'re looking for? ')
    #this gets the specific blog object
    print_posts(blogs[blog_title])

def print_posts(blog):
    for post in blog.posts:
        print(post)

#asks for a blog title, post title and post content and creates a new post in the blog specified.
def ask_create_post():
    blog_title = input('What is the title of the blog that you want to add a post to? ')
    post_title = input('What is the title of your post? ')
    post_content = input('Enter your post content: ')
    blog = blogs[blog_title]
    blog.create_post(post_title, post_content)


blog1 = Blog('test blog 1', 'Test Author 1')
blog2 = Blog('test blog 2', 'Test Author 2')
blog1.create_post('test post 1 title', 'test post 1 content')
blog1.create_post('test post 2 title', 'test post 2 content')
blog2.create_post('test post 1 title', 'test post 1 content')
blog2.create_post('test post 2 title', 'test post 2 content')
blogs = {'test blog 1': blog1, 'test blog 2': blog2}

print_blogs()