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

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()