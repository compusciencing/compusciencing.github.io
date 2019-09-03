---
layout: post
title: "Design, Implementation, and Optimization of Neural Networks Proposal"
tags: ["csc596", "ai", "neural networks", "proposal", "msu"]
author: "Anthony Harris"
---

This project will focus on the development, implementation, and optimization of [Artificial Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (ANNs) in at least 2 sub projects of the [Omega Gaming Project](https://www.omega-gaming-project.org/). I will base the ANNs on the principle ideas behind the AlphaNet design of AI, which will be implemented in the Omega Gaming Project. In short, the goal of the AlphaNet design is to minimize the amount of processing power required by a neural network while maximizing human-like information processing by the abstraction of data to a binary state where possible.

## Legibility of Randomly Generated Words 

Initially, I will take an existing random word generator and determine whether a given word is *legible* using an ANN. Then, I will optimize different ANN variants and grade their fitness based on the “confidence” of the output and the time taken to process. Given success, this also provides an opportunity to compare the results of individual variant optimization to the optimization methods found in the [Neuro-Evolution of Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)(N.E.A.T.) method. 

Potential expansion of this sub-project might include the determination of legibility using different languages as a point of reference as opposed to just English.

## Application of Data Abstraction in a Game

After showing a sufficient level of accuracy in legibility determination, I will move to the design, implementation, and optimization of a similarly structured ANN with the goal of applying continuous application in a simple tank game. The objective of this game is to defeat your opponent by hitting them with a rocket and the gamespace is a simple block-based map with indestructible walls channeling player movement. This game is limited to cardinal directionality (North, East, South, and West) for the sake of simplicity, but the data could just as simply be abstracted to omnidirectional angular values for the purposes of the ANN. 

Ideally, I’d expect to have the tank game fully functional by that point in time, but it is still in development. If it is not finished yet, I may dedicate time to the completing the game.

Potential expansion of this sub-project might include the addition of new mechanics like destructible walls, power-ups, and skills.

## Closing:

The opportunity to have dedicated time to research these topics is invaluable. Not only does this give me the experience needed to be prepared for an AI-reliant workforce, but this also gives me experience with the abstraction of data into a form that is more universally applicable. I would say this research will be the foundation upon which the AlphaNet AI is built.
