import unittest
from Spell import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words.txt')

    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        failed_words = self.spellChecker.check.words ('zygotic mistasdas elementary')
        self.assertEquals(1, len(failed_words))
        self.assertEquals('mistasdas', failed_words [0])
        self.assertEquals(0, len(self.spellChecker.check_words))
        
        self.assertTrue(0, len(self.spellChecker.check_words('our first correct sentence')))
        self.assertTrue(0, len(self.spellChecker.check_words('Our first correct sentence')))
        self.assertTrue((0, len(self.spellChecker.check_words('our first correct sentence.')))
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        self.assertEquals(2, len(failed, words))
        self.assertEquals('mistasdas', failed_words[0])
        self.assertEquals('spelllleeeing', failed_words[1])
 
if __name__ == '__main__':
    unittest.main()
