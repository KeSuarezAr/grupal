import reflex as rx

from grupal.pages.admin.admin_dashboard import admin_page
from grupal.pages.asignaciones_list_page import asignments_page
from grupal.pages.padres.dashboard_padres import dashboard_page
from grupal.pages.index import index_page
from grupal.pages.student.dashboard_student import cursos_page
from grupal.pages.student.dashboard_student_Horarios import horario_page
from grupal.pages.student.dashboard_student_actividades import actividades_page
from grupal.pages.student.dashboard_student_calificaciones import calificaciones_page
from grupal.pages.student.student_page import student_page
from grupal.pages.student.students import students_page
from grupal.pages.student.tareas import tareas_page
from grupal.pages.user_list_page import users_page
from grupal.pages.asignacion_tareas import asignar_tarea_page
from grupal.pages.estudiante.dashboard_student_actividades import materias_page
from grupal.pages.login import login_page
from grupal.pages.register import register_page

app = rx.App()

app.theme = rx.theme(
    appearance="dark", has_background=True, radius="large", accent_color="grass"
)

app.add_page(index_page)
app.add_page(users_page)
app.add_page(register_page)
app.add_page(login_page)
app.add_page(users_page)
app.add_page(student_page)
app.add_page(students_page)
app.add_page(asignments_page)
app.add_page(dashboard_page)
app.add_page(tareas_page)
app.add_page(cursos_page)
app.add_page(actividades_page)
app.add_page(calificaciones_page)
# app.add_page(docente_page)
app.add_page(asignar_tarea_page)
app.add_page(materias_page)
app.add_page(horario_page)
app.add_page(admin_page)
