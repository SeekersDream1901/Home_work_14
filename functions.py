import sqlite3

import json


def connect_to_database_and_query_execution(query):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def get_movie_or_TV_series_by_title(title):
    """
    The function searches for a movie or TV series in the database by its title.
    :param title: Users query.
    :return: Dictionary with category and search result.
    """
    query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title LIKE '%{title}%'
        ORDER BY release_year DESC
        LIMIT 1
        """
    movie_or_tv_series_search_result = connect_to_database_and_query_execution(query)[0]
    keys = ['title', 'country', 'release_year', 'listed_in', 'description']
    result = dict(zip(keys, movie_or_tv_series_search_result))
    return result


def get_movie_or_TV_series_by_year_range(start_year, end_year):
    """A function that searches for a movie or TV series within a specified time period by year of release.
    :param start_year:The year of manufacture from which to search.
    :param end_year: Year of manufacture up to which to search.
    :return: List of dictionaries of films and/or TV series released in the specified years of release.
    """
    query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE {start_year} <= release_year <= {end_year}
        LIMIT 100
        """
    movies_or_tv_shows_search_result = connect_to_database_and_query_execution(query)
    movies_or_tv_shows_list = []
    for movies_or_TV_show in movies_or_tv_shows_search_result:
        keys = ['title', 'release_year']
        movies_or_tv_shows_list.append(dict(zip(keys, movies_or_TV_show)))
    return movies_or_tv_shows_list


def get_filter_movies_or_tv_series_by_rating(rating):
    """
    The function implements filtering of films and TV series by their rating.
    :param rating: Requested rating.
    :return: List of dictionaries of films and/or TV series by the desired rating.
    """
    query = f"""
        SELECT rating
        FROM netflix
        WHERE rating LIKE '{rating}'
        """
    movies_or_tv_shows_search_result = connect_to_database_and_query_execution(query)
    movies_or_tv_shows_list = []
    for movies_or_TV_show in movies_or_tv_shows_search_result:
        keys = ['title', 'rating', 'description']
        movies_or_tv_shows_list.append(dict(zip(keys, movies_or_TV_show)))
    return movies_or_tv_shows_list


def get_10_movies_or_TV_series_released_recently_by_listed_in(listed_in):
    """
    A function for displaying the 10 most recently released movies and/or TV series of a specific genre in JSON format.
    :param listed_in: The desired genre.
    :return: The 10 most recently released movies and/or TV series of a certain genre in JSON format.
    """
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in LIKE '%{listed_in}%'
        ORDER BY release_year DESC
        LIMIT 10
        """
    movies_or_tv_shows_search_result = connect_to_database_and_query_execution(query)
    movies_or_tv_shows_list = []
    for movies_or_TV_show in movies_or_tv_shows_search_result:
        keys = ['title', 'description']
        movies_or_tv_shows_list.append(dict(zip(keys, movies_or_TV_show)))
    movies_or_tv_shows_json = json.dumps(movies_or_tv_shows_list, ensure_ascii=False, indent=4)
    return movies_or_tv_shows_json


def get_names_of_actors_playing_in_more_two_films_with_the_actors_looking_for(name_of_the_first_actor,
                                                                              name_of_the_second_actor):
    """
    A function that takes the names of two actors as an argument, stores all actors from the cast column, and returns
    a list of those who have played with them in pairs more than 2 times.
    """
    query = f"""SELECT COUNT(`cast`), `cast`
        FROM netflix
        WHERE `cast` LIKE '%{name_of_the_first_actor}%' AND `cast` LIKE '%{name_of_the_second_actor}%'
        ORDER BY `cast`
        """
    return connect_to_database_and_query_execution(query)


def find_movie(type, release_year, listed_in):
    """
    A function that can be used to pass in the type of film (movie or series), the year of release, and its genre, and
    return a list of film titles with their descriptions in JSON.
    """
    query = f"""SELECT title, description
        FROM netflix
        WHERE type LIKE '%{type}%' AND release_year = {release_year} AND listed_in LIKE '%{listed_in}%'
        LIMIT 10
        """
    data = connect_to_database_and_query_execution(query)
    film_list = []
    for item in data:
        film = {"title": item[0], "description": item[1]}
        film_list.append(film)
    return film_list
