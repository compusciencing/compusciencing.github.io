---
layout: post
title: "Making Computer Science: CS Education"
tags: ["csci181AL.1FA23", "arduino", "circuitpython", "3d printing", "hmc"]
author: "Anthony J. Clark"
---

This serves as my journal entry for the first module of the Making Computer Science course (CS 181AL at HMC).

## Pre-Unit Prompt

What previous experience do you have with the topics in this unit?

> I have experience with programming, CAD, and electronics. But I have never used e-textiles, and I have never directly used a 3D printer. I have a lot of experience asking students to 3D print things, and I am excited to do it myself.

What do you want to learn during this unit?

> I want to learn how to use the [HMC Maker Space](https://make.hmc.edu/) and better complete projects with physical components. I have a lot of designs and project ideas, but they do not come to fruition without a student doing to work. I also want to involve my 7 year old daughter so she can see me struggle and then overcome (as well as experience the maker space—I’ll ask Kim about rules for bringing my daughter along).

What will your learning look like in this unit?

> Enthusiasm, joy, and frustration. I am very excited for this course, and the drive that it will give me to work on projects that have been on my backlog for a long time. Many projects end up on my backlog because I am not confident enough to get into the maker space.

How will you demonstrate your learning?

> I am going to journal using my blog. I will document my process, failings, and epiphanies. Journal entries might include videos.

## Final Project Ideas

I have the following projects in mind. I am not sure while I will complete for the final project in this course.

- Roll-up/sandwich case for my folding bicycle.
- A e-textile for my daughter’s Halloween costume.
- A rotary inverted pendulum.
- Refurbishing an old globe.
- Creating an electronic sign for my office.
- An autonomous ground vehicle.
- Casting parts using resins.
- Casting parts using bronze.
- Embroidering a hat.
- Astronomical telescope.
- Magnetic wool electronics case.

## 3D-Printing

I started by completing all [HMC Maker Space quizzes](https://make.hmc.edu/?p=quiz-info). I recommend completing these even if you don't see yourself using that particular tool. It was a good way to come up with ideas for what is possible.

We modeled four toys, but I'll focus just on one here: a fake version of our dog Trapp.

<div style="display: flex;">
	<div style="flex: 22%; padding 2px;">
		<img width="100%" src="/assets/2023-09-20-makingcs-cseducation/Trapp1.webp" alt="Trapp1" />
	</div>
	<div style="flex: 22%; padding 2px;">
		<img width="100%" src="/assets/2023-09-20-makingcs-cseducation/Trapp2.webp" alt="Trapp2" />
	</div>
	<div style="flex: 22%; padding 2px;">
		<img width="100%" src="/assets/2023-09-20-makingcs-cseducation/Trapp3.webp" alt="Trapp3" />
	</div>
	<div style="flex: 22%; padding 2px;">
		<img width="100%" src="/assets/2023-09-20-makingcs-cseducation/Trapp4.webp" alt="Trapp4" />
	</div>
</div>

*Figure 1:* Trapp was a good dog.

Here is the stuffed version of Trapp.

<img width="50%" src="/assets/2023-09-20-makingcs-cseducation/ZeusReal.webp">

*Figure 2:* Zeus is a good stuffie.

We used [Polycam](https://poly.cam/) on an iPad to create a mesh of the stuffed animal from a series of photos.

<iframe src="https://poly.cam/capture/0EEDD2E6-C1E3-4767-9812-ECF0BA6BF5AE" title="polycam capture viewer" style="height:100%;width:100%;max-height:720px;max-width:1280px;min-height:280px;min-width:280px" frameborder="0"></iframe>

We exported the mesh as an STL and imported it into [Tinkercad](https://www.tinkercad.com/). In Tinkercad, we removed some visual artifacts and added a base.

<img width="50%" src="/assets/2023-09-20-makingcs-cseducation/ZeusTinkercad.png">

*Figure 3:* Zeus in Tinkercad.


My daughter and I decided to model and print a few of her toys.

- maker space quizzes
- 3d printing
	+ photographed four items
		* zeus, kuromi, pompompuri, black panther
	+ polycam created a mesh
	+ exported to STL
	+ imported into tinkercad
		* removed artifacts
		* added base (different for two prints)
	+ 3d printed
		* needed supports for tail and belly

## E-Textiles

![Adafruit Gemma M0](https://cdn-learn.adafruit.com/assets/assets/000/049/776/original/adafruit_gemma_Adafruit_Gemma_M0.png?1514755968)

*Figure TODO: Adafruit Gemma M0*

Documentation:

- [`adafruit_debounce`](https://docs.circuitpython.org/projects/debouncer/en/latest/api.html)
-

Not yet completed work:

- Adding a fading mode to the external LEDs using [pwmio](https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/index.html)

## Reflections

I read the articles and watched the video listed under resources. I did so before I realized there would be a reflection section of the journal entry. Luckily, I am auditing the course so I am giving myself a pass on having a write-up this time.

## Post-Unit Prompt

Look back at your pre-unit prompt. To what extent did you learn the things you said you wanted to during this unit?

Did you spend (at least) 6 hours a week on focused work for this class?

In what ways did your learning look like you expected? In what ways did things go differently?

Reflect on your experience sharing your work with others. How did it feel? Did you get ideas you hadn’t thought of before?

What new ideas, questions, or topics for learning do you have in mind at the end of this unit? Are there things you started here that might be the foundation for a final project?








# screen -S circuitpy /dev/tty.usbmodem2301
# ctrl-a d to detach
# ctrl-a k to kill
# screen -r circuitpy


>>> import storage
>>> storage.erase_filesystem()


mdutil -i off /Volumes/CIRCUITPY
cd /Volumes/CIRCUITPY
rm -rf .{,_.}{fseventsd,Spotlight-V*,Trashes}
mkdir .fseventsd
touch .fseventsd/no_log .metadata_never_index .Trashes
cd -

cp -rX folder_to_copy /Volumes/CIRCUITPY

duf

❯ dust /Volumes/CIRCUITPY/
❯ df /Volumes/CIRCUITPY/



❯ cp -X lib/adafruit_dotstar.mpy /Volumes/CIRCUITPY/lib/
ImportError: no module named 'adafruit_pixelbuf'
❯ cp -X lib/adafruit_pixelbuf.mpy /Volumes/CIRCUITPY/lib/

Gemma capabilities

- internal RGB led --> `DotStar`
	+ from rainbowio import colorwheel
- internal led board.LED --> `digitalio`
- touch input A0, A1, A2 --> `TouchIn`

python -m pip install circup
circup list
circup install --auto
circup freeze

❯ cp /Volumes/CIRCUITPY/code.py .

❯ df /Volumes/CIRCUITPY/
Filesystem   512-blocks Used Available Capacity iused ifree %iused  Mounted on
/dev/disk2s1         94   23        71    25%     512     0  100%   /Volumes/CIRCUITPY

❯ dust -c /Volumes/CIRCUITPY/
  0B     ┌── no_log                │                                                                           ░█ │   0%
512B   ┌─┴ .fseventsd              │                                                                           ██ │   2%
512B   ├── boot_out.txt            │                                                                           ██ │   2%
2.0K   ├── code.py                 │                                                                       ██████ │   7%
1.0K   │ ┌── adafruit_ticks.mpy    │                                                     ░░░░░░░░░░░░░░░░░░░░░███ │   4%
1.5K   │ ├── adafruit_dotstar.mpy  │                                                     ░░░░░░░░░░░░░░░░░░░█████ │   5%
2.5K   │ ├── adafruit_debouncer.mpy│                                                     ░░░░░░░░░░░░░░░░████████ │   9%
3.0K   │ ├── adafruit_pixelbuf.mpy │                                                     ░░░░░░░░░░░░░░░█████████ │  11%
8.5K   ├─┴ lib                     │                                                     ████████████████████████ │  31%
 27K ┌─┴ CIRCUITPY                 │█████████████████████████████████████████████████████████████████████████████ │ 100%

dotstar
- long press -> cycle through modes (off, glow, solid, touch, cycle)
- fell -> (glow:change-color, solid:change-color, touch:on)

leds
- long press -> cycle through modes (off, solid, touch)

long press changes mode:
- on-press
- on/off
- color cycle
- color picker
