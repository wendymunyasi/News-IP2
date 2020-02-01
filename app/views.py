from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome To The best News Website Of The Century'
    message = 'Boom, done'
    return render_template('index.html', message=message, title = title)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html', news_id=news_id)
