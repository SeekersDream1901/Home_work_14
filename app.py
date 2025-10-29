#                              ██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗ 🄱🅈 🄿🅁🄾🄹🄴🄲🅃
#                              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░██║
#                              ██████╦╝██║░░██║██████╔╝██║░░██║███████║
#                              ██╔══██╗██║░░██║██╔═══╝░██║░░██║██╔══██║
#                              ██████╦╝╚█████╔╝██║░░░░░╚█████╔╝██║░░██║
#                              ╚═════╝░░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
from flask import Flask

from functions import get_movie_or_TV_series_by_title, get_movie_or_TV_series_by_year_range, \
    get_filter_movies_or_tv_series_by_rating

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_or_TV_series_page(title):
    return f"{get_movie_or_TV_series_by_title(title)}"


@app.route('/movie/<start_year>/to/<end_year>')
def movie_or_TV_series_page_by_years(start_year, end_year):
    return f"{get_movie_or_TV_series_by_year_range(start_year, end_year)}"


@app.route('/rating/children')
def movie_or_TV_series_page_for_children():
    return f"{get_filter_movies_or_tv_series_by_rating("G")}"


@app.route('/rating/<required_rating>')
def movie_or_TV_series_page_for_family(required_rating):
    if required_rating == 'children':
        return f"{get_filter_movies_or_tv_series_by_rating('G')}"
    elif required_rating == 'family':
        rating_g = get_filter_movies_or_tv_series_by_rating('G')
        rating_pg = get_filter_movies_or_tv_series_by_rating('PG')
        rating_pg_13 = get_filter_movies_or_tv_series_by_rating('PG_13')
        return rating_g + rating_pg + rating_pg_13
    elif required_rating == 'adult':
        rating_r = get_filter_movies_or_tv_series_by_rating('R')
        rating_nc_17 = get_filter_movies_or_tv_series_by_rating('NC_17')
        return rating_r + rating_nc_17


if __name__ == '__main__':
    app.run()
