---
layout: post
title: "Report: Design, Implementation, and Optimization of Neural Networks"
tags: ["csc596", "artificial neural networks", "genetic algorithms", "tank game", "omega gaming project", "report"]
author: "Anthony Harris"
---

Artificial Neural Networks (ANNs) are a form of artificial intelligence (AI) that are widely used in supervised learning tasks; they, as well as their variants, excel in tasks such as image and voice recognition. I intend to use them in a slightly different manner.

Using data abstraction and other process minimization techniques, my goal was to develop a novel ANN that could interpret and respond to an environment in a game scenario in a way that more closely resembles a human player; such an ANN would represent the [Omega Gaming Project's (OGP)](https://www.omega-gaming-project.org) proposed AlphaNet. This task was particularly challenging given the complexity of the problems I attempted to solve, but progress was made nonetheless.

All project development was done in C#, using the Visual Studio 2019 IDE and GitHub for source control.

# Project Outline

The project can be divided into 3 major categories:
- Tank Game Development
- Neural Network Design
- Genetic Algorithm Design

The game rendering and logic categories refer to the design and implementation of a simple tank game. These tasks consumed approximately half of the total project development time but allowed me to work in an environment that I had complete control over; this was desirable as I was able to manipulate the rules of the world as necessary in the following stages.

# Tank Game Development

![Initialized State](/assets/2019-12-16-report-design-implement-optimize-neural-nets/initial-state.png)

*Figure 1: Initialized State*

## Rendering

Before I could focus on the AI side of things, I had to design a world that I had complete control over. As such, it seemed appropriate to design a tank game. The rules of the game are simple: the objective is to survive and kill the enemy tank. Graphics, however, are not my strong suit, and posed a bit more of a challenge than I had originally anticipated. 

The game is rendered in a C# form, using a split panel for the general window structure, with text in panel 1 for data display and a bitmap in panel 2 for graphic display. The image above displays the game in its initialized state. Notice the information panel on the left contains a variety of information about both the current game and the global population. The map is defined as a 25x25 arena, where the gray tiles represent unbreakable walls, the black tiles represent a floor, and the white tiles represent the spawn points of the tanks. This information is saved in a JSON file and is loaded upon execution of the game.

```text
JSON Map Representation:

    "grid":[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,1], //middle
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	]
```

This format was used because it allows for an easy means of defining new maps, as well as the introduction of new elements into an existing map. Note that the 1s represent the wall tiles, 0s represent floor tiles, and the 8 and 9 represent the spawn points for the red and blue tanks respectively.

## Logic

After getting the game to render appropriately, it was time to focus on the logic. 

In the interest of simplicity, I restricted the movement to a tile-by-tile basis. That is, the tanks move in a very discretized manner as opposed to smooth, continuous movement. Furthermore, tank and turret orientations are restricted to the 4 cardinal directions: North (Up), East (Right), South (Down), and West (Left). This allowed for simpler in-game logic, although I would argue that it resulted in more challenges in the AI portion, as ANNs tend to perform better in continuous environments. I also restricted each tank to only having up to 2 missiles on the field at any given point. This was partly in the interest of simplicity, but was largely due to the AI. I hypothesized early on that the AI would simply spam missiles indefinitely in an attempt to win, and this helped prevent that from the start.

At the inception of the tank game, my goal was to allow a player to play against the AI, so I needed a means of standardizing the tank "controllers". I accomplished this by implementing an enumerated type to represent the different possible commands, as well as a player controller method within the player class to handle said commands. The following code snippet demonstrates the simple design of the tank command portion of that method.

```c#
//Player Controller Implementation

    public void playerController(ControlCommand tankCommand, ControlCommand turretCommand)
		{
			switch (tankCommand)
			{
				case ControlCommand.NONE:
					break;
				case ControlCommand.Up:
					velocity.x = 0;
					velocity.y = -1;
					tankOrientation = Orientation.North;
					break;
				case ControlCommand.Right:
					velocity.x = 1;
					velocity.y = 0;
					tankOrientation = Orientation.East;
					break;
				case ControlCommand.Down:
					velocity.x = 0;
					velocity.y = 1;
					tankOrientation = Orientation.South;
					break;
				case ControlCommand.Left:
					velocity.x = -1;
					velocity.y = 0;
					tankOrientation = Orientation.West;
					break;
			}
			// Another switch for turretCommand
		}
```

This method allows human and AI players to interact with the world in the same way, and also allows for parallelization, which becomes important in the AI portion.

# Neural Network Design

One of the most important goals of this project for me was to begin the development of an ANN library. I am reluctant to use existing libraries as I feel that there is more for me to gain academically by developing my own.

The initial data structure of the implemented ANN can be defined as a simple list of edges, where each edge simply contains an input and output neuron ID, a weight, and a bias. This data structure is incredibly simple and easy to understand, but poses some challenges when modifying the structure of the ANN, as I ended up doing. As such, I moved to a more robust, albeit complicated, data structure that can be defined as a dictionary of dictionaries of edges, where the input neuron ID is the key to the outer dictionary and the output neuron ID in the key to the inner dictionary, keeping the same edge definition as mentioned prior. Each of these data structures were designed with the invaluable assistance and recommendations of Gage Coates, and I credit him as such.

The tank game, as it stands at the time of this post, is currently a somewhat messy combination of the two above ANN designs. This is the case due to the time constraints of the project; the first ANN design was fully implemented in the game before the issues with its structure arose. As opposed to fully redesigning the already implemented AI constructs, I simply did the patchwork necessary to reap the benefits of both ANN structures. This is less than ideal in a good practice sense, but yielded the desired results in far less time than a full revamp. For future projects, however, the double dictionary approach will be utilized exclusively.

The inputs to the ANN are currently the angle and distance to the enemy, as well as the angle and distance to the nearest enemy missile, with the outputs simply being a command that is passed to the player controller. The ANN is initialized to the most simple ANN possible given these inputs and outputs: it is simply an input layer consisting of 4 neurons, and an output layer consisting of 10 neurons (5 each for tank and turret commands, including a NONE option for each).

# Genetic Algorithm Design

ANNs tend to be best represented in supervised learning tasks; as such, I quickly had to consider whether winning the tank game could be defined as supervised learning or not. There is an argument to be made that it could be defined as such using the Imitation Learning technique, but this technique is very data dependent, which requires more time than allowed by the scope of this project. As a result, I chose to pursue an alternate approach: Neuro Evolution of Augmenting Topologies (NEAT).

At its core, NEAT is simply a hybridization of ANNs and Genetic Algorithms (GAs) that allows for the alteration of the core structure of the ANN. That is, the number of neurons and the connections between neurons are subject to change, as well as the weights and biases. While this method can be somewhat slow at times due to the randomness factor that is introduced, it offers a means of using ANNs without an enormous amount of data dependency.

## General GA Information

My implementation of the GA focuses on rapid evolution, largely due to the small scale of the project. Given time, it would be a simple matter to transition from the rapid evolution phase into a more steady rate of evolution, but my primary goal was to get results sooner rather than later, so evolving early and often seemed to offer more promise. I used a population size of 500 ANNs, each assigned randomly to a game at every generation. The games are all run in parallel using the C# System.Threading.Tasks library, resulting in 250 games run simultaneously. After each game has concluded, the fitness is calculated for each ANN, and the bottom 90% of the population are replaced with offspring generated via crossing over and mutation, as defined in the section below. 

At the time of this post, the game that contains the most fit individual from the population is rendered to the screen. This slows down the iterations considerably, but offers a visual representation of the progress being made. I have a means of only rendering every n iterations, but that n is currently set to 1. Increasing n drastically increases the number of iterations per second, as there is then no extra overhead.

## Crossing Over

As with the standard implementation of GAs, I implemented a crossover function that crossed the traits of 2 "parent" ANNs and produced an offspring. My implementation is somewhat different, however, in that it biases the offspring toward the traits of the more fit parent. That is, when crossing the parents, I define the topology of the offspring to match the topology of the more fit parent, and then each matching edge is a 60/40 contribution split in favor of the same parent. I did this in the hopes of maintaining an acceptable level of diversity, while simultaneously reducing the time required to find an optimal solution.

## Mutations

The mutations I defined in the tank game are as follows: add a new edge, remove an existing edge, add a new neuron, change the weight of an edge, and change the bias of an edge. I chose not to remove neurons simply because the removal of an edge would have the same effect and it seemed redundant in the face of my time constraints. Each mutation type has an equal chance of occurring, which would be an area of improvement and/or adjustment for future work.

## Fitness Function Engineering

GAs require the developer to define a metric that measures how well a given solution performs. This metric is called the fitness function. The fitness function is arguably the most influential aspect of GAs, but they also represent the greatest challenge.

During the testing phase of this project, I defined and tested a multitude of fitness functions. Each function represents an attempt to define the best description of the task to be solved, and each yielded unique results. There were a few test fitness functions implemented to determine if the GA implementation performed as expected, for example, fitness = number of missiles fired. Each test fitness function was a simple function, similar to the aforementioned number of missiles function, and each yielded the expected results, thus supporting the GA implementation. 

Challenges arose when I started implementing more complex fitness functions; functions that added a major win bonus to the fitness were still reliant upon some prioritization of moving and firing missiles. I implemented several functions that aimed to maximize the distance between the ANN in question and the nearest enemy missile while simultaneously minimizing the distance between the enemy and the nearest friendly missile, each to no avail. There were few cases where I would see realistic play for a short period of time, but the ANNs tended to perform in one of 3 ways: they would both do exactly nothing, they would both spam missiles, or one would chase the other around the map. 

# Conclusion and Future Work

This project has been an invaluable source of growth and learning for me as both a software developer and a computer scientist. While I was unable to obtain the results I had initially intended, the enormous amount of insight and understanding of the challenge of human-like AI, as well as the experience with C#, that I obtained will be utilized in future projects. This project could be improved in multiple ways, however.

1.  An overall code cleanup and transition fully into the double dictionary ANN implementation would drastically increase the quality of the project.
2. Transitioning into a continuous world space is necessary for improved ANN performance.
3. Altering the rate at which each mutation occurs would improve the overall evolution of the ANNs.
4. Further research into an appropriate fitness function could yield one that sufficiently defines the desired goal.

This project is available on GitHub at [Tank Game](https://github.com/KillerBOB999/TankGame.git).
