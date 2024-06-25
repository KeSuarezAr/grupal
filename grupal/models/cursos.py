import reflex as rx


class CursosModel(rx.Model):

    def __init__(self, nombre: str, descripcion: str, duracion: str, responsable: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.responsable = responsable

    def __str__(self):
        return self.nombre
