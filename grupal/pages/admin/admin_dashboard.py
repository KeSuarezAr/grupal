from typing import List, Dict

import reflex as rx


class TeacherState(rx.State):
    teachers: List[Dict[str, str]] = [
        {"first_name": "Carlos", "last_name": "Perez", "subjects": "Matematicas, Ingles"},
        {"first_name": "Maria", "last_name": "Gonzalez", "subjects": "Matematicas, Ingles"},
        {"first_name": "Pedro", "last_name": "Lopez", "subjects": "Matematicas, Ingles"},
        {"first_name": "Ana", "last_name": "Martinez", "subjects": "Matematicas, Ingles"},
    ]

    current_teacher: Dict[str, str] = {
        "first_name": "",
        "last_name": "",
        "subjects": "",
    }

    def add_or_edit_teacher(self):
        existing_teacher = next((t for t in self.teachers if
                                 t["first_name"] == self.current_teacher["first_name"] and t["last_name"] ==
                                 self.current_teacher["last_name"]), None)
        if existing_teacher:
            index = self.teachers.index(existing_teacher)
            self.teachers[index] = self.current_teacher.copy()
        else:
            self.teachers.append(self.current_teacher.copy())
        self.current_teacher = {"first_name": "", "last_name": "", "subjects": ""}

    def delete_teacher(self, teacher: Dict[str, str]):
        self.teachers = [t for t in self.teachers if t != teacher]

    def set_current_teacher(self, teacher: Dict[str, str]):
        self.current_teacher = teacher

    def set_first_name(self, first_name):
        self.current_teacher["first_name"] = first_name

    def set_last_name(self, last_name):
        self.current_teacher["last_name"] = last_name

    def set_subjects(self, subjects):
        self.current_teacher["subjects"] = subjects


class ScheduleState(rx.State):
    schedules: List[Dict[str, str]] = [
        {"name": "Matematicas", "image": "math.png"},
        {"name": "Ciencias", "image": "science.png"},
        {"name": "Historia", "image": "history.png"},
        {"name": "Geografia", "image": "geography.png"},
    ]

    current_schedule: Dict[str, str] = {
        "name": "",
        "image": "",
    }

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename
            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
            # Update the img var.
            self.current_schedule["image"] = file.filename

    def add_or_edit_schedule(self):
        existing_schedule = next((s for s in self.schedules if s["name"] == self.current_schedule["name"]), None)
        if existing_schedule:
            index = self.schedules.index(existing_schedule)
            self.schedules[index] = self.current_schedule.copy()
        else:
            self.schedules.append(self.current_schedule.copy())
        self.current_schedule = {"name": "", "image": ""}

    def delete_schedule(self, schedule: Dict[str, str]):
        self.schedules = [s for s in self.schedules if s != schedule]

    def set_current_schedule(self, schedule: Dict[str, str]):
        self.current_schedule = schedule

    def set_name(self, name):
        self.current_schedule["name"] = name

    def set_image(self, image):
        self.current_schedule["image"] = image


@rx.page(
    route="/admin",
    title="Administrador",
)
def admin_page() -> rx.Component:
    def teacher_form() -> rx.Component:
        return rx.form(
            rx.input(
                placeholder="Nombres",
                name="first_name",
                type="text",
                input_mode="text",
                on_change=TeacherState.set_first_name,
                value=TeacherState.current_teacher["first_name"],
            ),
            rx.input(
                placeholder="Apellidos",
                name="last_name",
                type="text",
                input_mode="text",
                on_change=TeacherState.set_last_name,
                value=TeacherState.current_teacher["last_name"],
            ),
            rx.input(
                placeholder="Materias",
                name="subjects",
                type="text",
                input_mode="text",
                on_change=TeacherState.set_subjects,
                value=TeacherState.current_teacher["subjects"],
            ),
            rx.button(
                "Guardar",
                type="submit",
                on_click=TeacherState.add_or_edit_teacher,
            ),
            rx.dialog.close(
                rx.button("Cancelar", variant="soft", color_scheme="red"),
            ),
            reset_on_submit=True,
            justify="center",
            align="center",
        )

    def teacher_dialogue() -> rx.Component:
        return rx.dialog.root(
            rx.dialog.trigger(rx.button("Add Teacher")),
            rx.dialog.content(
                rx.dialog.title("Add New Teacher"),
                rx.dialog.description("Fill in the teacher's information"),
                teacher_form(),
            ),
        )

    def teacher_content_card(item) -> rx.Component:
        return rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(item["first_name"], font_size="1.2em", color="white"),
                    rx.text(item["last_name"], font_size="1em", color="white"),
                    rx.text(item["subjects"], font_size="0.8em", color="white"),
                    align_items="start",
                ),
                rx.vstack(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button("Edit", on_click=lambda: TeacherState.set_current_teacher(item))
                        ),
                        rx.dialog.content(
                            rx.dialog.title("Edit Teacher"),
                            teacher_form(),
                            style={"width": "400px", "padding": "10px"},
                        )
                    ),
                    rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.button("Delete", color_scheme="red")
                        ),
                        rx.alert_dialog.content(
                            rx.alert_dialog.title("Delete Teacher"),
                            rx.alert_dialog.description(
                                f"Are you sure you want to delete {item['first_name']} {item['last_name']}?",
                            ),
                            rx.flex(
                                rx.alert_dialog.cancel(
                                    rx.button("Cancel"),
                                ),
                                rx.alert_dialog.action(
                                    rx.button(
                                        "Delete",
                                        color_scheme="red",
                                        on_click=lambda: TeacherState.delete_teacher(item),
                                    ),
                                ),
                                spacing="3",
                                justify="end",
                            ),
                        ),
                    ),
                    width="100%",
                )
            ),
            height="150px",
            width="200px",
            margin="1em",
            padding="1em",
            background="#2A5D7C",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
        )

    def teachers_body():
        return rx.vstack(
            teacher_dialogue(),
            rx.box(
                rx.foreach(
                    TeacherState.teachers,
                    lambda item: teacher_content_card(item)
                ),
                display="flex",
                flex_wrap="wrap",
                justify_content="center",
            ),
            padding="2em",
            background="rgba(0, 0, 0, 0.5)",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
            width="80%",
            align_items="center",
        ),

    def schedule_content_card(item) -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.image(src=rx.get_upload_url(item['image']), height="100px", width="100px"),
                rx.text(item["name"], font_size="1.2em", color="white"),
                rx.hstack(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.button("Edit", on_click=lambda: ScheduleState.set_current_schedule(item))
                        ),
                        rx.dialog.content(
                            rx.dialog.title("Edit Schedule"),
                            schedule_form(),
                            style={"width": "400px", "padding": "10px"},
                        )
                    ),
                    rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.button("Delete", color_scheme="red")
                        ),
                        rx.alert_dialog.content(
                            rx.alert_dialog.title("Delete Schedule"),
                            rx.alert_dialog.description(
                                f"Are you sure you want to delete {item['name']}?",
                            ),
                            rx.flex(
                                rx.alert_dialog.cancel(
                                    rx.button("Cancel"),
                                ),
                                rx.alert_dialog.action(
                                    rx.button(
                                        "Delete",
                                        color_scheme="red",
                                        on_click=lambda: ScheduleState.delete_schedule(item),
                                    ),
                                ),
                                spacing="3",
                                justify="end",
                            ),
                        ),
                    ),
                ),
            ),
            height="200px",
            width="150px",
            margin="1em",
            padding="1em",
            background="#2A5D7C",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
        )

    def schedule_form() -> rx.Component:
        return rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Materia",
                    name="name",
                    type="text",
                    input_mode="text",
                    on_change=ScheduleState.set_name,
                    value=ScheduleState.current_schedule["name"],
                ),
                rx.upload(
                    rx.text("Upload Image"),
                    id="schedule_upload",
                    border="1px dotted rgb(107,99,246)",
                    padding="2em",
                    multiple=False,
                    accept={"image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"]},
                    max_files=1,
                ),
                rx.button(
                    "Guardar",
                    type="submit",
                    on_click=ScheduleState.add_or_edit_schedule,
                ),
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft", color_scheme="red"),
                ),
                spacing="4",
            ),
            reset_on_submit=True,
        )

    def schedule_dialogue() -> rx.Component:
        return rx.dialog.root(
            rx.dialog.trigger(rx.button("Add Schedule")),
            rx.dialog.content(
                rx.dialog.title("Add New Schedule"),
                rx.dialog.description("Upload a Picture"),
                schedule_form(),
            ),
        )

    def schedules_body():
        return rx.vstack(
            schedule_dialogue(),
            rx.box(
                rx.foreach(
                    ScheduleState.schedules,
                    lambda item: schedule_content_card(item)
                ),
                display="flex",
                flex_wrap="wrap",
                justify_content="center",
            ),
            padding="2em",
            background="rgba(0, 0, 0, 0.5)",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
            width="80%",
            align_items="center",
        )

    return rx.vstack(
        rx.text("Administrador", font_size="2em", color="white", weight="bold", align="center", padding="1em"),
        rx.text("Docentes", font_size="1.5em", color="white", font_weight="bold", align="center"),
        teachers_body(),
        rx.text("Horarios", font_size="1.5em", color="white", font_weight="bold", align="center"),
        schedules_body(),
        rx.vstack(),
        display="flex",
        width="100%",
        height="100vh",
        background="linear-gradient(to bottom right, navy, red)",
        align="center"
    )
