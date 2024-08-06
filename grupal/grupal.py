from reflex import App

from grupal.pages.index import index_page
from grupal.pages.users import users_page
from grupal.pages.login import login_page
from grupal.pages.register import register_page

app = App()

app.add_page(index_page)
app.add_page(users_page)
app.add_page(login_page)
app.add_page(register_page)
