import sqlite3


def search_by_title(title):
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

