---
layout: post
title:  "a Transformable Wheel-Leg Hybrid for Adabot"
categories: ["Missouri State University"]
tags: ["uhc396"]
author: "Eric McCullough"
---
#a Transformable Wheel-Leg Hybrid for Adabot
####Introduction
Transformable robots are robots that can adapt their physical bodies to better suit their environments.  Adabot is a 
small-scale autonomous robotic rover intended for search and rescue and exploration. This semester, I worked on a 
transformable wheel-leg hybrid to allow Adabot to more effectively adapt to its environment and overcome obstacles. 

Wheel-leg hybrids are often used in transformable robots. The core idea is to have a wheel that can deploy spoke-like 
legs that extend their radius while reducing their points of connection to the ground. This grants the robot utilizing
the wheel-leg hybrid the best of both worlds: the speed and efficiency of a traditional wheel and the ability to 
overcome rough terrain of legs. The rational for wheel-leg hybrids is fairly simple. The traditional wheel has been a 
 cornerstone of human vehicles since the beginning of technology for a reason. They are easy to make, provide 
excellent speed and mobility, and are so energy efficient that their basic design has not had to be updated for 
centuries. Legged movement apparatuses are more prone to failure and require far more energy per unit of travel than 
their simpler counterparts, but they do offer one clear advantage in overcoming obstacles. The larger radii and 
smaller points of contact with the ground that make them easier to break and require more energy do allow them to 
climb over obstacles that would be impassible for a simple wheel. Robots that are subjected to irregular terrain are 
prime candidates for transformable wheels. For search and rescue robots like Adabot, the ability to quickly and 
reliably overcome difficult terrain is a must. 
####Design Requirements
Adabot’s transformable wheel was designed with two key guiding principles in mind. First, the design had to be simple. 
Simplicity ensures that the wheel is easy to fabricate and assemble. This saves time for researchers working with 
Adabot and ensures that replacement parts are always readily available. A simpler design also means that there are 
fewer points of failure for the mechanism. While far more elegant transformable wheels have been created, every 
additional step in the transformation process provides an additional point where something could go wrong. In contrast,
a simple design means that issues are easily identified and addressed. 

The second design principle was also driven by the need to ensure the reliability of the transformation mechanism. The
design needed to reduce friction where possible. Previous implementations of a wheel-leg hybrid for Adabot had failed 
because the friction involved in the transformation process was too much for its parts, causing them to break. 
Reducing friction also offers the added benefit of making the transformation process more efficient and less taxing 
on Adabot’s motor. 
####Design
The resulting transformable wheel design consists of only three primary parts: an outer rim, an inner rim, and the 
legs. The inner rim is a disk 35 mm in radius and 2 mm thick. It operates as the wheel, when Adabot is in wheel mode.
On the outside of the inner rim are four brackets, upon which the legs can be hinged. These brackets extend outward 
from the rim 5 mm, providing the legs room necessary to carry out their motion for the transformation.

The outer rim is essentially a smaller version of the inner rim. It measures 15 mm across. In order to transform, a 
motor on adabot can pull the outer rim in towards the inner rim, extending the legs out as it comes in.

The legs are 30 mm long and 3 mm thick. They have two mounting areas: a 1 mm hole for attaching to the inner rim, and 
a 1 mm thick slit running up the length of the leg. The slit is mounted to a bracket on the outer rim, allowing the 
leg to both rotate and slide, extending into legged mode when the outer rim is retracted. 

####Design Images
![Wheel leg hybrid 1](assets/2018-12-10-a-transformable-wheel-leg-hybrid-for-adabot/Capture1.PNG)
![Wheel leg hybrid 1](assets/2018-12-10-a-transformable-wheel-leg-hybrid-for-adabot/Capture2.PNG)