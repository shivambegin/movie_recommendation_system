import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load movie data
try:
    with open("movie_dict.pkl", "rb") as f:
        movie_dict = pickle.load(f)
    movies = pd.DataFrame(movie_dict)
except FileNotFoundError:
    raise Exception(
        "Error: 'movie_dict.pkl' file not found. Please ensure the file exists."
    )

# Load similarity matrix or recommendation model
try:
    with open("similarity.pkl", "rb") as f:  # Assuming you have a similarity matrix
        similarity = pickle.load(f)
except FileNotFoundError:
    raise Exception(
        "Error: 'similarity.pkl' file not found. Please ensure the file exists."
    )


def recommend_movie(movie_title):
    """
    Recommends top 5 movies based on the selected movie.
    """
    try:
        # Find the index of the selected movie
        movie_index = movies[movies["title"] == movie_title].index[0]

        # Get similarity scores for the selected movie
        similarity_scores = similarity[movie_index]

        # Sort movies based on similarity scores and get top 5 recommendations
        recommended_movie_indices = similarity_scores.argsort()[::-1][1:6]

        # Get recommended movie titles
        recommended_movies = movies.iloc[recommended_movie_indices][
            "title"
        ].values.tolist()

        return recommended_movies
    except IndexError:
        return []  # Return an empty list if the movie is not found


@app.route("/")
def index():
    """
    Renders the homepage with a list of movie titles.
    """
    movie_titles = movies["title"].values.tolist()
    return render_template("index.html", titles=movie_titles)


@app.route("/recommend", methods=["POST"])
def recommend():
    """
    Handles the recommendation request and renders the results.
    """
    selected_movie = request.form.get("movies")  # Get the selected movie from the form

    if not selected_movie:
        # Handle case where no movie is selected
        movie_titles = movies["title"].values.tolist()
        return render_template(
            "index.html", titles=movie_titles, error="Please select a movie."
        )

    recommendation = recommend_movie(selected_movie)  # Get recommendations
    movie_titles = movies["title"].values.tolist()

    return render_template(
        "index.html",
        titles=movie_titles,
        recommendation=recommendation,
        selected_movie=selected_movie,
    )


if __name__ == "__main__":
    app.run(debug=True)
