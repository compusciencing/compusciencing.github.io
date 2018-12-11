---
layout: post
title:  "Some nlp algorithms"
categories: ["Missouri State University", "ARCS"]
tags: ["CSC 799"]
author: "Dipto Das"
---

# Word Embedding Models

Word embedding models are a modern approach of representing text in natural language processing. It is a way of representing a word in a dense vector space that is based on their meaning. It is an advancement on simple bag-of-words approach. Word embedding models are trained to be a fixed length dense and continuous valued vectors using a large corpus of text. Each word is represented by a point in the embedding space and these points are learned by moving around based on the words that usually surround that target word. In other words, a word is learned by the company it keeps that usually has "something" to do with the meanings of the words.

Let's see a very popular example.

If we know a pair of words that are from same group like (man, king) and we want to get a similar pair where we know one entry like this: (woman, ?).

A standard word embedding model would suggest a like queen as the answer. Because it is the closest word that can replace king when woman replace the word man.

Something like this: queen = (king - man) + woman

Popular word embedding models include word2vec model by Google, GloVe by Stanford. There are some unconventional word embedding models available as well like urban dictionary model. The model that you need to use depends on the application that you have in mind.

We can easily find already trained models for word2vec or Glove easily. However, you may need to develop/train the model from corpus at hand if you have a very specific application field in mind. For example, Google's word2vec model was trained with entire Wikipedia corpus. The basic idea is similar to n-gram approach that means we need a group of words at a time to get idea of the context of the use of the word. Here, I show a general step through approach for training your word embedding model in Gensim, a more matured natural language processing framework than natural language toolkit (NLTK) that comes readily with python.

```python
sentences = 'This is a small corpora'	#assume we fit all our corpus in a variable in memory
model = Word2Vec(sentences)

words = list(model.wv.vocab)	#vocabulary of the corpora
model.wv.save_word2vec_format('my_word_embedding_model', binary = True)
```

We can load a pre-trained model by using:

```python
model = Word2Vec.load('my_word_embedding_model')
```

If we have a group of words meaning similar thing and we know only one or two meaning the opposite, word embedding models can find the similar words; that can even specialized for our problem context if we chose to train our own word embedding models.
