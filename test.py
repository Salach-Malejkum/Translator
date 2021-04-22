import unittest
import data_base
import translate


class TestRunner:
    def __init__(self):
        self.runner = unittest.TextTestRunner()

    def run(self):
        test_suite = unittest.TestSuite(tests=[
            unittest.makeSuite(TestDataBase),
            unittest.makeSuite(TestTranslate)
        ])
        return self.runner.run(test_suite)


# Update tests according to new translate method
class TestDataBase(unittest.TestCase):

    def test_add_same_lang(self):
        db = data_base.DataBase()
        print(db.get_languages().keys())


# Update tests according to new translate method
class TestTranslate(unittest.TestCase):

    def test_translation_word(self):
        text = 'dog'
        src = 'en'
        dest = 'pl'
        self.assertEqual("pies", translate.translate_google_cloud_api(src, dest, text)['translatedText'])

    def test_translation_text(self):
        text = 'Hello world'
        src = 'en'
        dest = 'pl'
        self.assertEqual("Witaj świecie", translate.translate_google_cloud_api(src, dest, text)['translatedText'])
