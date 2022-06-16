#Simple word map function for coursera crash course project

file_contents = """A beginning is the time for taking the most delicate care that the balances are correct.
This every sister of the Bene Gesserit knows. To begin your study of the life of Muad’Dib, then, take care that you first
place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you
locate Muad’Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his
first fifteen years there. Arrakis, the planet known as Dune, is forever his place."""

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    #Cleaning string
    usable_words = []
    wordmap_dict = {}
    file_contents = file_contents.lower()
    for character in punctuations:
        file_contents = file_contents.replace(character, "")
    #List Comprehension
    usable_words = [word for word in file_contents.split()
                    if word not in uninteresting_words
                    and word.isalpha()]
    #Dict Comprehension
    wordmap_dict = {word:usable_words.count(word)
              for word in usable_words}
    #Dict Value
    return wordmap_dict

print(calculate_frequencies(file_contents))

