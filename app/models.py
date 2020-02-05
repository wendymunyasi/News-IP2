class Article:
    '''
    Source class to define our Article Objects
    '''

    def __init__(self, article_id, author, title, description, url, urlToImage, publishedAt, content):
        
        self.article_id = article_id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Source:
    '''
    Source class to define our Source Objects
    '''

    def __init__(self, source_id, name, description, url, category, language, country):
        
        self.source_id = source_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country