import unittest
import data_base
import translate


class TestDataBase(unittest.TestCase):

    def test_add_same_lang(self):
        db = data_base.DataBase()
        db.add_language("polish")
        content_expected = db.get_languages()
        db.add_language("polish")
        self.assertEqual(content_expected, db.get_languages())


class TestTranslate(unittest.TestCase):

    def test_translation(self):
        text = 'Hello world'
        src = 'english'
        dst = 'polish'
        self.assertEqual("Witaj świecie ", translate.translate(text, src, dst))
