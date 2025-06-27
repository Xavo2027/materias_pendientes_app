from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import get_db_connection

alumnos_bp = Blueprint('alumnos', __name__)

@alumnos_bp.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        data = {
            "email": request.form.get("email"),
            "dni": request.form.get("dni"),
            "apellido": request.form.get("apellido"),
            "nombre": request.form.get("nombre"),
            "celular": request.form.get("celular")
        }

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO alumnos (email, dni, apellido, nombre, celular)
                VALUES (%(email)s, %(dni)s, %(apellido)s, %(nombre)s, %(celular)s)
            """, data)
            conn.commit()
            cur.close()
            conn.close()

            flash("✅ Alumno guardado correctamente.", "success")
            return redirect(url_for("alumnos.vista_excel"))

        except Exception as e:
            flash(f"❌ Error al guardar: {e}", "danger")

    return render_template("alumnos.html")

@alumnos_bp.route("/vista_excel")
def vista_excel():
    return render_template("vista_excel.html")
