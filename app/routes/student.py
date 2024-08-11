from . import app
from db.models import Student, Config, Group
from sqlalchemy import select, update, delete
from flask import jsonify


@app.get("/students")
def student_list():
    with Config.SESSION() as session:
        query = select(Student)  # .join(Group)  # .where(Student.name.all_())
        data = session.scalars(query).all()

        result = jsonify([{"name": item.name} for item in data])
        return result
