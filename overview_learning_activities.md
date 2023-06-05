# (Embarrassingly) Parallel Python - Overview and Learning Activities

Jakob, Zbigniew, Jenni

## Learning activities

In the course of the lecture, a student will:  
 * Understand the difference between a thread and a process, and why using multithreading with Python is often not beneficial [Jenni]
    * Example exercise: We explain the basics of the GIL, then ask the students to hypothesize in pairs why (a) multithreading in python doesn’t really work and (b) why numpy magically works [10 mins, including discussion]
 * Identify which sorts of computational problems are better solved with multithreading vs. multiprocessing [Jenni]
    * Example exercise: We list different sorts of problems, they need to figure out whether it is better suited to multithreading or multiprocessing (or neither) [10 mins, including discussion]
 * Analyse the effect of threading on numpy execution and, from that, hypothesize the architecture of the laptop [Zbyszek]
    * Example plotting speed versus threads [30 mins, including discussion]
 * Apply the multiprocessing module to an embarrassingly parallel problem and analyse the resulting speed-up [Jakob]
    * Exercise: Take our code and improve it, please :) [30 mins, including discussion]
 * Examine the interaction between multiprocessing and numpy’s multithreading [Zbyszek]
    * Exercise: using multiprocessing, start 4 jobs with numpy and then see how many threads you spin up and how your speed-up DIES [20 mins, including discussion]
 * Hear about simple techniques for larger-than-memory problems [Jenni]  
 * Hear about related packages for parallel computing [Jakob]
