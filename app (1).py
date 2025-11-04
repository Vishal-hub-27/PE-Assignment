from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# ---------- Load Dataset ----------
def load_movies():
    movies = []
    csv_path = os.path.join(os.path.dirname(__file__), "movies.csv")

    if not os.path.exists(csv_path):
        print("❌ Error: movies.csv not found.")
        return movies

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                movies.append({
                    "Title": row["Title"],
                    "Genre": row["Genre"],
                    "Rating": float(row["Rating"]),
                    "Popularity": float(row["Popularity"]),
                    "Year": int(row["Year"])
                })
            except Exception as e:
                print(f"⚠️ Skipping invalid row: {row} ({e})")
    print(f"✅ Loaded {len(movies)} movies.")
    return movies

movies = load_movies()

# ---------- Heuristic Function ----------
def heuristic(user_genre, movie):
    genre_match = 1.0 if user_genre.lower() in movie["Genre"].lower() else 0.0
    score = (0.5 * genre_match) + (0.3 * (movie["Rating"] / 10)) + (0.2 * (movie["Popularity"] / 100))
    return score

# ---------- Best First Search ----------
def best_first_search(user_genre):
    if not movies:
        return []
    scores = [(heuristic(user_genre, m), m) for m in movies]
    scores.sort(reverse=True, key=lambda x: x[0])
    return [m for _, m in scores[:10]]

# ---------- Hill Climbing ----------
def hill_climbing(user_genre):
    if not movies:
        return []
    current = movies[0]
    current_score = heuristic(user_genre, current)

    for _ in range(50):
        neighbor = max(movies, key=lambda m: heuristic(user_genre, m))
        neighbor_score = heuristic(user_genre, neighbor)
        if neighbor_score <= current_score:
            break
        current = neighbor
        current_score = neighbor_score
    return [current]

# ---------- Flask Routes ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    algo = request.form["algorithm"]
    genre = request.form["genre"]

    if not movies:
        return render_template("index.html", error="❌ movies.csv not loaded correctly!")

    if algo == "bestfirst":
        result = best_first_search(genre)
    else:
        result = hill_climbing(genre)

    if not result:
        return render_template("index.html", error=f"No results found for '{genre}'.")

    # Go to next page with results
    return render_template("recommend.html", results=result, algo=algo, genre=genre)

if __name__ == "__main__":
    app.run(debug=True)
