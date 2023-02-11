from flask import Flask, render_template
import utils


app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def title_page(title):
    data = utils.search_title_in_db(title)
    return render_template("search_title.html", data=data, title=data["title"])


@app.route('/movie/<int:year>/to/<int:to_year>')
def years_page(year, to_year):
    data = utils.search_year_to_year(year, to_year)
    return render_template("search_years.html", data=data, year=year, to_year=to_year)


@app.route('/rating/<input_rating>')
def rating_page(input_rating):
    if input_rating.lower() == "children":
        data = utils.search_rating('G')
    elif input_rating.lower() == "family":
        data = utils.search_rating('G, PG, PG-13')
    elif input_rating.lower() == "adult":
        data = utils.search_rating('R, NC-17')
    else:
        return "Введите корректное значение фильтра по рейтингу: children, family или adult"
    return render_template("search_rating.html", data=data, rating=input_rating)


@app.route('/genre/<genre>')
def genre_page(genre):
    data = utils.search_genre(genre)
    return data


if __name__ == '__main__':
    app.run()
