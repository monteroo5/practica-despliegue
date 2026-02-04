from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # Usamos tus mismos datos de la App 3
        conn = mysql.connector.connect(
            host="172.31.18.91",
            user="admin_practica",
            password="Sandia4you",
            database="db_app4"
        )
        return "<h1>✅ App 4 (Python): Conexión exitosa a la DB en Instancia 4!</h1>"
    except Exception as e:
        return f"<h1>❌ Error de conexión: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
