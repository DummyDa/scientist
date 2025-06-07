from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DBNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
)

app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def forms():
    if request.method == "POST":
        name = request.form["name"]
        achievements = request.form["achievements"]
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO scientists (name, achievements) VALUES (%s, %s)", (name, achievements),)
                conn.commit()
                return "Успешно"
        except Exception as e:
            conn.rollback()
            print("проблема с ", e)
            return "Ошибка"
    return render_template("form.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()