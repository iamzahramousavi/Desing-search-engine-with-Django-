# -*- coding: utf-8 -*-
"""nlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r15A7en3Df1uuDQGFXKLIDwgXdlzyiC2
"""

pip install hazm

pip install persian

pip install pytrie

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import string
import persian
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
import hazm
from nltk.stem.lancaster import LancasterStemmer
from pytrie import StringTrie
OurPunctuation = string.punctuation
from hazm.Stemmer import StemmerI

"""#Read json file and convert to csv"""

df=pd.read_json("/content/drive/MyDrive/news_article.json")
df.to_csv("/content/drive/MyDrive/news_article.csv")
df=pd.read_csv("/content/drive/MyDrive/news_article.csv")
df.head(10)

class Normalization:
  def __init__(self,text,word,data,headername):
     self.text=text
     self.word=word
     self.data=data
     self.headername=headername
  def duplicated(self):
    df=self.data.drop_duplicates(subset=self.headername)
  def HazfEmoji(self):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', self.text)

  def HazfAlaem(self):
    #lowrCase
    result = self.text.lower()
    #حذف اعداد
    result=re.sub(r'\d+','', result)
    #حذف punctuation
    result = re.sub(r'[^\w\s]|\n|_','', result)
    return result

  def RisheGiri(self):
    stemmer=hazm.Stemmer()
    stm=stemmer.stem(str(self.word))
    return stm

  def Sentence_Tokenization(self):
    informal_normalizer=hazm.InformalNormalizer()
    normalized_informal_sample_text=informal_normalizer.normalize(self.text)
    return normalized_informal_sample_text

  def Word_Tokenization(self):
    wordtokenizer=hazm.word_tokenize(self.text)
    lexicaltokens=wordtokenizer.tokenize(self.text)
    return lexicaltokens

  def Normalize(self):
    index=0;
    for i in df[self.headername]:
        df[self.headername].loc[[index]]=persian.convert_ar_characters(str(i))
        df[self.headername].loc[[index]]=persian.convert_ar_numbers(str(i))
        df[self.headername].loc[[index]]=persian.convert_en_characters(str(i))
        df[self.headername].loc[[index]]=persian.convert_en_numbers(str(i))
        df[self.headername].loc[[index]]=HazfEmoji(str(i))
        df[self.headername].loc[[index]]=HazfAlaem(str(i))
        index=index+1
    return df
  def normal_2(self):
    index=0
    normalizer=hazm.Normalizer()
    for i in df[self.headername]:
      df[self.headername].loc[[index]]=normalizer.normalize(str(i))
    return df

obj=Normalization()

"""#convert to json"""

path_csv=r' '
d=pd.read_csv(path)
d.to_json('')