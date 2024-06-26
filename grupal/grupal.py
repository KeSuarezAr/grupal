import reflex as rx

from rxconfig import config

from grupal.pages.index import index_page
from grupal.pages.usuarios import usuarios_page
from grupal.pages.agregar_usuario import agregar_usuario_page


class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(component=index_page)
app.add_page(component=usuarios_page)
app.add_page(component=agregar_usuario_page)
