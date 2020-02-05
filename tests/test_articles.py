import unittest
from app.models import Article


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article(
            "bbc-news", "BBC News", "Police search homes in Streatham attack probe", "Two addresses are searched as it emerges attacker Sudesh Amman was released from prison last month.", "http://www.bbc.co.uk/news/uk-51356447", "https://ichef.bbci.co.uk/news/1024/branded_news/D862/production/_104849355_terror105-18amman.jpg", "2020-02-03T09:43:01Z", "Image copyrightMet Police Police have been searching two addresses as part of the investigation into the attack in Streatham on Sunday")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))