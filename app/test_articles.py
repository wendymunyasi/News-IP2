import unittest
from models import article

Article = article.Article


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article(
            "Satoshi Nakaboto", "Satoshi Nakaboto: ‘Bitcoin shoots up almost 10%!’", "Our robot colleague Satoshi Nakaboto writes about Bitcoin every fucking day. Welcome to another edition of Bitcoin Today, where I, Satoshi Nakaboto, tell you what’s been going on with Bitcoin in the past 24 hours. As Stephen Hawking used to say: Live, laugh, …", "https://thenextweb.com/hardfork/2020/01/15/satoshi-nakaboto-bitcoin-shoots-up-almost-10/", "2020-01-15T09:51:36Z", "Our robot colleague Satoshi Nakaboto writes about Bitcoin BTC every fucking day. Welcome to another edition of Bitcoin Today, where I, Satoshi Nakaboto, tell you whats been going on with Bitcoin in the past 24 hours.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()
