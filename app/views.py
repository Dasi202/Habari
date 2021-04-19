from flask import render_template
from app import app
from .request import get_articles

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # getting us news
    us_articles = get_articles('us')
    print(us_articles)
    title = 'Habari /Home of up to date news.'
    return render_template('index.html',title=title,us = us_articles)
