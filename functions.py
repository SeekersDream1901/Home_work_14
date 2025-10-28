import sqlite3


def get_movie_or_TV_show_by_title(title):
    """
    The function searches for a movie or TV show in the database by its title.
    :param title: Users query.
    :return: Dictionary with category and search result.
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE '%{title}%'
            ORDER BY release_year DESC
            LIMIT 1
            """
        cursor.execute(query)
        movie_search_result = cursor.fetchall()[0]
        keys = ['title', 'country', 'release_year', 'listed_in', 'description']
        result = dict(zip(keys, movie_search_result))
        return result


def get_movie_or_TV_show_by_year_range(start_year, end_year):
    """

    :param start_year:
    :param end_year:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE {start_year} <= release_year <= {end_year}
            LIMIT 100
            """
        cursor.execute(query)
        movies_or_tv_show_search_result = cursor.fetchall()
        movies_or_tv_show_list = []

        for movies_or_TV_show in movies_or_tv_show_search_result:
            keys = ['title', 'release_year']
            movies_or_tv_show_list.append(dict(zip(keys, movies_or_TV_show)))

        return movies_or_tv_show_list
