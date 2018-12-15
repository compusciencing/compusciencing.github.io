---
layout: post
title:  "Some nlp algorithms"
categories: ["Missouri State University", "ARCS"]
tags: ["CSC 799"]
author: "Dipto Das"
---

# Student t-test

Let me start by telling a story. There was a person named William Sealy Gosset. He worked at Guiness Brewery over a hundred years ago. He came up with a statistical test to show the difference between barley yield from two fields. When he wanted to publish the test, he was nervous, and instead of publishing it in his name, he used the pseudo name 'Student'. To this day, this test is known as Student's t-test instead of Gosset's t-test.

# What is t-test?
Imagine, you have two fields of same crops - field 1 and field 2. May be, you want to compare the productions of these two fields with respect to a certain criteria. However, obviously it's not wise to cut the crops from the whole fields for this. A test on samples from both these fields should be enough. Look at the following image:

![Different distributions from two fields](/images/ttest.jpg)

The top figure says that field 2 (indicated by blue line) has a higher mean than field 1 (indicated by green curve). But that just says a partial story. The fields can have different distributions as shown in other two figures. Depending on that, the crops from these two fields can have statistical differences or not. And that's where t-test becomes useful. We can see the t-value as a ratio between signal and noise. Signal means the numbers that can show the differences in two distributions, if any, and noise means the numbers that are just outliers. We can define signal as difference between group means and noise is the variability in the groups.

The formula that we are going to use:

t-value = |mean of field 1 - mean of field 2|/(variance of field 1/sample count of field 1 + variance of field 2/sample count of field 2)^0.5

A sample calculation is shown in the following google sheet: https://docs.google.com/spreadsheets/d/1H8ajhRR5SOqkcx3pBPHjA1LY76j8-mtNDsnGajFBrXM/edit?usp=sharing

The t-value here is 2.3 that means there is more signal than noise.

If we had a null hypothesis: "There is no statistically significant difference between the samples." That means any difference we find is just by chance. Hence, we need a critical value. If the our t-value is less than that we cannot reject the null hypothesis however if it is higher, we can reject the hypothesis and accept the alternative hypothesis.

Now, let's look at the t-value table.

![t-value table](/images/ttable.png)

The degree of freedom is calculated as: df = count of samples from field 1 + count of samples from field 2 - 2 = 16 + 16 - 2 = 30 in our case. Generally, in inferential statistics, p = 0.05 is widely used. We are going to use that same value. Therefore, the critical value for us will be 2.042. Our t-value is greater than critical value, thus, we can reject the null hypothesis and accept the alternative hypothesis: There is statistically significant difference between the crops from two fields.

We can use the function: ttest as well to calculate the p value directly that gives us p = 0.026 < 0.05 and we can accept alternate hypothesis.

What if the calculated p value is greater than 0.05? There is no significant difference. What if it is slightly greater like 0.06? There is nothing like provisionally rejected in t-test. It just says you that you might try to apply that as a feature to machine learning algorithm on them to classify. It might be helpful however it will not be decisive.
