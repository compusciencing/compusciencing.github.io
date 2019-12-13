---
layout: post
title: "Report: OGP Engine Development"
tags: ["csc596", "game engine", "simulation", "omega gaming project","report"]
author: "Gage Coates"
---

# Omega Gaming Project Overview

The [Omega Gaming Project (OGP)](https://www.omega-gaming-project.org) provides a large number of possible domains to work in, especially those suited for 3D graphics and simulation. As such, the developments in this report vary widely and are in no way representative of a final version of the project.  

## Game

As a game, the player can explore a uniquely different world as often as they like. This world contains a single continent (~4km x 4km) that is populated with dynamically simulated plants, animals, and A.I. controlled NPCs. When a world is created, the initial continent is passed through millions of years of erosion, and gradually populated with evolving plant and animal life. A seed number is used to derive this initial continent, allowing players to start over with the same initial conditions. Once the player interacts with the world, a unique state will emerge that is distinctly unique from any other

## Procedural Content

Due to the ever increasing high budget nature of game development, this project aims to maximize the number of computer generated (procedural) plants, animals, rocks, terrain, textures, quests, names, etc. Content generating algorithms are based on principles that are observed in nature, such as the processes of erosion on terrain, and the gradual adaptation of organisms to their environment through evolution.

## Simulation

Rather than generating the game world at astronomical scales, our approach is to simulate more detail in the confined space of a single continent. Everything from basic newtonian physics to the genetic evolution of plants will be simulated, creating a living world that is always changing. This low level simulation leads to complex emergent patterns that were never explicitly defined. Examples include: the formation of rivers, biomes, plant and animal specialization, cities, road networks, and social networks.

## Artificial Intelligence

Conventional A.I. systems are simple decision trees that require attention to detail and careful consideration of edge cases. These types of A.I. are predictable and can only handle one type of environment. We aim to provide a more general purpose A.I. that interacts with the game and player in a believable and un-planned manner. Since a designer is not explicitly prescribing content, the narrative is primarily driven by each player's experience and decisions.

# Key Developments

## Terrain Strata

The terrain is represented by a 2D array of floating point values that represent the height of each vertex in the terrain mesh. This data structure was extended to maintain a strata of materials, namely grass, dirt, and stone.

## Construction Mechanics

Agents (including the player) are able to manipulate objects by picking them up and placing them in or above the ground. Placing items in the ground will anchor them in place.

## New Content

Sticks

Small stone

Hay

## Plant Simulation

A basic plant simulation controls plant growth, genes, and reproduction. Every update tick calculates each plant's external resources. Resource transformations then convert Light and water into sugar which the plant uses to either grow or generate seeds. There are several types of leaves that exhibit different performance characteristics with respect to temperature.



## Improved Data Access Patterns

The Idea in a nutshell is that you have a query signature composed of a Read mask, Write mask, and Region set. When a thread executes a task, it grabs a lock on this signature; if there are read/write conflicts the Region set is checked for intersection to determine if there really is a conflict. When a signature is released, all other blocked threads are notified and attempt to grab a lock on their signature
Read mask and Write mask
A 64 bit integer, where each bit is a flag for a specific component type, be it Position, Movement, Plant, etc.
Region set
An unordered set of regions, where each region is a unique predefined spatial grid square within the world (right now they are 64m x 64m)
Example usage:




# Future Work