from flask import render_template
from app import app
from .request import get_sources, get_source

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

    title = 'Home - Welcome to the best News website of this century'
    return render_template('index.html', title=title, general=general_source, business=business_source, sports=sports_source, entertainment=entertainment_source, health=health_source, science=science_source, technology=technology_source)


@app.route('/source/<source_id>')
def source(source_id):
    '''
    View article page function that returns the articles under the source
    
    '''
    
    source = get_source(source_id)
    title = f'{source.title}'
     
    return render_template('article.html', source_id = source_id, title = title, source = source)
