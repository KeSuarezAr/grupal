from grupal.connection.conexion import create_database_engine
from grupal.models.usuarios import UsuarioModel

from sqlmodel import Session, select, insert


def select_all() -> list[UsuarioModel]:
    engine = create_database_engine()

    with Session(engine) as session:
        consulta = select(UsuarioModel)
        estudiantes = session.exec(consulta)
        return list(estudiantes)


def select_user(id: int) -> list[UsuarioModel]:
    engine = create_database_engine()

    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.id == id)
        estudiantes = session.exec(consulta)
        return list(estudiantes)


def insert_usuario(usuario: dict):
    engine = create_database_engine()

    with Session(engine) as session:
        session.add(UsuarioModel(**usuario))
        session.commit()


def update_usuario(id: int, usuario: dict):
    engine = create_database_engine()

    with Session(engine) as session:
        session.query(UsuarioModel).filter(UsuarioModel.id == id).update(usuario)
        session.commit()


def delete_usuario(id: int):
    engine = create_database_engine()

    with Session(engine) as session:
        session.delete(session.get(UsuarioModel, id))
        session.commit()


def select_all_estudiante() -> list[UsuarioModel]:
    engine = create_database_engine()

    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.rol == "estudiante")
        estudiantes = session.exec(consulta)
        return list(estudiantes)


def select_all_profesor() -> list[UsuarioModel]:
    engine = create_database_engine()

    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.rol == "profesor")
        profesores = session.exec(consulta)
        return list(profesores)


def select_all_admin() -> list[UsuarioModel]:
    engine = create_database_engine()

    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.rol == "admin")
        admins = session.exec(consulta)
        return list(admins)
