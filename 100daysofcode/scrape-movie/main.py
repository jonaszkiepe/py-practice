import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movie_h3s = soup.select("div h3")
movie_text = [movie.getText() + "\n" for movie in movie_h3s]
with open("100-movies.txt", "w", encoding="utf-8") as file:
    file.writelines(movie_text[::-1])
