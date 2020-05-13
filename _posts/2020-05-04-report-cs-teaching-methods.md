---
layout: post
title: "Report: A CS Teaching Methods Experiment"
tags: ["csc696", "teaching", "pedagogy", "experiment preparation", "msu"]
author: "Nathan Hartzler"
---

*During the Spring 2020 semester, I worked to develop an experiment to research Pedagogy in Computer Science*.

# Working Hypothesis

When teaching a computer science concept, is student understanding increased if an analogous hands-on activity is performed in addition to the traditional lecture of the concept?

# Experiment Framework

- Working with a computer science instructor, design as many activities as feasible in line with a course syllabus. The preference is for a computer science course with multiple lab sections to have a control group for the experiment.

- Each activity should cover a specific course objective, such as **Understanding Sorting Algorithms** or **Understanding Error Detection**.

- One section should receive a traditional lecture and programming exercise for a topic. The other section(s) should perform an activity in addition to the lecture and programming exercise.

- Non-credit, anonymized surveys should be given throughout the semester to evaluate how the activity (or lack thereof) affected student understanding of a topic.

# Sample Activity - Error Detection

To familiarize students with the concept of flipped bit error detection and parity bits, I investigated a simple activity found on [csunplugged.org](https://csunplugged.org/en/topics/error-detection-and-correction/unit-plan/parity-magic/).

1. In a classroom or small group setting, I have a volunteer student lay out a 5 x 5 grid of black and white square tiles. These are white on one side and black on the other. I ask the student to choose tile colors at random.

    ![Example 5 by 5 grid](/assets/2020-05-04-report-cs-teaching-methods/parity-cards-6x6-grid-step-1.png)

    - Example layout of a 5 x 5 grid set up by the volunteer [1]. [csunplugged.org](https://csunplugged.org/en/topics/error-detection-and-correction/unit-plan/parity-magic/)

2. Then I add an additional row and column with "parity bits". The result should be a 6 x 6 with an even number of black tiles in each row and column.

    <video controls autoplay="true">
        <source src="/assets/2020-05-04-report-cs-teaching-methods/parity-cards.mp4"
                type="video/mp4">
        Sorry, your browser doesn't support embedded videos.
    </video>

    - Adding a parity bit to each row and column [2]. [csunplugged.org](https://csunplugged.org/en/topics/error-detection-and-correction/unit-plan/parity-magic/)

3. I then turn my back to the grid and the student flips one of the squares over, changing its color.

4. Next I look at the board and silently scan the black tiles in each row. Once an odd number of black tiles is found in a row, the columns can be scanned. When the corresponding column is found the (x,y) point of the flipped tile is known.

Students then break into groups of 2 to 3, each group with its own set tile cards, and take turns flipping or finding the "erroneous" bits.

# Challenges

Due to the onset of the COVID-19 pandemic, hands-on group activties in a classroom are put in a different light. There is now a need to switch to online versions of the activies in order to perform the experiment in the fall.

- **Problem:** How to develop online activies that aren't just coding exercises?
    - One aspect of this research is to study non-coding activies. I want to test if teaching practical analogies of abstract digital concepts is worth doing.
    
    - Custom online activies can be produced but this may take lots of development time.
    
    - Fortunately, there is an interactive version of the sample [Card Flip Error Detection](https://csfieldguide.org.nz/en/interactives/parity/) activity.

- **Problem:** How to engage students in the activity when the course is delivered asynchronously online?
    - Part of the engament in the activities was planned to come from group dynamics. 
    - 2 large groups of classmates racing against each other in a sorting activity
    - Or many small groups performing the error detection activity
    - Without 1 on 1 engagement between the instructor and students, the connections may not be made between the analogous activity and the algorithm or concept being taught.

I do not have answers to these problems but will continue to study and work to figure out some workarounds or solutions.

# Accomplishments

Dr. Jamil Saquer has agreed to work with me on this research for Missouri State's CSC 131 course lab sections. This may not be possible in Fall 2020 since there is only 1 lab section offered and the COVID-19 requirements may move this section online.

An application for this research is in progress for an application for review to Missouri State University's [Institutional Review Board](https://ora.missouristate.edu/IRB.htm).

As part of this investigation, I read multiple papers including Dr. Saquer's pedegologcal approaches to simplify Dynamic Programming [3] and a study of engagement in the computer science classroom [4].

# Future Work

I will discuss online activies with Dr. Saquer and potentially develop them for the Spring 2021 semester.

As studied by John Aycock in [5], I would like to use my ❤️ for computer science history by working to develop a course that uses the challenges and constraints of past computer scientists/developers/etc. to teach modern students valuable skills for the future.  

# References

[1] Anon. Example layout of a 5 x 5 grid set up by the volunteer, Computer Science Education Research Group, University of Canterbury. https://csunplugged.org/en/topics/error-detection-and-correction/unit-plan/parity-magic/

[2] Anon. Adding a parity bit to each row and column., Computer Science Education Research Group, University of Canterbury. https://csunplugged.org/en/topics/error-detection-and-correction/unit-plan/parity-magic/

[3] Jamil Saquer. 2016. An Approach To Making Dynamic Programming Easier For Students In The Computer Science Curriculum. The International Journal of E-Learning and Educational Technologies in the Digital Media 2, 4 (2016), 157–165. DOI:http://dx.doi.org/10.17781/p002223

[4] Johanna Pirker, Maria Riffnaller-Schiefer, and Christian Gütl. 2014. Motivational active learning. Proceedings of the 2014 conference on Innovation & technology in computer science education - ITiCSE 14 (2014). DOI:http://dx.doi.org/10.1145/2591708.2591750

[5] John Aycock. 2015. Applied Computer History. Proceedings of the 2015 ACM Conference on Innovation and Technology in Computer Science Education - ITiCSE 15 (2015). DOI:http://dx.doi.org/10.1145/2729094.2742583
