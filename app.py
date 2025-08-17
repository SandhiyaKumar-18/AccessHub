from flask import Flask
import os
import psycopg2

app = Flask(__name__)


# def get_db_connection():
#     conn = psycopg2.connect(os.environ['DATABASE_URL'])
#     return conn
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        port=os.environ['DB_PORT']
    )
    return conn
@app.route("/")
def home():
    return "IAM Dashboard is running 🚀"

@app.route("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"✅ DB Connected! Server time: {result[0]}"
    except Exception as e:
        return f"❌ DB Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
