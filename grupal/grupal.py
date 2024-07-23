from reflex import App

from grupal.pages.index import index_page
from grupal.pages.users import users_page

app = App()

app.add_page(index_page)
app.add_page(users_page)
