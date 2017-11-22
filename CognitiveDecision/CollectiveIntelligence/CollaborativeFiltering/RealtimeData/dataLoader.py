#! python3


def load_movieslen(path='data'):
    movies = {}
    for line in open(path + '/u.item'):
        movie_id, title = line.split('|')[:2]
        movies[movie_id] = title

    prefs = {}
    for line in open(path + '/u.data'):
        user, movie_id, rating = line.split('\t')[:3]
        prefs.setdefault(user, {})
        prefs[user][movies[movie_id]] = float(rating)
    return prefs
