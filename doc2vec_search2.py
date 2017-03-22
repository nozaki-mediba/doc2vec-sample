#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab
import doc2vec
from gensim import models
import linecache

DOC_PATH = './search_target/{0}.txt'
# DOC_PATH = './search_target/article/{0}.txt'
# DOC_PATH = './parsed_data/{0}.txt'

model = models.Doc2Vec.load('doc2vec.model')

# 似た文章を探す
def search_similar_texts(path):

    print("==入力=================================")
    print(path)
    print(linecache.getline(path, 1))
    linecache.clearcache()

    print("==結果=================================")
    most_similar_texts = model.docvecs.most_similar(path)
    for similar_text in most_similar_texts:
        print("-------------------------")
        print(similar_text[0])
        print(linecache.getline(similar_text[0], 1))
        linecache.clearcache()


if __name__ == '__main__':
    print('記事:')
    article = input()
    print()
    search_similar_texts(DOC_PATH.format(article))
