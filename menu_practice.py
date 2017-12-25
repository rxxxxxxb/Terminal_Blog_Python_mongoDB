from database import Database
from models.blog import Blog

class Menu:
    def __init__(self):
        self.user = input('Author Name')
        self.user_blog = None

        if self._user_has_account():
            print('WB')
        else:
            self._prompt_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_for_account(self):
        title = input('ENter title :')
        description = input('Enter description')

        blog = Blog (author = self.user,
                     title = title,
                     description = description)

        blog.save_to_mongo()
        self.user_blog = blog             

    def run_menu(self):
        userInput = input("REad [R] or Write [W]")
        if userInput == 'R':
            self._list_blogs()    
            self._view_blogs()
        elif userInput == 'W':
            self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection= 'blogs',
                                query = {})

        for blog in blogs:
            print("ID :")                        

    def _view_blogs(self):
        blog_to_see = input("Enter blog ID :")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()

        for post in posts:
            print("Date {} title {} \n\n {}".format(post['created_date'],post['title'],post['content']))

        




