---
layout: post
title: "Proposal: OGP Weather Simulation"
tags: ["csc596", "game engine", "simulation", "omega gaming project", "proposal", "weather"]
author: "Gage Coates"
---

# Weather Simulation

 Weather is an integral part of any ecosystem, and as such it is a major component in the [Omega Gaming Project (OGP)](https://www.omega-gaming-project.org). Weather simulations typically deal with common aspects of the atmosphere such as pressure, air velocity, humidity, temperature, etc. They employ a process called ‘advection’ to transport air along a velocity field, and there are three primary methods for carrying out this process, namely Eulerian, Lagrangian, and Semi-Lagrangian. From the Eulerian perspective, the observer may ask how much of a fluid has passed through a given volume of space. Conversely, the Lagrangian perspective follows a single particle along its path through a velocity field. Semi-Lagrangian advection combines the previous two in such a way that the velocity field can be discretized into regular parcels of air, while advection is carried out by tracing the path of virtual particles that move between parcels.

I will attempt to implement a comprehensive weather simulation by using the aforementioned advection methods, and research into numerical weather simulation techniques. I find this type of computer science immensely interesting because of the unexpected and beautiful results that arise from modeling complex natural systems with such simple and elegant equations. As I have found in the past, the challenge here is keeping the simulation numerically stable, while also preserving natural phenomena like compression waves and vortices.

## Goals

* Stable advection of air
* Prevent advection through the terrain
* Model the following properties
    * Pressure
    * Temperature
    * Humidity
    * Velocity
* Water cycle
    * Evaporate ground water into the atmosphere
    * Precipitate humid air into rain that collects on the terrain
    * Update the groundwater simulation to run in realtime
* Model heating and cooling of air contacting the terrain
* If time permits, look into parallelizing the simulation on the GPU

## Value

Working through this problem will not only yield valuable insight into fluid simulations, but also push OGP closer to a holistic world simulation. I am quite interested to see developing weather patterns affect erosion, plants, and future animal populations. Of all the possible processes to model, I see weather as bringing the project the most value at present. Without a rich simulation of the water cycle and temperature variation, many other systems that rely on such characteristics are unrealistically homogeneous.
