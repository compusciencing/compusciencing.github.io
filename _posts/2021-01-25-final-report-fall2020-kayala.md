---
layout: post
title: Final Report - Fall 2020 Semester
tags: ["kevin", "independent study", "unreal engine", "arcslab"]
author: "Kevin Ayala"
include_mathjax: false
---


# Activities/Accomplishments and Concepts/Lessons Learned #
Concepts:

- Working with Unreal Engine

    - LOD and Materials
    - Movement and Cameras
    - Blueprints

- Creating Levels

    - Perlin noise generated maps
    - Transfer to Unreal Engine 4.25

Activities:

- I started the semester learning about Unreal Engine. I spent time making new materials and 
- objects, learning about Level Of Detail(LOD) mechanics and best practices for making hyper realistic environments. Part of that was learning about how to efficiently show realistic environments, and that hinged around only loading what is necessary.


![Example of LOD 1](../assets\2021-01-25-final-report-fall2020-kayala\lod1Rock.png)
*Figure 1: Example of close-up shot with Level of Detail 1*

![Example of LOD 5](../assets\2021-01-25-final-report-fall2020-kayala/lod5rock.png)
*Figure 2: Example of far-away shot with Level of Detail 5*


In the picture above, see the difference between a LOD of 1, which renders when the camera is close to the object, versus a LOD 5 object, which is used when the camera is further. 

Then I moved on to dynamic actors, including humanoid and rover forms. Moving the cameras and having them positioned and scripted correcly for 1st person views that were necessary to training the model was especially difficult. Here's what it looked like on the car model:

![Aerial view of car camera](../assets\2021-01-25-final-report-fall2020-kayala/vehicle-cam.png)

*Figure 3: Aerial view of camera placement on first car model*


Finally, I moved onto working with Blueprints, since a large part of the work involved taking and organizing screenshots at appropriate points in the movement of the vehicle. I struggled with this because UE is a very large program with not-so-adequate documentation for some tasks, but I was eventually able to learn how to take these screenshots and later organize them with a script into a CSV file. 

The Blueprint ended up looking like this:

![Final blueprint for screenshots](../assets\2021-01-25-final-report-fall2020-kayala/full-logging.png)
*Figure 4: Final blueprint*

I used Rama's extension to add more nodes to the blueprint environment. These were absolutely essential, as Unreal doesn't support reading or writing to text files otherwise. 

Afterwards, I wrote a python script to organize the screenshots into a csv, labeled with the direction the rover was going at the time it was taken. 

![Python script for organizing images](../assets\2021-01-25-final-report-fall2020-kayala/py-script.png)
*Figure 5: Final Python Script*

# Issues/Problems

- One of the recurring bugs I experienced was not enough space in my C drive, which Unreal Engine insisted on being installed in, even after I moved it to the larger F drive. Supporting files got installed there even if I pointed the installation wizard towards F:. It wasn't a huge deal, just a source of annoyance
- The largest setback was simply unfamiliarity with Unreal Engine, but I got over that ok. There are plenty of good youtube videos that you can watch to learn more. 
- Lastly, finding the library to read/write files was a huge breakthrough, but did take a lot of digging to find. 

# Plans for next semester

- The next essential step is being able to read a text file and generate a new world from it. For this, C++ is essential, so I'll be taking a crash course to learn the basics. 
