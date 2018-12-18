# Text-analysis
This is a project to clea text document and get what is document is about using Python. For this exercise,I started out with texts of 124 text file.
Whenever we get any data its a good practice to clean the data and remove the unwanted stop words, punctuation to clean our data and after the cleaning we can explore the data to make sense out of the document.  So here we used different types of technique to clean our data.

## Tokenization 

Tokenization is the process of breaking up a sequence of strings into pieces such keywords, phrases, symbols and other elements called tokens.  We converted our data into sentence token using NLTK sent_tokenize and then to word token using word_tokenize of nltk method.  These tokens helped to understand the data and we taken this list of tokens for further cleaning process.
 
## Removed stopwords
A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.  We removed these stopwords by using already existing stopwords in Python and utilized it to get documents without stop words as these stopwords were not required to take into consideration.
Since stopwords do not give a very good idea of the content present inside the data, we eliminate them. Also, if we build word cloud or perform any topic modelling operations on the text, the main highlight of every article would be the articles - ‘the’, ‘a’ and ‘and’. After removing the stopwords, making sense of data gets easy.

## Removed punctuations and non-English characters:
We removed punctuations and non english characters from the data using “re” (regular function) library of python and taken the clean data into other text file to use it for further cleaning process.


## Lemmitised the words using WordNetLemmatizer
After above cleaning we found out there were many different words which was repeating in different forms, for example, Customer and Customers both were present.  Here these both words have same meaning, so we preferred to do lemmatization and combine these words to grab what is important in the document.  For this we used nltk method called WordNetLemmatizer.
## Common words
Common words provide sense about document in a very clear way.  We used nltk.probability FreqDist library to generate top 50 words and the visualized it using matplotlib of python to generate bar graph to have proper understanding of each document.
 
 

## Part of Speech Tagging with NLTK:
NLTK module has the Part of Speech tagging.We  try to  labeled common words which we generated above in a sentence as nouns, adjectives, verbs, etc. This tagging helped us to get all the words parts of speech which we used to perform chunking in next step.Below is the image attached the way we got in python. 
 

 
## Chunking with NLTK:
Now that we had the parts of speech, we used method called chunking, and group words into hopefully meaningful chunks.  One of the main goals of chunking is to group into what are known as "noun phrases”. Our main goal to perform chunking to get clear idea about data and words in some detail way.
 
 
## Named Entity Recognition with NLTK:
One of the most major forms of chunking is called "Named Entity Recognition”.  The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations, monetary figures, and more.
 
Our primary purpose of understanding named entity recognition was to understand the data and get familiar with the content.  For Example: “Washington” which appears several times in multiple text could either refer to George Washington/Denzel Washington or it can refer to Washington D.C. Understanding the reference of such words could prove a big difference in detecting and keeping track of trading activities.

 
## Building Word Clouds:
Word clouds present a low-cost alternative for analyzing text from online surveys.  Word Clouds work by breaking the text down into component words and counting how frequently they appear in the body of text.  Next, the font point size is assigned to words in the cloud based on the frequency that the word appears in the text: the more frequently the word appears, the larger the word is shown in the cloud. 
The purpose of building a word cloud in our program is that key words and brand names pop to the surface which helps to provide an overall sense of the text and would help identifying trends and patterns that would otherwise be difficult to see in a tabular or text format. 

 
