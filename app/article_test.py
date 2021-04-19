import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.Testcase):
    '''
    Test class to test the behaviour of Article class
    '''
    def setUp(self):
        '''
        Method that runs before every test
        '''
        self.new_article = Article(
            "Danlon Situma", "Test Article", "Lorem Ipsum", "#", "#", "2021-04-19", "Lorem Ipsum")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()