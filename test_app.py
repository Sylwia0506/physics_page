import unittest
from app import app, slugify
from settings import PHYSICS_TOPICS

class TestMathsPage(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_slugify(self):
        test_cases = [
            ('Mechanika kwantowa', 'mechanika-kwantowa'),
            ('Elektryczność i magnetyzm', 'elektrycznosc-i-magnetyzm'),
            ('Fizyka atomowa', 'fizyka-atomowa'),
            ('Termodynamika', 'termodynamika'),
            ('Fale i optyka', 'fale-i-optyka'),
            ('Fizyka jądrowa', 'fizyka-jadrowa'),
            ('Astronomia', 'astronomia'),
            ('Fizyka cząstek elementarnych', 'fizyka-czastek-elementarnych'),
            ('Relatywistyka', 'relatywistyka'),
            ('Fizyka statystyczna', 'fizyka-statystyczna')
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(slugify(input_text), expected)

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_matura_route(self):
        response = self.app.get('/matura')
        self.assertEqual(response.status_code, 200)

    def test_topics_route(self):
        response = self.app.get('/działy')
        self.assertEqual(response.status_code, 200)

    def test_topic_route(self):
        for topic in PHYSICS_TOPICS:
            slug = slugify(topic['name'])
            response = self.app.get(f'/działy/{slug}')
            self.assertEqual(response.status_code, 200)

    def test_nonexistent_topic(self):
        response = self.app.get('/działy/nonexistent-topic')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 