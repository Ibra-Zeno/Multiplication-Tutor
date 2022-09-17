# Multiplication-Tutor
A program which helps the user to practise their multiplication tables. The user is able to specify how many equations they would like to solve and the range of numbers used in the problems. The program gives feedback on the answers and the time taken to answer.

---

###Technologies
Python 3.10-64
Random module

## Project Status
Complete with room for improvement.

## Example of project function

The program, when run, will initially ask the range at which the user is comfortable with multiplication e.g. 12. This is followed up with the question of how many problems the user would like to solve. The program will output multiplication questions such as

>12*11

The program will give feedback after every question, discerning whether the solution was correct or not. Once all problems are solved, information about the performance is given i.e. all the questions asked, with their correct solutions, alongside the user answers. Information regarding the time taken to answer each question is then returned. Below is an example:

>Question 1: 10 * 8 = 80.
  >You answered: 80.
 >It took you 1.9 seconds to answer this question


## Room for improvement
- The program fails if a non-integer is input. An improvement can be made to accept non-integer answers and return a message asking for integers only.
- Duplicate questions can be avoided if random.sample() is used.

## Sources 
[Python 3.10.7 documentation](https://docs.python.org/3/)

## Other information
Contact me on Github under the username *Ibra-Zeno*
