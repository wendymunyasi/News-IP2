import urllib.request
import json
from .models import Source, Article


# Getting api key
api_key = None

# Getting the news base url
base_url = None

# Getting the article base url
article_base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLES_BASE_URL']


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


def get_article(article_id):
    '''
    Function that gets the articles from the source using the id of the source
    '''

    get_articles_url = article_base_url.format(article_id, api_key)

    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            article_articles_list = get_articles_response['articles']
            articles_results = process_articles(article_articles_list)

        # print(get_articles_response)
        print(articles_results)

    return articles_results


def process_articles(article_articles_list):
    '''
    Function that takes the sources results and transform them to a list of objects
    '''

    article_results = []

    for article_item in article_articles_list:
        article_id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Article(
                article_id, author, title, description, url, urlToImage, publishedAt, content)
            article_results.append(article_object)

    return article_results
