from flask import render_template
from app import app
from .request import get_sources, get_article

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    general_source = get_sources('general')
    business_source = get_sources('business')
    technology_source = get_sources('technology')
    sports_source = get_sources('sports')
    entertainment_source = get_sources('entertainment')
    health_source = get_sources('health')
    science_source = get_sources('science')

    title = 'News'
    return render_template('index.html', title=title, general=general_source, business=business_source, sports=sports_source, entertainment=entertainment_source, health=health_source, science=science_source, technology=technology_source)


@app.route('/article/<article_id>')
def article(article_id):
    '''
    View article page function that returns the articles under the source

    '''

    articles = get_article(article_id)
    print(articles)

    return render_template('article.html', id=article_id, articles=articles)