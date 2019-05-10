---
layout: post
title: "Web Simulator for Nybble"
categories: ["Missouri State University"]
tags: ["csc596", "robotics", "threejs", "cannonjs"]
author: "Saket Roy"
---

# Websimulator for Nybble

Working with Dr. Clark, I can define my research as the development of a web-based interface for quadruped gait simulation. Specifically, the aim of the research is to simulate a variety of gait patterns for the [Nybble](https://www.indiegogo.com/projects/nybble-world-s-cutest-open-source-robotic-kitten#/), an open-source robotic kitten. Hosted on [Github Pages](https://roy-05.github.io/websimulator/), I developed the project in pure HTML and JavaScript and used of the following libraries:

- [three.js](https://threejs.org): A lightweight cross-browser JavaScript library/API used to create and display animated 3D computer graphics on a Web browser.

- [cannon.js](http://www.cannonjs.org): A rigid body simulation library written in Javascript used to make objects move and interact in a realistic way. 

# Rendering the World

With no prior experience in computer graphics or physical simulation, it was initially quite difficult to wrap my head around how threejs and cannonjs worked. After spending the first few weeks watching [tutorials](https://www.youtube.com/watch?v=YKzyhcyAijo&t=560s) and reading through the extensive documentation provided by both libraries, the next step was render a world we could further populate with other graphic objects. Leveraging many functions from cannonjs, I created a world that abided by [Newton's laws of classical mechanics](https://en.wikipedia.org/wiki/List_of_equations_in_classical_mechanics#Kinematics) with relative ease. However, given that cannonjs is nothing but a physics engine, I still needed to handle the graphical aspect of our simulation. threejs was used to render the graphics of a ground plane. Next, by copying the position and orientation of the simulated cannonjs objects to the threejs objects with each time step, our graphics objects now moved around by the Newtonian physics defined in our engine, allowing us to simulate real-world interactions between graphical objects.

![Initial threejs ground plane](/assets/2019-05-09-web-simulator-final-report/world.jpg)

# Rendering the Nybble

Having created a proper graphical environment for our other objects to interact in, the next step was to render the Nybble itself. Studying this [video](https://youtu.be/ZX17mcpGfp8) carefully I began by modeling the graphics for the body, followed by the four limbs - each comprising an upper and lower limb. Rendering the individual pieces was not difficult as the body was simply a cuboid and the limbs were cylinders. What proved challenging, however, was figuring out the requisite constraints so that the eight cylinders and a cuboid could be assembled into the shape of a quadruped. Resolving this issue took a while, and there was a week of essentially no progress. Finally, Dr. Clark's technical expertise came to the rescue as he provided me with an example limb - two cylinders actuated with motors and a hinge constraint. Examining the code carefully, I was able to replicate it to produce four limbs and then use the hinge constraint logic to attach them to our cat body. The final rendition of our Nybble graphic object was as follows:

![Nybble graphic object](/assets/2019-05-09-web-simulator-final-report/default.jpg)

# Rendering the Gait

With all the hinges set up properly, the next step was to simulate motion. This was perhaps the hardest part of the project. It was easy to simulate motion, but it was not easy to produce a desireable walking gait. I spent hours dedicated to research - watching [simulations on gait pattern](https://www.youtube.com/watch?v=dRthdBr46cs), reading [scholarly articles](https://www.frontiersin.org/articles/10.3389/fncom.2014.00027/full), and experimenting with different gait patterns (Trot v. Creep). Dr. Clark further assisted me by providing me with code of a limb actuated to replicate knee-bend motion. Unfortunately, I was unable to convert those resources into a viable gait pattern; instead, we switched focus to developing the UI and as a result a gait pattern was never developed for Nybble and it remains a static object. 

# Rendering the UI

As the primary purpose of this project is to serve as an educational tool for simulation of quadruped gait patterns we focused on accomplishing certain UI features as well. Initial tasks were to add buttons to toggle play/pause, reset camera, and the ability to exit the simulation. Completing the first two took little time, issues with the exit button too were eventually resolved by simply refreshing the page on click and allowing grabage collection to destroy cannonjs/threejs objects. I also added other features such as maintaining canvas size on window resize and orbit controls to navigate. Next, I began work on building a dialog box with functionality to update Nybble's upper and lower arm lengths, torso dimensions, and max limb angles. 

![Dialog Box for input parameters](/assets/2019-05-09-web-simulator-final-report/ui.jpg)

Having coompleted this, currently the user is first presented with the dialog box wherein the user selects input values to render the simulation. For example, selecting the input as 

```
Upper Limb Height: 0.5
Lower Limb Height: 0.5
Torso Length: 2.0
Torso Width: 1.5
Torso Height: 0.6
```

renders the following simulation for Nybble:

![Example with different parameters](/assets/2019-05-09-web-simulator-final-report/example.jpg)
