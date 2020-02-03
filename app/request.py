from app import app
import urllib.request
import json
from .models import source, article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# Getting the article base url
# article_base_url = app.config["ARTICLES_BASE_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_sources_list = get_sources_response['sources']
            source_results = process_sources(source_sources_list)

    return source_results


def process_sources(source_sources_list):
    '''
    Function that takes the sources results and transform them to a list of objects
    '''

    source_results = []

    for source_item in source_sources_list:
        source_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(
                source_id, name, description, url, category, language, country)
            source_results.append(source_object)

    return source_results


def get_source(source_id):
    '''
    Function that gets the articles from the source using the id of the source
    '''

    get_source_details_url = base_url.format(source_id, api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        print(source_details_response)

        source_object = None

        if source_details_response:
            source_id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            language = source_details_response.get('language')
            country = source_details_response.get('country')

            source_object = Source(
                source_id, name, description, url, category, language, country)

    return source_object
