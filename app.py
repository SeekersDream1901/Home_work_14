
#                              ██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗ 🄱🅈 🄿🅁🄾🄹🄴🄲🅃
#                              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░██║
#                              ██████╦╝██║░░██║██████╔╝██║░░██║███████║
#                              ██╔══██╗██║░░██║██╔═══╝░██║░░██║██╔══██║
#                              ██████╦╝╚█████╔╝██║░░░░░╚█████╔╝██║░░██║
#                              ╚═════╝░░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
from flask import Flask

from functions import get_movie_or_TV_series_by_title, get_movie_or_TV_series_by_year_range

app = Flask(__name__)

@app.route('/movie/<title>')
def movie_or_TV_series_page(title):
    return f"{get_movie_or_TV_series_by_title(title)}"


@app.route('/movie/<start_year>/to/<end_year>')
def movie_or_TV_series_page_by_years(start_year, end_year):
    return f"{get_movie_or_TV_series_by_year_range(start_year, end_year)}"


if __name__ == '__main__':
    app.run()