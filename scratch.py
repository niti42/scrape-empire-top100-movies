import re


def extract_movie_data(pattern, text):
    if match := re.search(fr'{pattern}', text):
        return match.group(1)


movies = ['100) Reservoir Dogs (1992)', '99) Groundhog Day (1993)', '98) Paddington 2 (2017)',
          '97) Amélie (2001)', '96) Brokeback Mountain (2005)', '95) Donnie Darko (2001)']


movie_rank_pattern = "(^\d{1,3})\)"
movie_name_pattern = "\)\s(.+)\s\("
release_year_pattern = "\((\d{4})\)$"

movie_name_list = []
for movie in movies:
    movie_rank = extract_movie_data(movie_rank_pattern, movie)
    movie_name = extract_movie_data(movie_name_pattern, movie)
    movie_release_year = extract_movie_data(release_year_pattern, movie)
    movie_entry = f"{movie_name},{movie_rank},{movie_release_year}"

    print(movie_entry)
    movie_name_list.append(movie_name)

print(movie_name_list)
