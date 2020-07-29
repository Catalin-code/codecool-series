from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_all_shows():
    return data_manager.execute_select('SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY rating DESC;')


def get_most_rated_shows_genres():
    return data_manager.execute_select('SELECT genres.id, genres.name, show_genres.genre_id, show_genres.show_id FROM genres JOIN show_genres ON genres.id = show_genres.genre_id ORDER BY name;')


def get_actors():
    return data_manager.execute_select('SELECT actors.id, actors.name, show_characters.actor_id, show_characters.show_id FROM actors JOIN show_characters ON actors.id = show_characters.actor_id ORDER BY name;')


def get_show_seasons(show_id):
    return data_manager.execute_select(f'SELECT * FROM seasons WHERE show_id = {show_id} ORDER BY title;')


def shows_by_rating_desc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY rating DESC LIMIT 15 OFFSET {offset};')


def shows_by_rating_asc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY rating LIMIT 15 OFFSET {offset};')


def shows_by_year_desc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY year DESC LIMIT 15 OFFSET {offset};')


def shows_by_year_asc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY year LIMIT 15 OFFSET {offset};')


def shows_by_title_desc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY title DESC LIMIT 15 OFFSET {offset};')


def shows_by_title_asc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY title LIMIT 15 OFFSET {offset};')


def shows_by_length_desc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY runtime DESC LIMIT 15 OFFSET {offset};')


def shows_by_length_asc(page):
    offset = (page - 1) * 15
    return data_manager.execute_select(f'SELECT id, title, year, runtime, CAST(rating AS decimal(10, 1)), trailer, homepage  FROM shows ORDER BY runtime LIMIT 15 OFFSET {offset};')


def get_show_by_id(id):
    return data_manager.execute_select(f'SELECT * FROM shows WHERE id = {id};')
