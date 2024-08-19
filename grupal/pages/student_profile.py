import reflex as rx

from grupal.models.person import PersonModel
from grupal.models.user import UserModel
from grupal.states.profile import ProfileState


def student_profile() -> rx.Component:
    user = ProfileState.user
    return rx.hstack(
        user_box(user),
        person_box(user.person),
        style=profile_style(),
        on_mount=lambda: ProfileState.get_user_by_id,
    )


def user_box(user: UserModel) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("User Information", font_weight="bold", color="white"),
            rx.image(src="/user.png", width="100%", height="20vh", border_radius="50%"),
            rx.text(f"Username: {user.username}"),
            rx.text(f"Email: {user.email}"),
            spacing="3",
            padding="10"
        ),
        style=box_style(),
    )


def person_box(person: PersonModel) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Personal Information", font_weight="bold", color="white"),
            rx.text(f"First Name: {person.first_name}", color="white"),
            rx.text(f"Last Name: {person.last_name}", color="white"),
            rx.text(f"Cedula: {person.cedula}", color="white"),
            rx.text(f"Address: {person.address}", color="white"),
            margin="10",
            spacing="3",
            padding="10"
        ),
        style=box_style()
    )


def box_style() -> rx.Style:
    return rx.Style(
        margin="10",
        border_radius="10px",
        background_color="#222",
    )


def profile_style() -> rx.Style:
    return rx.Style(
        background_color="#222",
        border_radius="10px",
        box_shadow="0px 0px 10px 0px rgba(0,0,0,0.75)",
    )
