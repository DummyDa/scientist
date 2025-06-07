from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import psycopg2

app = Flask(__name__)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()