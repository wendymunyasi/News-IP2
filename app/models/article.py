class Article:
    '''
    Source class to define our Article Objects
    '''

    def __init__(self, author, title, description, url, publishedAt, content):
        
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content