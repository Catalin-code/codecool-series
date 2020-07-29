from flask import Flask, render_template, url_for, request, redirect, jsonify, json
from data import queries
import math
from dotenv import load_dotenv


load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/shows/most-rated/page<int:num>')
def shows_by_rating_desc(num):
    shows = queries.shows_by_rating_desc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 1
    return render_template('shows_by_rating_desc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/lowest-rated/page<int:num>')
def shows_by_rating_asc(num):
    shows = queries.shows_by_rating_asc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 0
    return render_template('shows_by_rating_asc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/z-a/page<int:num>')
def shows_by_title_desc(num):
    shows = queries.shows_by_title_desc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 1
    return render_template('shows_by_title_desc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/a-z/page<int:num>')
def shows_by_title_asc(num):
    shows = queries.shows_by_title_asc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 0
    return render_template('shows_by_title_asc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/oldest/page<int:num>')
def shows_by_year_desc(num):
    shows = queries.shows_by_year_desc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 1
    return render_template('shows_by_year_desc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/most-recent/page<int:num>')
def shows_by_year_asc(num):
    shows = queries.shows_by_year_asc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 0
    return render_template('shows_by_year_asc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/longest-runtime/page<int:num>')
def shows_by_length_desc(num):
    shows = queries.shows_by_length_desc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 1
    return render_template('shows_by_length_desc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/shows/shortest-runtime/page<int:num>')
def shows_by_length_asc(num):
    shows = queries.shows_by_length_asc(num)
    genres = queries.get_most_rated_shows_genres()
    all_shows = queries.get_all_shows()
    all_pages = []
    for i in range((len(all_shows) // 15) + 1):
        all_pages.append(i + 1)
        i += 1
    shown_pages = []
    if num in all_pages:
        for i in range(5):
            shown_pages.append(num + i)
            i += 1
    sorted = 0
    return render_template('shows_by_length_asc.html', shows=shows, genres=genres, pages=shown_pages, num=num, sorted=sorted)


@app.route('/show/<int:id>')
def show_id(id):
    show = queries.get_show_by_id(id)
    genres = queries.get_most_rated_shows_genres()
    actors = queries.get_actors()
    show_seasons = queries.get_show_seasons(id)
    return render_template('show.html', show=show, genres=genres, actors=actors, show_seasons=show_seasons)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
