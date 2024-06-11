"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from grupal.pages.index import index_page


class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(route="/", title="inicio", component=index_page)
