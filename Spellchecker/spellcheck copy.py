words = open("spell.words_copy.txt").readlines()
words = map(lambda x: x.strip(), words)
#print words
print len(words)
print words [0]
print words [len(words)-1]
print('zygotic'in words)
print('mistasdas' in words)

def load_words(file_name):
    words = open(file_name).readlines()
    words = map(lambda x: x.strip().lower(), words)
    return words

    
def check_words(words, sentence):
    words_to_check = sentence.split(' ')
    failed_words = []
    for word in words_to_check:
        if not check_word(words, word):
            print('word is misspelt:' + word)
            failed_words.append(word)
    return failed_words

def check_word(words, word):
    return failed_words

def load_file(self, file_name):
    lines = open(file_name).readlines()
    return map(lambda x: x.strip(), lines)

def load_words(self, file_name):
    self.words = self.load_file(file_name)



def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        index = 0
        for sentence in self.sentences:
            failed_words_in_sentences.extend(self.check_words(sentence, index))
            index = index + 1
        return failed_words_in_sentences

#words = load_words('spell.words_copy.txt')
#print(check_word(words, 'zygotic'))
#print(check_words(words, 'zygotic mistasdas elementary'))
#print load_words("spell.words.txt")[0]
print check_word(words, 'zygotic')
