---
layout: post
title: "Proposal: Stock Analysis with Neural Networks"
tags: ["csc596", "stocks", "neural network", "machine learning", "msu"]
author: "Alex Wilson"
---

With the help of Dr. Anthony Clark, I plan to implement a neural network to "predict" the stock price of Google (GOOG) using historical stock information from January 1st, 2014 - January 1st, 2019. I will collect the data using the [Yahoo Finance API]( https://rapidapi.com/apidojo/api/yahoo-finance1). I plan to write the program using [Python 3.6](https://docs.python.org/3/whatsnew/3.6.html) and will use [Keras]( https://keras.io/) as a high-level framework using [TensorFlow 1.1]("https://www.tensorflow.org/") as the low level library. Accurately predicting stock prices is considered very difficult. 

The [Efficient Market Hypothesis]( https://en.wikipedia.org/wiki/Efficient-market_hypothesis), developed by Eugene Fama and Benoit Mandelbrot, states that all stocks are traded at an efficient or real price because all the people competing against one another. Any kind of exclusive information that one party possess is immediately accounted for by the price. This theory has yet to be disproven.

[High Frequency Trading]( https://en.wikipedia.org/wiki/High-frequency_trading) enables machines to directly impact the market by selling, buying, and cancelling massive orders many times a second. Many believe this directly violates at least some assumptions in the Efficient Market Hypothesis. Is it possible, using enough stock data, that it would be possible to model these trades and the market? Very little public information is available on this topic. 

This implementation will be a conventional neural network which means the topology of the network will not change. I will define the topology from manual feature extraction based on the training data set. The data that the neural network will learn from will include previous closing price, previous opening, current opening price, volume, market cap, and running average stock price. Ideally the closing price for the current day will be the output, but even predicting the direction from the opening price is useful because I could use it to predict a profit or loss. Because I will not be at Missouri State over the summer, I plan on maintaining regular communications with Dr. Clark over Skype, Missouri State Email, and [codeshare.io](https://codeshare.io/). I plan on sharing my code with Dr. Clark. 
