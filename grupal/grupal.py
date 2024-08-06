from reflex import App

from .pages.index import index_pages
from .pages.login import login_page
from .pages.dashboard_padres import dashboard_page
from grupal.pages.student_page import student_page
from grupal.pages.user_list_page import users_page
from grupal.pages.asignaciones_list_page import asignments_page

app = App()

app.add_page(index_pages)
app.add_page(users_page)
app.add_page(login_page)
app.add_page(users_page)
app.add_page(student_page)
app.add_page(asignments_page)
app.add_page(dashboard_page)
