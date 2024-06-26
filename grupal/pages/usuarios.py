import reflex as rx

from grupal.models.usuarios import UsuarioModel

from grupal.connection.usuarios import (
    select_all_admin,
    select_all_profesor,
    select_all_estudiante,
)

from grupal.views.lista_usuarios import tabla_usuarios


class UsuariosState(rx.State):
    usuarios_admin: list[UsuarioModel] = []
    usuarios_profesores: list[UsuarioModel] = []
    usuarios_estudiantes: list[UsuarioModel] = []

    def get_data(self):
        self.usuarios_admin = select_all_admin()
        self.usuarios_profesores = select_all_profesor()
        self.usuarios_estudiantes = select_all_estudiante()


@rx.page(
    on_load=UsuariosState.get_data,
    route="/usuarios",
    title="Usuarios",
)
def usuarios_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.flex(
            rx.heading(
                "Usuarios Administradores",
                title="Usuarios Administradores",
                size="5",
                center=True,
            ),
            tabla_usuarios(UsuariosState.usuarios_admin),
            rx.heading(
                "Usuarios Profesores",
                title="Usuarios Profesores",
                size="5",
                center=True,
            ),
            tabla_usuarios(UsuariosState.usuarios_profesores),
            rx.heading(
                "Usuarios Estudiantes",
                title="Usuarios Estudiantes",
                size="5",
                center=True,
            ),
            tabla_usuarios(UsuariosState.usuarios_estudiantes),
            direction="column",
            justify="center",
            style={
                "padding": "20px",
                "width": "100%",
                "border": "1px solid black",
                "border-radius": "10px",
            },
        ),
    )
