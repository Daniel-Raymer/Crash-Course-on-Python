#Refactored word_map project into my own OOP version

class Book:
    """class attributes shared across all Book objects"""
    #punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #uninteresting words
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    def __init__(self):
        """attributes specific to the instance of object"""
        self.book_contents = ""
        self.usable_words = []
        self.word_map_dict = {}
        
    def word_map(self, txt_para):
        """method to wordmap a text or file parameter into a dictionary"""
        #Preparing string
        self.book_contents = txt_para.lower()
        for character in Book.punctuations:
            self.book_contents = self.book_contents.replace(character, "")
        #Filtering usable words into list with comprehension
        self.usable_words = [word for word in self.book_contents.split()
                             if word not in Book.uninteresting_words
                             and word.isalpha()]
        #Adding frequency of words into dictionary with comprehension
        self.word_map_dict = {word:self.usable_words.count(word)
                              for word in self.usable_words}
        
    def __str__(self):
        """return contents of word_map_dict when called"""
        self.cloud = wordcloud.WordCloud()
        self.cloud.generate_from_frequencies(word_map_dict)
        return self.cloud.to_array()


file_contents = """A beginning is the time for taking the most delicate care that the balances are correct.
This every sister of the Bene Gesserit knows. To begin your study of the life of Muad’Dib, then, take care that you first
place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you
locate Muad’Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his
first fifteen years there. Arrakis, the planet known as Dune, is forever his place."""

dune = Book()
dune.word_map(file_contents)
print(dune)
