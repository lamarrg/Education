from database import Database

from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()

# --------  stuff that has been removed when menu created  -------

# blog = Blog(author='Lamar', title='Blog title', description='best blog')
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database=Blog.from_mongo(blog.id)
#
# print(blog.get_posts())
# -----------
# post = Post(blog_id="125",
#             tLitle="Yet Another great post",
#             content="content galore",
#             author="Lamar")

# post.save_to_mongo()

#post = Post.from_mongo('ba8466fdd69947b981fd0fd74391805b')
# post = Post.from_blog('125')
#
# print(post)