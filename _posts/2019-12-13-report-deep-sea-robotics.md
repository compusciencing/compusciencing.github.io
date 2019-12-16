---
layout: post
title: "Report: Deep Sea Robotics"
tags: ["csc197", "deep sea", "simulation", "robotics", "report", "self-study"]
author: "Fiona Wu"
---

I define my research as the development of underwater environments and models using Gazebo Simulator. Specifically, the aim of my research was to create a robot model that could withstand deep sea pressures. However, as the semester went by and technical difficulties arose, my research devolved into more of an exploration of the [UUV simulator](https://uuvsimulator.github.io/) while learning how to use new software and operating systems such as [Gazebo Simulator](http://gazebosim.org/), [Github](https://github.com/), [Blender](https://www.blender.org/), and Linux. Although I did not get as far as I had hoped on my research, I developed an initial prototype to the model and altered the existing [UUV simulator environment](https://uuvsimulator.github.io/). 


# Setting Up

With no previous experience using Gazebo and Linux, I devoted a lot of my time in the first few weeks to downloading and differentiating between Linux distributions. After experimenting with [Ubuntu](https://ubuntu.com/) and [Linux Mint](https://linuxmint.com/), both of which are Linux distros, I opted to use Ubuntu which proved much easier to download and run Gazebo. 

# Environment Changes/understanding UUV Simulator

After downloading Gazebo, my first step was to create or find a suitable underwater environment. Unlike most other environments, Gazebo does not have a very in-depth default underwater environment, so I used the UUV simulator. The UUV simulator is a "set of packages with Gazebo plugins and ROS modules to enable simulation of underwater vehicles" [(Manhães 2018)](https://roscon.ros.org/2018/presentations/ROSCon2018_uuvsimulator.pdf) . After installing the simulator and the proper ROS distributions, I played around with the provided environments; I settled with using the empty_underwater_world as the base. 

I tested the buoyancy of the simulator by making sure objects sunk when denser.

![bouyancysinking](/assets/2019-12-13-report-deep-sea-robotics/buoyancysinking.png)
 *sinking cube* 

Going into the research, I knew I wanted to make my focus more about the deep sea. Because of this, I would have to alter the default depth of the simulator. To do this, I expanded the pose and collision of each of the "walls" of the sea.

![pose](/assets/2019-12-13-report-deep-sea-robotics/pose.png)
 *"walls" of the sea* 

![pose2newvsoriginal](/assets/2019-12-13-report-deep-sea-robotics/pose2newvsoriginal.png)
 *altered pose numbers vs. original* 

# Building Initial Model

To create my initial mode, I used Blender. Never having used Blender before, it took me a while to get comfortable with the controls and build 3-D shapes. While deciding what shape to use, I learned a lot about different shapes that comprise manmade underwater vehicles such as submarines, cameras, and more. Some interesting things that I came upon included the pressure. 

![blenderpartofmodel](/assets/2019-12-13-report-deep-sea-robotics/blenderpartofmodel.png)
 *part of the model in Blender* 

![sinkingvehicle](/assets/2019-12-13-report-deep-sea-robotics/sinkingvehiclegif.gif)
 *final model sinking* 

# Going Forward

Going forward in this project, several of the issues I want to work on are the robot dealing with and interpreting pressure. It does not seem as if the original simulator has pressure built into it. I also want to work on making the robot more independent. 
