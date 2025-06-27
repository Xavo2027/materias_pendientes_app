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
            "celular": request.form.get("celular"),
            "celular_alt": request.form.get("celular_alt"),
            "fecha_nac": request.form.get("fecha_nac"),
            "cursado_anterior": request.form.get("cursado_anterior"),
            "turno": request.form.get("turno"),
            "cursa_actualmente": request.form.get("cursa_actualmente"),
            "institucion": request.form.get("institucion"),
            "nombre_institucion": request.form.get("nombre_institucion"),
            "localidad_provincia": request.form.get("localidad_provincia"),
            "materias_totales": request.form.get("materias_totales"),
            "materias_a_rendir": request.form.get("materias_a_rendir"),
            "materias": request.form.get("materias"),
            "preferencia_materias": request.form.get("preferencia_materias"),
            "observaciones": request.form.get("observaciones"),
            "genero": request.form.get("genero"),
            "egreso_fines": request.form.get("egreso_fines"),
            "cursado_2023": request.form.get("cursado_2023")
        }

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO alumnos (
                    email, dni, apellido, nombre, celular, celular_alt, fecha_nac, cursado_anterior,
                    turno, cursa_actualmente, institucion, nombre_institucion, localidad_provincia,
                    materias_totales, materias_a_rendir, materias, preferencia_materias, observaciones,
                    genero, egreso_fines, cursado_2023
                ) VALUES (
                    %(email)s, %(dni)s, %(apellido)s, %(nombre)s, %(celular)s, %(celular_alt)s, %(fecha_nac)s, %(cursado_anterior)s,
                    %(turno)s, %(cursa_actualmente)s, %(institucion)s, %(nombre_institucion)s, %(localidad_provincia)s,
                    %(materias_totales)s, %(materias_a_rendir)s, %(materias)s, %(preferencia_materias)s, %(observaciones)s,
                    %(genero)s, %(egreso_fines)s, %(cursado_2023)s
                )
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
