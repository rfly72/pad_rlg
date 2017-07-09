class SpellChecker:    
    def __init__(self):
        self.words = []
    def load_words(self, file_name):
        self.words = open(file_name).readlines()
        self.words = map(lambda x: x.strip().lower(), self.words)

    def load_file(self, file_name):
        lines = open(file_name).readlines()
        lines = map(lambda x: x.strip().lower(), lines)
        return lines
        
        
    def check_word(self, word):
        return word.strip('.').lower in self.words
    
    def check_words(self, sentence):
        words_to_check = sentence.split(' ')
        for word in words_to_check:
            if not self.check_word(word):
                print('word is misspelt:' + word)
                failed_words.append(word)
                return False
        return True
if __name__ == '__main__':
    spell_check = SpellChecker()
    spell_check.load_words("spell.words_copy.txt")


    print spell_check.check_word('zygotic')
    print spell_check.check_word('mistasdas')
    print spell_check.check_words('zygotic mistasdas elementary')

