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


class TestDataBase(unittest.TestCase):

    def test_add_same_lang(self):
        db = data_base.DataBase()
        db.add_language("polish")
        content_expected = db.get_languages()
        db.add_language("polish")
        self.assertEqual(content_expected, db.get_languages())


# Update tests according to new translate method
class TestTranslate(unittest.TestCase):

    def test_translation_word(self):
        text = 'dog'
        src = 'en'
        dst = 'pl'
        self.assertEqual("pies", translate.translate_google_cloud_api(src, dst, text)['translatedText'])

    def test_translation_text(self):
        text = 'Hello world'
        src = 'en'
        dst = 'pl'
        self.assertEqual("Witaj świecie", translate.translate_google_cloud_api(src, dst, text)['translatedText'])
