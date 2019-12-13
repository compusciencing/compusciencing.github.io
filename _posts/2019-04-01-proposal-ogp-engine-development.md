---
layout: post
title: "Proposal: OGP Engine Development"
tags: ["csc596", "game engine", "simulation", "omega gaming project", "proposal", "msu"]
author: "Gage Coates"
---

# Overview

I plan on working through the design and implementation of game systems, mechanics, and optimizations in the current game engine for the [Omega Gaming Project (OGP)](https://www.omega-gaming-project.org). The foundation of the engine is largely complete, allowing for modular systems, assets and game entities to be designed, tested and iterated upon. The largest takeaway of this self-study from a learning perspective is understanding how to pragmatically and efficiently implement these systems in such a way that the end goal of the project is satisfied. In addition to this, I will better understand how to provide a good user experience within the game environment. While the course will help fulfill CS credit requirements, it also provides structured development that enforces deadlines that would otherwise not exist. Having this opportunity to work on a project that I am passionate about in a professional setting is delightful and should be very productive.

## Specific Goals

* Construction mechanics
    *	Initial iterations
        * Allow the conversion of inventory resources to instanced geometry that is physically interactable – think prefabricated structures
    *	Late iterations 
        * May include modular construction systems that allow for more building permutations
* Resource gathering
    *	Initial iterations
        * Basic tools
        * will allow the user to harvest mineral, timber, and water resources from the environment
        * Harvested resources are transformed into inventory resources
    * Late iterations
        * Physical interactions between tools and resources can be modelled to allow for more accurate tool effectiveness
        * If tool design is A.I. controlled, possibly come close to some sort of tool evolution?
* Plant simulation
    * Initial iterations
        * Basic spreading and growth function based on available resources
    * Late iterations
        * A genetic model for defining all plant life
        * Use of Genetic Algorithms to simulate evolution of plants
* Atmosphere simulation
    * Initial iterations
        * Low resolution global simulation
        * Temperature advection (heat moving towards cold areas)
        * Humidity advection
    * Late iterations
        * High resolution localized simulation
        * Condensation
        * Evaporation


<blockquote> 
It is required that all systems that handle user input are also easily capable of handling input from an artificial agent
</blockquote>

___

## Current Engine

<blockquote> 
content (textures, 3D models, etc.) is subject to change
</blockquote>

An erosion and water advection algorithm is passed over a noise generated heightmap giving rise to emergent terrain features like rivers and lakes

![Some erosion](/assets/2019-04-01-proposal-ogp-engine-development/screenshot0.jpg)

Supports instanced geometry and multiple level of detail (LOD) assets that can be imported from the portable FBX file format, or generated from within the engine

![Instanced geometry](/assets/2019-04-01-proposal-ogp-engine-development/screenshot7.jpg)
