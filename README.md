# Text-analysis
This is a project to clea text document and get what is document is about using Python. For this exercise,I started out with texts of 124 text file.
Whenever we get any data its a good practice to clean the data and remove the unwanted stop words, punctuation to clean our data and after the cleaning we can explore the data to make sense out of the document.  So here we used different types of technique to clean our data.

Tokenization 
Tokenization is the process of breaking up a sequence of strings into pieces such keywords, phrases, symbols and other elements called tokens.  We converted our data into sentence token using NLTK sent_tokenize and then to word token using word_tokenize of nltk method.  These tokens helped to understand the data and we taken this list of tokens for further cleaning process.
 
Removed stopwords:
A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.  We removed these stopwords by using already existing stopwords in Python and utilized it to get documents without stop words as these stopwords were not required to take into consideration.
Since stopwords do not give a very good idea of the content present inside the data, we eliminate them. Also, if we build word cloud or perform any topic modelling operations on the text, the main highlight of every article would be the articles - ‘the’, ‘a’ and ‘and’. After removing the stopwords, making sense of data gets easy.

Removed punctuations and non-English characters:
We removed punctuations and non english characters from the data using “re” (regular function) library of python and taken the clean data into other text file to use it for further cleaning process.


Lemmitised the words using WordNetLemmatizer
After above cleaning we found out there were many different words which was repeating in different forms, for example, Customer and Customers both were present.  Here these both words have same meaning, so we preferred to do lemmatization and combine these words to grab what is important in the document.  For this we used nltk method called WordNetLemmatizer.
