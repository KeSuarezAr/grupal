import reflex as rx
from typing import Optional
from sqlmodel import Field
from enum import Enum


class Rol(str, Enum):
    admin = "admin"
    profesor = "profesor"
    estudiante = "estudiante"


class UsuarioModel(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    cedula: str
    nombres: str
    apellidos: str
    correo: str
    telefono: str
    direccion: str
    rol: Rol
