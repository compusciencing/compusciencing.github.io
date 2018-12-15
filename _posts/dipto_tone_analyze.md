---
layout: post
title:  "Tone analysis of text!"
categories: ["Missouri State University"]
tags: ["csc799"]
author: "Dipto Das"
---

# Tone Analysis with IBM Tone Analyzer

At first let's ask the question, what is the benefit of using **tone** information instead of **sentiment** information in text analysis or natural language processing?

There are several popular sentiment analysis tools out there like Vader sentiment analyzer, TextBlob, and etc. They each have their own way to represent sentiment. For example, TextBlob sentiment analyzer gives a positive sentiment value and a negative sentiment value whereas Vader sentiment analyzer gives a positive, a negative, a neutral, or a compound (i.e. aggregated) sentiment score. All of these suggest the overall polarity of the sentiment. However, none of these has a way to distinguish among the positive emotions and negative emotions. For example, both sadness and anger are negative emotions, but there is an obvious distinction between them and they are often clearly distinguishable by human from written text. IBM Watson tone analyzer is a tool for estimating the emotional scores from text so that we can differentiate among emotions in negative sentiments and positive sentiments.

The IBM tone analyzer gives a sentence-wise score in a scale of 0 to 1 representing different aspects of the text. What do I mean with different aspects? This tool gives values of three aspects - emotions, language, and social - for any sentence supplied to it. Isn't it fascinating? Huh! This tool is based on linguistic behavior and psychological theories.

The emotion score in the IBM Tone Analyzer represents the likelihood of a sentence to convey one of the following five emotions: anger, fear, disgust, joy, and sadness. These are a subset of the seminal classification of emotions by Ekman and Plutchik. The score is derived from a stacked ensemble framework. That means it combines predictions from many lower level models under a high level hood to achieve better performance. Examples of these low level features include: n-grams (unigrams, bigrams, and trigrams), punctuations, emoticons, curse words, greetings, and last but not the least sentiment polarity scores as we get from Vader or TextBlob. The high level hood uses a constrained optimization approach that is designed to handle co-occurances of multiple emotions and noisy data. Thus, it becomes applicable for text we usually come across including on social media.

In the same way, language and social scores were calculated with analysis of learned features. Language scores evaluate three qualities in the words of a sentence: analytical, tentative, and confidence. As the names of the categories suggest, analytical scores represents the amount of reasoning and technical words in the sentences, tentaive scores shows the amount of doubt in text, and confidence scores represent the degree of certainity in the text. In order to test the system's performance, IBM tone analyzer used crowdsourcing on a platform named CrowdFlower. The system achieved F1-score of ~0.7 with respect to experts' annotations.

The social scores indicate the likelihood of a sentence having the characteristics of the Big Five personality model: openness, conscientiousness, extraversion, emotional range, and agreeableness. Openness indicates the property of being open to new ideas; conscientiousness indicates the property of being methodical and organized; extraversion means the tendancy of finding stimulation with others; emotional range (a.k.a. neuroticism) represents the extent to which emotion conveyed 
in the text shows sensitivity or stability; and lastly, agreeableness is the tendancy of being compassionate.

So, important question is where we can use it? We can use this tool to analyze text where there is context involved. Well, those who advocate for n-grams can argue here that it is already done in their way. Let me give you an example.

Paragraph 1: It is a rainy day. Do I really need to out today?

Paragraph 2: It is a rainy day. School going kids are happy that their classes got canacled.

Paragraph 3: It is a rainy day. The humidity was very high and the large difference in atomspheric pressure flew the clouds towards the city causing the rain.

Now, tell me does n-gram on first sentence give you enough information about the context?

I rest my case here. To know more about the IBM tone analyzer their official documentaion is a good start. They got APIs in popular languages. And the best thing is, though it is a paid service, you get 3,000 API calls per month for free. That, I think, is enough for research purpose and for playing around with it.
