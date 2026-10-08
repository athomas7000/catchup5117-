import os

import psycopg
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv(".env")

app = Flask(__name__)


def get_guests():
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM guest ORDER BY guest_id")
            return [row[0] for row in cur.fetchall()]


def save_guest(name):
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO guest (name) VALUES (%s)",
                (name,),
            )


@app.route("/")
def home():
    user_name = request.args.get("userName", "unknown")

    return render_template(
        "index.html",
        user=user_name,
        guests=get_guests(),
    )


@app.route("/about")
def about():
    return "<h1>About the Travel Guestbook</h1>"


@app.route("/guestbook", methods=["POST"])
def add_guest():
    guest_name = request.form.get("guestName", "").strip()

    if not guest_name:
        return jsonify({"error": "Name is required"}), 400

    save_guest(guest_name)

    return jsonify({"name": guest_name}), 201


@app.route("/destination/<city>")
def destination(city):
    return f"<h1>Travel guide for {city}</h1>"