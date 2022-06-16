# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


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
    def __init__(self, book_contents):
        """attributes specific to the instance of object"""
        self.book_contents = book_contents
        self.usable_words = []
        self.word_map_dict = {}
        
    def word_map(self):
        """Loading instanced object's attribute into a dictionary to be sent to wordcloud array method"""
        #Preparing string
        self.book_contents = self.book_contents.lower()
        for character in Book.punctuations:
            self.book_contents = self.book_contents.replace(character, "")
        #Filtering usable words into list with comprehension
        self.usable_words = [word for word in self.book_contents.split()
                             if word not in Book.uninteresting_words
                             and word.isalpha()]
        
        #Adding frequency of words into dictionary with comprehension
        self.word_map_dict = {word:self.usable_words.count(word)
                              for word in self.usable_words}

        #calling wordcloud class & method
        self.cloud = wordcloud.WordCloud()
        self.cloud.generate_from_frequencies(self.word_map_dict)
        return self.cloud.to_array()
        
    def __str__(self):
        """Display instanced object's attribute"""
        return "The current contents of my string parameter are:n\{}".format(self.book_contents)


# Display your wordcloud image

myimage = Book(file_contents)
plt.imshow(myimage.word_map(), interpolation = 'nearest')
plt.axis('off')
plt.show()