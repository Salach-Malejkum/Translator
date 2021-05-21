import actions
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)


class TranslatorTest(unittest.TestCase):

    def setUp(self):
        self.form = actions.MainWindow()

    def test_default(self):
        self.assertEqual(self.form.text_in.toPlainText(), "")
        self.assertEqual(self.form.text_out.toPlainText(), "")
        self.assertEqual(self.form.languages_in.currentText(), "Afrikaans")
        self.assertEqual(self.form.languages_out.currentText(), "Afrikaans")
        self.assertEqual(self.form.autocomplete.text(), "Press Tab to complete:")

    def test_empty_translation(self):
        QTest.mouseClick(self.form.translate_button, Qt.LeftButton)
        self.assertEqual(self.form.text_out.toPlainText(), "")

    def test_empty_autocomplete(self):
        self.assertEqual(self.form.text_in.toPlainText(), "")
        QTest.keyClick(self.form.text_in, Qt.Key_Tab)
        self.assertEqual(self.form.text_in.toPlainText(), "")

    def test_autocomplete_wh(self):
        self.assertEqual(self.form.text_in.toPlainText(), "")
        QTest.keyClick(self.form.text_in, 'w')
        QTest.keyClick(self.form.text_in, 'h')
        self.assertEqual(self.form.autocomplete.text(), "Press Tab to complete: where")
        QTest.keyClick(self.form.text_in, Qt.Key_Tab)
        self.assertEqual(self.form.text_in.toPlainText(), "where")
        self.assertEqual(self.form.autocomplete.text(), "Press Tab to complete:")

    def test_few_tab_clicks(self):
        self.assertEqual(self.form.text_in.toPlainText(), "")
        QTest.keyClick(self.form.text_in, 'w')
        QTest.keyClick(self.form.text_in, 'h')
        QTest.keyClick(self.form.text_in, Qt.Key_Tab)
        QTest.keyClick(self.form.text_in, Qt.Key_Tab)
        QTest.keyClick(self.form.text_in, Qt.Key_Tab)
        self.assertEqual(self.form.text_in.toPlainText(), "where")
        self.assertEqual(self.form.autocomplete.text(), "Press Tab to complete:")

    def test_autocomplete_bad_word(self):
        self.assertEqual(self.form.text_in.toPlainText(), "")
        QTest.keyClick(self.form.text_in, 'w')
        QTest.keyClick(self.form.text_in, 'h')
        QTest.keyClick(self.form.text_in, 'e')
        QTest.keyClick(self.form.text_in, 'e')
        QTest.keyClick(self.form.text_in, 'e')
        self.assertEqual(self.form.autocomplete.text(), "Press Tab to complete:")

    def test_swap(self):
        self.form.languages_in.setCurrentIndex(21)
        QTest.mouseClick(self.form.translate_button, Qt.LeftButton)
        actual_text = self.form.text_out.toPlainText()
        QTest.mouseClick(self.form.swap_button, Qt.LeftButton)
        self.assertEqual(actual_text, self.form.text_in.toPlainText())

    def test_same_language_translation(self):
        self.form.text_in.setText("where")
        QTest.mouseClick(self.form.translate_button, Qt.LeftButton)
        self.assertEqual(self.form.text_out.toPlainText(), "where")

    def test_translation(self):
        self.form.languages_in.setCurrentIndex(21)
        self.form.text_in.setText("where")
        QTest.mouseClick(self.form.translate_button, Qt.LeftButton)
        self.assertNotEqual(self.form.text_out.toPlainText(), "")

    def test_save_empty_translation(self):
        QTest.mouseClick(self.form.save_button, Qt.LeftButton)


if __name__ == '__main__':
    unittest.main()
