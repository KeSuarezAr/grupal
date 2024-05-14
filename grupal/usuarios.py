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


class UsuariosState(rx.State):
    """The app state."""

    def __init__(self):
        self.usuarios = []

    def add_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def remove_usuario(self, usuario: Usuario):
        self.usuarios.remove(usuario)

    @rx.var
    def get_usuarios(self):
        return self.usuarios

    def get_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario

        return None

    def get_usuario_by_id(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario

        return None

    def get_usuarios_by_proyecto(self, proyecto):
        usuarios = []
        for usuario in self.usuarios:
            if proyecto in usuario.proyectos:
                usuarios.append(usuario)

        return usuarios

    def get_usuarios_by_rol(self, rol):
        usuarios = []
        for usuario in self.usuarios:
            if rol in usuario.roles:
                usuarios.append(usuario)

        return usuarios

    def get_usuarios_by_proyecto_and_rol(self, proyecto, rol):
        usuarios = []
        for usuario in self.usuarios:
            if proyecto in usuario.proyectos and rol in usuario.roles:
                usuarios.append(usuario)

        return usuarios

    def get_usuarios_by_proyecto_and_rol_and_estado(self, proyecto, rol, estado):
        usuarios = []
        for usuario in self.usuarios:
            if (
                proyecto in usuario.proyectos
                and rol in usuario.roles
                and estado in usuario.estados
            ):
                usuarios.append(usuario)

        return usuarios


@rx.page("/usuarios")
def usuarios_page() -> rx.Component:
    """Usuarios Page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="9"),
        rx.container(
            rx.hstack(
                rx.button("Nuevo Usuario", on_click=UsuariosState.add_usuario),
                rx.button("Buscar Usuario", on_click=UsuariosState.get_usuario),
                rx.button("Listar Usuarios", on_click=UsuariosState.get_usuarios),
                rx.button(
                    "Listar Usuarios por Proyecto",
                    on_click=UsuariosState.get_usuarios_by_proyecto,
                ),
                rx.button(
                    "Listar Usuarios por Rol",
                    on_click=UsuariosState.get_usuarios_by_rol,
                ),
                rx.button(
                    "Listar Usuarios por Proyecto y Rol",
                    on_click=UsuariosState.get_usuarios_by_proyecto_and_rol,
                ),
                rx.button(
                    "Listar Usuarios por Proyecto, Rol y Estado",
                    on_click=UsuariosState.get_usuarios_by_proyecto_and_rol_and_estado,
                ),
                rx.button("Volver", on_click="volver"),
                spacing="5",
                justify="center",
            ),
            rx.container(id="usuarios"),
        ),
    )
