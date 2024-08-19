import reflex as rx
from datetime import datetime
from grupal.backend.backend_register import State

class FormState(rx.State):
    name: str = ""
    last_name: str = ""
    email: str = ""
    password: str = ""
    rol: str = "Estudiante"
    active: bool = True

    def handle_change(self, key: str, value: str):
        setattr(self, key, value)

    def handle_checkbox(self, value: bool):
        self.active = value

    def handle_register(self):
        # Create a dictionary with the user data
        user_data = {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "rol": self.rol,
            "active": self.active,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        # Call the method to add the user to the database
        result = State.add_user_to_db(user_data)
        if result:
            print("Usuario creado exitosamente")
            rx.window_alert("Usuario registrado exitosamente.")
            return rx.redirect("/login")  # Redirect after successful registration
        else:
            self.handle_existing_user()

    def handle_existing_user(self):
        """Handle the case where the user already exists and redirect to the login page."""
        print("El usuario ya existe. Redirigiendo a la página de login.")
        rx.window_alert("El usuario ya existe. Serás redirigido a la página de inicio de sesión.")
        return rx.redirect("/login")

# Define the signup form component
def signup_form() -> rx.Component:
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
                    rx.heading(
                        "Registro de Usuario",
                        size="2.5em",
                        color="#FF011D",  # Red color for the title
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%"
                ),
                rx.vstack(
                    rx.text(
                        "Nombre",
                        size="1.5em",
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Nombre",
                        on_change=lambda value: FormState.handle_change("name", value),
                        style={
                            "width": "100%",
                            "border_color": "#001737",
                            "background_color": "#F8F8F8",
                            "color": "#001737",
                            "border": "1px solid #001737",
                            "border_radius": "0.65em",
                            "padding": "0.50em",

                        },
                    ),
                    rx.text(
                        "Apellido",
                        size="1.5em",
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Apellido",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#F8F8F8",  # Light gray background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.50em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("last_name", value),
                    ),
                    rx.text(
                        "Correo Electrónico",
                        size="1.5em",
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="ejemplo@gmail.com",
                        type="email",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#F8F8F8",  # Light gray background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.50em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("email", value),
                    ),
                    rx.text(
                        "Contraseña",
                        size="1.5em",
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        size="1.5em",
                        width="100%",
                        border_color="#001737",  # Dark blue for input borders
                        background_color="#F8F8F8",  # Light gray background for inputs
                        color="#001737",  # Dark blue text for inputs
                        border="1px solid #001737",  # Solid dark blue border
                        border_radius="0.75em",  # More rounded borders
                        padding="0.50em",  # Larger padding inside the input
                        on_change=lambda value: FormState.handle_change("password", value),
                    ),
                    rx.text(
                        "Rol",
                        size="1.5em",
                        color="#001737",  # Dark blue for text
                        text_align="left",
                        width="100%",
                    ),
                    rx.select(
                        ["Estudiante", "Docente", "Administrador"],
                        placeholder="Seleccione un rol",
                        color_scheme="blue",
                        size="3",
                        on_change=lambda value: FormState.handle_change("rol", value),
                    ),
                    rx.box(
                        rx.checkbox(
                            rx.text("Activo", color="black"),
                            default_checked=FormState.active,
                            on_change=lambda value: FormState.handle_checkbox(value),
                            color_scheme="indigo",  # Dark blue for checkbox
                        ),
                    ),
                    rx.button(
                        "Registrarse",
                        size="1.5em",
                        width="100%",
                        background="#001737",  # Dark blue for the button
                        color="white",
                        border_radius="0.75em",
                        box_shadow="0 4px 8px rgba(0, 0, 0, 0.2)",
                        on_click=FormState.handle_register,
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("¿Ya tienes una cuenta?", color="#000000"),  # Black for the text
                    rx.link(
                        "Iniciar sesión",
                        href="/login",
                        color="#FF011D",  # Vibrant red for the link
                        text_decoration="underline",
                        hover_color="#001737",  # Dark blue on hover
                    ),
                ),
                spacing="2",
                width="100%",
            ),
            size="14",
            max_width="50rem",
            width="100%",
            background_color="white",
            padding="2.5em",
            border_radius="1.5em",
            box_shadow="0 8px 10px rgba(0, 0, 0, 0.8)",
        ),
        height="100vh",
        background_color="#F0F0F0",
    )

@rx.page(route="/register", title="Registro")
def register_page() -> rx.Component:
    return signup_form()
