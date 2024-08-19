import reflex as rx
from sqlmodel import select

from grupal.models.user_model import User


class LoginFormState(rx.State):
    user: dict = {
        "email": "",
        "password": "",
    }
    redirect_url: str = ""

    def submit(self):
        """Maneja la autenticación y redirige según el rol."""
        user_data = self.login_user(self.user)

        if user_data:
            print("Login correcto")
            # Redirige a la página correspondiente según el rol
            self.redirect_url = self.get_redirect_url(user_data["role"])
            print(f"Redirigiendo a: {self.redirect_url}")
            return rx.redirect(self.redirect_url)
        else:
            print("Login incorrecto")
            return rx.window_alert("Credenciales incorrectas.")

    def set_email(self, email):
        self.user["email"] = email

    def set_password(self, password):
        self.user["password"] = password

    def login_user(self, user):
        """Lógica de autenticación"""
        try:
            with rx.session() as session:
                user_data = session.exec(
                    select(User).where(User.email == user["email"], User.password == user["password"])
                ).first()
                if user_data:
                    role = user_data.rol
                    if isinstance(role, list):
                        role = role[0]
                    return {"email": user_data.email, "role": role}
        except Exception as e:
            rx.window_alert(f"Error en la autenticación: {str(e)}")
        return None

    def get_redirect_url(self, role):
        """Devuelve la URL de redirección basada en el rol"""
        role_to_url = {
            "Administrador": "/admin/dashboard",
            "Docente": "/cursos_docente",  # URL para el dashboard de docentes
            "Estudiante": "/materias",
        }
        return role_to_url.get(role, "/login")  # Redirige a login si el rol no está en el diccionario


def login_form() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/escuelajpeg.jpeg",
                        width="12em",
                        height="auto",
                        border_radius="50px",
                        border="5px solid #555"
                    ),
                    rx.text(
                        "Iniciar sesión",
                        font_size="2.5rem",
                        font_weight="bold",
                        color="#FF011D",  # Rojo vibrante para el subtítulo
                    ),
                    direction="column",
                    spacing="5",
                    width="100%"
                ),
                rx.text(
                    "Ingresa tus credenciales para acceder a tu cuenta.",
                    font_size="1.2rem",
                    color="#001737",  # Azul oscuro para el título 
                ),
                rx.vstack(
                    rx.text("Correo electrónico", color="#001737"),  # Azul oscuro para las etiquetas
                    rx.input(
                        placeholder="Correo electrónico",
                        type="email",
                        on_change=LoginFormState.set_email,
                        background_color="#FFFFFF",  # Blanco para el fondo del input
                        border="1px solid #001737",  # Azul oscuro para el borde
                        padding="0.50rem",
                        height="2rem",
                        width="100%",
                        color="#000000",  # Negro para el texto del input
                        font_size="1rem",
                        border_radius="0.75rem",
                        box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                    ),
                    rx.text("Contraseña", color="#001737"),  # Rojo vibrante para las etiquetas
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        on_change=LoginFormState.set_password,
                        background_color="#FFFFFF",  # Blanco para el fondo del input
                        border="1px solid #001737",  # Azul oscuro para el borde
                        padding="0.50rem",
                        height="2rem",
                        width="100%",
                        color="#000000",  # Negro para el texto del input
                        font_size="1rem",
                        border_radius="0.75rem",
                        box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                    ),
                    align_items="flex-start",
                    spacing="1",
                ),
                rx.button(
                    "Iniciar sesión",
                    on_click=LoginFormState.submit,
                    background_color="#001737",  # Azul oscuro para el botón
                    color="#FFFFFF",  # Blanco para el texto del botón
                    padding="0.75rem",
                    width="100%",
                    border_radius="0.75rem",
                    box_shadow="0 2px 10px rgba(0, 23, 55, 0.3)",  # Sombra azul
                    hover_background_color="#FF011D",  # Rojo vibrante al hacer hover
                    active_background_color="#FF011D",  # Rojo vibrante al hacer clic
                ),
                rx.hstack(
                    rx.text("¿Nuevo usuario?", color="#000000"),  # Negro para el texto
                    rx.link(
                        "Crear una cuenta",
                        href="/register",
                        color="#FF011D",  # Rojo vibrante para el enlace
                        text_decoration="underline",
                        hover_color="#001737",  # Azul oscuro al hacer hover
                    ),
                ),
                spacing="1.5rem",
            ),
            padding="3rem",
            background_color="#FFFFFF",  # Blanco para el fondo del card
            border_radius="1rem",
            box_shadow="0 5px 20px rgba(0, 0, 0, 0.1)",  # Sombra ligera
        ),
        height="100vh",
        background_color="#F0F0F0",  # Gris claro para el fondo de la página
    )


@rx.page(route="/login", title="Login")
def login_page() -> rx.Component:
    return login_form()
