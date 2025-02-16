from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route (Loads HTML frontend)
@app.route("/")
def home():
    return render_template("index.html")  # Renders the frontend

# API route to handle movie search
@app.route("/search", methods=["GET"])
def search_movie():
    query = request.args.get("query")  # Get user input from frontend
    if not query:
        return jsonify([])  # Return empty response if no input

    # Dummy movie data (Replace with a database or API)
    movies = [
        {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "poster": "https://via.placeholder.com/200x300"},
        {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "poster": "https://via.placeholder.com/200x300"},
        {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "poster": "https://via.placeholder.com/200x300"},
    ]

    # Filter movies based on query
    result = [movie for movie in movies if query.lower() in movie["title"].lower()]
    return jsonify(result)  # Return JSON response to frontend

if __name__ == "__main__":
    app.run(debug=True)