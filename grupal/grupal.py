from reflex import App

# from grupal.pages.index_page import index_page
# from grupal.pages.login_page import login_page
from grupal.pages.user_list_page import users_page
# from grupal.pages.trimester_list_page import trimesters_page
from grupal.pages.asignaciones_list_page import asignments_page
from .pages.index import index_pages
from .pages.login import login_page
from .pages.dashboard_padres import dashboard_page

app = App()

app.add_page(index_pages)
app.add_page(login_page)
app.add_page(users_page)
app.add_page(asignments_page)
app.add_page(dashboard_page)

# app.add_page(login_page)
# app.add_page(register_page)
# app.add_page(trimesters_page)
# app.add_page(index_page)
