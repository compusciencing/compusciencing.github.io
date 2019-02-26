---
layout: post
title: "Web Simulator for Nybble"
categories: ["Missouri State University"]
tags: ["csc596", "JavaScript"]
author: "Saket Roy"
---

With Dr. Anthony Clark, I am working on building a web simulator for the [Nybble](https://www.indiegogo.com/projects/nybble-world-s-cutest-open-source-robotic-kitten#/), an open-source robotic kitten. I am writing the simulator in [TypeScript](https://www.typescriptlang.org), using the [HyperApp](https://github.com/jorgebucaran/hyperapp) Framework and [Parcel](https://parceljs.org). I will use the [three.js](https://threejs.org) 3D library and the [cannon.js](http://www.cannonjs.org)
 physics engine to render the simulation. All the development is front-end with no server-side scripting, and the website will be hosted on github.io

The simulator will have numerous features, including: input and update functionality for parameters such as robot arm length, configurable obstacles in the Nybble’s path, and buttons to start/stop simulation. I will achieve this using URL query parameters. The aim is to simulate the movements of the Nybble robot with variable body dimensions, and also its ability to maintain its path even if there are numerous obstacles.

As previously established with Dr. Clark, we intend to meet every Tuesday at 11:30 AM. In the meeting, we discuss about progress over the week, issues faced, any possible queries, and expectations for the next week.
