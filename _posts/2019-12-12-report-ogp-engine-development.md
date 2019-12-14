---
layout: post
title: "Report: OGP Engine Development"
tags: ["csc596", "game engine", "simulation", "omega gaming project", "report"]
author: "Gage Coates"
---

# Omega Gaming Project Overview

The [Omega Gaming Project (OGP)](https://www.omega-gaming-project.org) provides many domains to work in, especially those suited for 3D graphics and simulation. As such, the developments in this report vary widely and are in no way representative of a final version of the project.  

## Game

As a game, the player can explore a uniquely different world as often as they like. This world contains a single continent (~4km x 4km) that is populated with dynamically simulated plants, animals, and A.I. controlled NPCs. When a world is created, the initial continent is passed through millions of years of erosion, and gradually populated with evolving plant and animal life. A seed number is used to derive this initial continent, allowing players to start over with the same initial conditions. Once the player interacts with the world, a unique state will emerge.

## Procedural Content

Due to the ever increasing high budget nature of game development, this project aims to maximize the number of computer generated (procedural) plants, animals, rocks, terrain, textures, quests, names, etc. Content generating algorithms are based on principles that are observed in nature, such as the processes of erosion on terrain, and the gradual adaptation of organisms to their environment through evolution.

## Simulation

Rather than generating the game world at astronomical scales, our approach is to simulate more detail in the confined space of a single continent. Everything from basic newtonian physics to the genetic evolution of plants will be simulated, creating a living world that is always changing. This low level simulation leads to complex emergent patterns that were never explicitly defined. Examples include: the formation of rivers, biomes, plant and animal specialization, cities, road networks, and social networks.

## Artificial Intelligence

Most conventional A.I. systems are simple decision trees that require attention to detail and careful consideration of edge cases. These types of A.I. are predictable and can only handle one type of environment. We aim to provide a more general purpose A.I. that interacts with the game and player in a believable and un-planned manner. Since a designer is not explicitly prescribing content, the narrative is primarily driven by each player's experience and decisions.

# Key Developments

## Terrain Strata

The terrain is represented by a 2D array of floating-point values that represent the height of each vertex in the terrain mesh. This data structure was extended to maintain a strata of materials, namely snow, grass, dirt, and stone. Other systems can interact with the terrain through this strata to create more realisitic behavior - examples include the plant system which uses soil depth, and the rendering system which renders the top strata with an appropriate texture.

## Construction Mechanics

Agents (including the player) are able to manipulate objects by picking them up and placing them in or on top of other objects. Placing items in the ground will anchor them in place.

`Construction`
![Construction](/assets/2019-12-12-report-ogp-engine-development/construction.jpg)

This mechanic is not limited to static structures, as it is possible to combine objects into one composite "tool" that can be carried. The simulation of tool interactions is covered later in this report.

## Plant Simulation

A basic plant simulation controls plant growth, genes, and reproduction. Every update tick calculates each plant's external resources, including: sunlight, water, temperature, and soil depth. Resource transformations then convert Light and water into sugar which the plant uses to either grow or generate seeds. There are several types of leaves that exhibit different performance characteristics with respect to temperature.

`Leaf performance as a function of temperature`
![Leaf performance as a function of temperature](/assets/2019-12-12-report-ogp-engine-development/leaf_functions.png)

`Plants`
![Plants](/assets/2019-12-12-report-ogp-engine-development/plants.png)

`Leaf specialization correlated to elevation. The atmosphere system generates a temperature variance across elevation, e.g. lower temperatures at higher elevations.`
![Leaf specialization correlated to elevation](/assets/2019-12-12-report-ogp-engine-development/plant_specialization.png)

## Simple Artificial Agents

As an experiment, simple neural nets were evolved using the NeuroEvolution of Augmenting Topologies (NEAT) method. Agents (red boxes) were given angle and distance to the nearest target (green spheres), while the fitness was determined by summing the number of collected targets.

`Population and agent fitness over time`
![Population and agent fitness over time](/assets/2019-12-12-report-ogp-engine-development/fitness.png)

`Agents`
![Agents](/assets/2019-12-12-report-ogp-engine-development/agents.jpg)

## Basic Tool Mechanics

For interactions between tools and resources to be modelled in a semi-realistic manner, a material representation was created to support common strength qualities of different materials.

`Material definition as seen in the OGP Asset Manager`
![`Material definition as seen in the OGP Asset Manager](/assets/2019-12-12-report-ogp-engine-development/material.png)

Every object in the world will have an associated material, and objects that have a mass lower than an agent's carrying capacity can be held. Tools are incidentally just the name given to the items that are held by agents - functionally there is no difference between a tool and an ordinary object in the world.

`Using a rock against a large plant`
![Using a rock against a large plant](/assets/2019-12-12-report-ogp-engine-development/tools.jpg)

## Mesh Slicing

As an attempt to further proceduralize tool interactions, work was made to develop a mesh slicing algorithm that can be used as a tool action. This mechanic is especially useful for cutting down trees and subdividing large resources into carryable sections.

`Slicing a complex mesh`
![Slicing a complex mesh](/assets/2019-12-12-report-ogp-engine-development/slice2.png)
![Slicing a complex mesh](/assets/2019-12-12-report-ogp-engine-development/slice1.png)

`Slicing a large boulder. Texture coordinates have not been calculated, leaving a monocolor surface`
![Slicing a complex mesh](/assets/2019-12-12-report-ogp-engine-development/slice3.jpg)
## Code Cleanup

### System Registration

Systems are this engine's bread and butter, so it makes sense for these areas to be concise and efficient. With the help of C++ Macros, it was possible to reduce code duplication in some key areas.

`Before`
![Before](/assets/2019-12-12-report-ogp-engine-development/systems_messy.png)

`After`

![After](/assets/2019-12-12-report-ogp-engine-development/systems_clean.png)

### Data Access

As systems access entity components, synchronization mechanisms must be im place to ensure thread safety when locking these resources for use. I have enhanced the primary locking pattern to include a set of regions—regions are large (64m by 64m) square spatial subdivisions of the world that do not overlap. In a nutshell, there is a query signature composed of a Read mask, Write mask, and Region set. When a thread executes a task, it grabs a lock on this signature; if there are read/write conflicts, the region set is checked for intersection to determine if there really is a conflict. When a signature is released, all other blocked threads are notified and attempt to grab a lock on their signature. Read and write masks are 64-bit integers, where each bit is a flag for a specific component type, be it Position, Movement, Plant, etc.

The region set is an unordered set of integer region IDs. 

`Example usage:`
![Example usage](/assets/2019-12-12-report-ogp-engine-development/data_access.png)

The advantage of adding this spatial component to the lock signature is increased parallelism. Because of the localized nature of all world systems, there is never a case where a system update requires a query that spans more than one region away. To illustrate this concept, consider the following diagrams.

`This grid represents regional subdivisions, where the red region is being written to by a system update, and the blue regions are only being read from.`
![Kernel](/assets/2019-12-12-report-ogp-engine-development/data_access_kernel.png)

Since it is possible to read the same memory location concurrently from multiple threads, the above "kernel" can be run concurrently with only one read region between. Given one thread per kernel, the number of global synchronizations that must take place is only 4.

`Pass 0`
![Example usage](/assets/2019-12-12-report-ogp-engine-development/data_access_0.png)

`Pass 1`
![Example usage](/assets/2019-12-12-report-ogp-engine-development/data_access_1.png)

`Pass 2`
![Example usage](/assets/2019-12-12-report-ogp-engine-development/data_access_2.png)

`Pass 3`
![Example usage](/assets/2019-12-12-report-ogp-engine-development/data_access_3.png)

# Future Work

OGP is an ongoing passion project that I will continue to pour time into when I can. The [website](https://www.omega-gaming-project.org) remains the most up-to-date source of information and will be the home of all available installations of the project. If you or anyone you know is interested in contributing, please email <omega.gaming.project@gmail.com>.