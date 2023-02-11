import json
import sqlite3


def search_title_in_db(search_title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                   SELECT title, country, release_year, listed_in, description
                   FROM netflix
                   WHERE title LIKE '%{search_title}%'
                   ORDER BY release_year DESC
                   """
        result = cursor.execute(query)
        data = cursor.fetchone()
        dict_data = {
            "title": data[0],
            "country": data[1],
            "release_year": data[2],
            "genre": data[3],
            "description": data[4]
        }
        return dict_data


def search_year_to_year(year, to_year):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                   SELECT title, release_year
                   FROM netflix
                   WHERE release_year BETWEEN {year} AND {to_year}
                   LIMIT 100
                   """
        result = cursor.execute(query)
        data = cursor.fetchall()
        data_list = []

        for row in data:
            data_dict = {
                "title": row[0],
                "release_year": row[1]
            }
            data_list.append(data_dict)

        return data_list


def search_rating(rating):
    rating_list = rating.split(", ")
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN {tuple(rating_list)}
                """
        result = cursor.execute(query)
        data = cursor.fetchall()
        data_result = []
        for row in data:
            str_data = {
                "title": row[0],
                "rating": row[1],
                "description": row[2]
            }
            data_result.append(str_data)
        return data_result


def search_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%' 
                    ORDER BY release_year DESC LIMIT 10
                """
        result = cursor.execute(query)
        data = cursor.fetchall()
        data_list = []
        for row in data:
            data_dict = {
                "title": row[0],
                "description": row[1]
            }
            data_list.append(data_dict)
        return json.dumps(data_list)


def search(type_, year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE type = '{type_}'
                    AND release_year = '{year}'
                    AND listed_in LIKE '%{genre}%'
                """
        result = cursor.execute(query)
        data = cursor.fetchall()
        data_list = []
        for row in data:
            data_dict = {
                "title": row[0],
                "description": row[1]
            }
            data_list.append(data_dict)
        return json.dumps(data_list)


print(search("Movie", 2001, "Comedies"))
