from flask import Flask, render_template, request, redirect, url_for,jsonify

app = Flask(__name__)

guest_names = []


@app.route("/")
def home():
    user_name = request.args.get("userName", "unknown")

    return render_template(
        "index.html",
        user=user_name,
        guests=guest_names
    )


@app.route("/about")
def about():
    return "<h1>About the Travel Guestbook</h1>"


@app.route("/guestbook", methods=["POST"])
def add_guest():
    guest_name = request.form.get("guestName", "").strip()

    if not guest_name:
        return jsonify({"error": "Name is required"}), 400

    guest_names.append(guest_name)

    return jsonify({"name": guest_name}), 201

@app.route("/destination/<city>")
def destination(city):
    return f"<h1>Travel guide for {city}</h1>"