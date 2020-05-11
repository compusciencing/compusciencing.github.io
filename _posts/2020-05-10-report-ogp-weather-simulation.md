---
layout: post
title: "Report: OGP Weather Simulation"
tags: ["csc596", "game engine", "weather", "simulation", "omega gaming project", "report"]
author: "Gage Coates"
---

# Weather Simulation in OGP

## Omega Gaming Project Overview

The [Omega Gaming Project (OGP)](https://www.omega-gaming-project.org) provides many domains to work in, especially those suited for 3D graphics and simulation. As such, the developments in this report vary widely and are in no way representative of a final version of the project.  

## Weather Simulation

Since OGP aims to provide many physically based simulation systems, it makes sense to introduce a way of handling atmospheric attributes like pressure, temperature, humidity, and wind. To accomplish these tasks, I first prototyped serveral of my own ideas, then conducted research into fluid simulations that model [Navier–Stokes equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations). The following sections cover my progression through implementing various fluid simulation techniques in javascript.

## Elastic Particles

I implemented an initial approach of representing atmosphere volumes as large elastic particles that need only repulse eachother to give the effect of gravity induced pressure and temperature. Unfortunately, this approach leads to rigid crystalline configurations under high pressure - this can be
seen at the bottom of Figure 1.

`Figure 1. A 2D profile of an atmosphere represented by elastic particles`
![Particles](/assets/2020-05-10-report-ogp-weather-simulation/particles.gif)

## Conservative Semi-Lagrangian Advection Research

Looking for a continuous solution to the problem of representing air movement, I read and implemented the following advection scheme presented in this paper:

An Unconditionally Stable Fully Conservative Semi-Lagrangian Method (2010)
by Michael Lentine∗ , J´on T´omas Gr´etarsson∗ , Ronald Fedkiw∗ 
http://physbam.stanford.edu/~fedkiw/papers/stanford2010-01.pdf

`Figure 2. Conservative advection of air through a constant velocity field`
![Advection](/assets/2020-05-10-report-ogp-weather-simulation/advection.gif)

I then proceeded on the implementation of incompressible fluid pressure equations, however I was unable to solve specific stability issues in my implementation - these can be seen as "checkerboard" patterns in Figure 3. where pressure quantities are oscillating at a high frequency.

`Figure 3. Introducing pressure at various locations`
![Pressure](/assets/2020-05-10-report-ogp-weather-simulation/incompressible.gif)

## Another Approach to Solving the Navier–Stokes Equations

Once again, looking for simple and well written literature, I came across the following paper: 

Cline, David & Cardon, David & Egbert, Parris. (2020). Fluid flow for the rest of us: Tutorial of the marker and cell method in computer graphics. https://www.researchgate.net/publication/228964362_Fluid_flow_for_the_rest_of_us_Tutorial_of_the_marker_and_cell_method_in_computer_graphics.

Implementation required solving large sparse matrix equations in the form Ax=b. I chose to use the [math.js](https://mathjs.org/) javascript library for this task. The end result of my implementation can be seen in Figure 4, where I introduce an artificial upward force into the velocity field. The matrix solver is attempting to satisfy the condition of zero divergence, this means velocities must be adjusted so there are no regions where air is created or destroyed - this is also what gives rise to the vortices that you see.

`Figure 4. Particles (blue) are advected according to the velocity field (white lines), with pressure visualized as red`
![Pressure](/assets/2020-05-10-report-ogp-weather-simulation/fluid-flow.gif)

Taking the existing framework forward with my goals of representing atmpospheric phenomena like the buoyancy of warm air, I introduced a temperature quantity that advects according to the velocity field, but also generates a slight bouyant force on the velocity field when there is a sufficient temperature gradient. This can be seen in Figure 5.

`Figure 5. Warm air rising and carrying particles with it`
![Pressure](/assets/2020-05-10-report-ogp-weather-simulation/temperature.gif)

## Transferring to the 3D Environment of OGP

The process of taking what I learned from the prototyping phase to the final 3D representation in the OGP engine was quite straightforward thanks to the generalizations used in the origional paper. The simulation is stable in 3 dimensions and responds to external forces like those being introduced in Figure 6. Since the engine is written in C++, I opted to use the highly regarded [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) matrix library for solving the very large matrices involved.

`Figure 6. Velocity field visualized in the 3D environment of OGP`
![Pressure](/assets/2020-05-10-report-ogp-weather-simulation/3d-velocity-field.png)

## Future Work

I plan to continue improving the functionality of this atmosphere system given I now have a solid understanding of the equations that make it work. Future improvements include: the addition of humidity generated by standing water, precipitation generated by condensing humidity, and heating of the air from the ground.
