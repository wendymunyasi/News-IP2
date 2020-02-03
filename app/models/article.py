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