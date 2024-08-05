from reflex import App

from grupal.pages.index_page import index_page
from grupal.pages.login_page import login_page
from grupal.pages.user_list_page import users_page
# from grupal.pages.trimester_list_page import trimesters_page
from grupal.pages.asignaciones_list_page import asignments_page

app = App()

app.add_page(index_page)
app.add_page(users_page)
app.add_page(login_page)
app.add_page(asignments_page)
# app.add_page(trimesters_page)
