import os
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import nltk
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
#import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
stopwords = set(STOPWORDS)
path = '/Users/shailaja/Desktop/bigdata_project/Text'
i=0
for itemName in os.listdir(path):
    itemName = os.path.join(path, itemName)
    if os.path.isfile(itemName):
        file= open(itemName,'rt',encoding="utf8")
        train_text=file.read()
        file.close()
        ## word tokenization
        word_tokens=nltk.word_tokenize(train_text)
        print(word_tokens)

        ###remove punctuation
        import re
        punctuation = re.compile(r'[-.?!,:;()|0-9]')
        post_punctuation = []
        for words in word_tokens:
            word = punctuation.sub("", words)
            if len(word) > 0:
                post_punctuation.append(word)

        ###stemming
        ps=PorterStemmer()
        word_stem=[]
        for word in word_stopword_removed:
            word_stem.append(ps.stem(word))
        print(word_stem)

        ######lemmetization
        word_lemmi=[]
        lemmi=WordNetLemmatizer()
        for word in post_punctuation:
            word_lemmi.append(lemmi.lemmatize(word))
        #print(word_lemmi)

        ### removing stopwords
        word_stopword_removed = []
        for word in word_lemmi:
            if word in stopwords:
                continue
            else:
                word_stopword_removed.append(word)


        words = [word for word in word_stopword_removed if word.isalnum()]

        ####frequency of words
        #print(len(word_tokens))
        from nltk.probability import FreqDist

        ####doesnt include special word
        fdist = FreqDist(words)
        total_word = fdist.most_common(50)
        #print("total_word", total_word)
        top_word=[]
        for k in total_word:
            top_word.append(k[0])
        #print("top_word",top_word)




        words_list_tagged=nltk.pos_tag(top_word)
       # print(nltk.pos_tag(top_word))
        pattern = """NP: {<DT>?<JJ>*<NN>}
        VBD: {<VBD>}
        IN: {<IN>}"""
        NPChunker = nltk.RegexpParser(pattern)
        result = NPChunker.parse(words_list_tagged)
        result.draw()

        words_ne_chunk=nltk.ne_chunk(words_list_tagged,binary=True)
        #print(words_ne_chunk)
        words_ne_chunk.draw()

        ###plot

        ##Word cloud of top words
        import matplotlib.pyplot as plt
        strng=" "
        #print(words)
        for word in top_word:
            #print("i",i)
            strng+=word+" "
        #print(strng)

        wordcloud = WordCloud(width=2000, height=2000, stopwords=stopwords, min_font_size=10).generate(strng)

        plt.tight_layout()
        plt.axis("off")
        plt.imshow(wordcloud)
        plt.show()

        ## Bar graph of top words
        plt.bar(range(len(total_word)), [val[1] for val in total_word], align='center')
        plt.xticks(range(len(total_word)), [val[0] for val in total_word])
        plt.xticks(rotation=70)
        plt.show()

