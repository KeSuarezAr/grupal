import reflex as rx


class Usuario:
    def __init__(self, id, nombre, proyectos, roles, estados):
        self.id = id
        self.nombre = nombre
        self.proyectos = proyectos
        self.roles = roles
        self.estados = estados

    def __str__(self):
        return f"{self.id} - {self.nombre}"


@rx.page("/agregar_usuario")
def agregar_usuario_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Nuevo Usuario", size="9"),
    )
