from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis = TextBlob("Garvita is sweet")
# #print(dir(analysis))
print(analysis.translate(to='hi'))
# # print(analysis.tags)
# print(analysis.sentiment)       #negative sentence: negative polarity and positive: positive polarity



# pos_count = 0
# pos_correct = 0
#
# with open("positive.txt","r",encoding = "ISO-8859-1") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.subjectivity > 0.9:
#             if analysis.sentiment.polarity > 0:
#                 pos_correct += 1
#             pos_count +=1
#
#
# neg_count = 0
# neg_correct = 0
#
# with open("negative.txt","r",encoding = "ISO-8859-1") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.subjectivity > 0.9:
#             if analysis.sentiment.polarity <= 0:
#                 neg_correct += 1
#             neg_count +=1


#Now Taking idea from vader and assuming polarity range between -0.5 and 0.5
# pos_count = 0
# pos_correct = 0
#
# with open("positive.txt","r",encoding = "ISO-8859-1") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#
#         if analysis.sentiment.polarity >= 0.5:
#             if analysis.sentiment.polarity > 0:
#                 pos_correct += 1
#             pos_count +=1
#
#
# neg_count = 0
# neg_correct = 0
#
# with open("negative.txt","r",encoding = "ISO-8859-1") as f:
#     for line in f.read().split('\n'):
#         analysis = TextBlob(line)
#         if analysis.sentiment.polarity <= -0.5:
#             if analysis.sentiment.polarity <= 0:
#                 neg_correct += 1
#             neg_count +=1
#
#
# print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
# print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# '''
# POS tag list:
# CC  coordinating conjunction
# CD  cardinal digit
# DT  determiner
# EX  existential there (like: "there is" ... think of it like "there exists")
# FW  foreign word
# IN  preposition/subordinating conjunction
# JJ  adjective   'big'
# JJR adjective, comparative  'bigger'
# JJS adjective, superlative  'biggest'
# LS  list marker 1)
# MD  modal   could, will
# NN  noun, singular 'desk'
# NNS noun plural 'desks'
# NNP proper noun, singular   'Harrison'
# NNPS    proper noun, plural 'Americans'
# PDT predeterminer   'all the kids'
# POS possessive ending   parent\'s
# PRP personal pronoun    I, he, she
# PRP$    possessive pronoun  my, his, hers
# RB  adverb  very, silently,
# RBR adverb, comparative better
# RBS adverb, superlative best
# RP  particle    give up
# TO  to  go 'to' the store.
# UH  interjection    errrrrrrrm
# VB  verb, base form take
# VBD verb, past tense    took
# VBG verb, gerund/present participle taking
# VBN verb, past participle   taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present  takes
# WDT wh-determiner   which
# WP  wh-pronoun  who, what
# WP$ possessive wh-pronoun   whose
# WRB wh-abverb   where, when
# '''
