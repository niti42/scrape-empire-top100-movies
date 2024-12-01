import requests
from bs4 import BeautifulSoup
import re


def extract_movie_data(pattern, text):
    if match := re.search(fr'{pattern}', text):
        return match.group(1)


url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)

empire_100movies = response.text

soup = BeautifulSoup(empire_100movies, "html.parser")
movie_tags = soup.find_all("h2")

movies = []
for movie in movie_tags:
    movie_name = movie.get_text()
    movies.append(movie_name)

movies = movies[1:][::-1]

movie_rank_pattern = "(^\d{1,3})\)"
movie_name_pattern = "\)\s(.+)\s\("
release_year_pattern = "\((\d{4})\)$"

movie_name_list = []

with open("empire100Movies.txt", 'w', encoding="utf-8") as f:
    headers = f"movie_rank,movie_name,movie_release_year\n"
    f.write(headers)
    for movie in movies:
        movie_rank = extract_movie_data(movie_rank_pattern, movie)
        movie_name = extract_movie_data(movie_name_pattern, movie)
        movie_release_year = extract_movie_data(
            release_year_pattern, movie)
        movie_entry = f"{movie_rank},{movie_name},{movie_release_year}\n"
        f.write(movie_entry)
