# Career Quiz CLI Tool

## Description

The Career Quiz is a simple Python command-line program that asks the user 8 multiple-choice questions about their interests and preferences.

Each answer is connected to a career category. The program gives one point to the selected category for every question. At the end, the category with the highest score is used to recommend a career path.

## Career Categories

The quiz has five career categories:

- Tech
- Creative
- Business
- Healthcare
- Social Impact

## Requirements

- Python 3
- No extra libraries are needed.

## How to Run

1. Open a terminal in the project folder.
2. Run the following command:

```bash
python career_quiz.py
```

3. Answer each question by entering the letter of your choice.

## Example Run

```text
==================================================
              CAREER QUIZ
==================================================
Answer the questions to find a career area that
matches your interests.

1. What would you rather do in your free time?
   a) Work on a computer or build something
   b) Draw, write, or make something creative
   c) Plan an event or business idea
   d) Learn about health or help someone
   e) Help with a community activity

Your answer: a

2. Which subject do you like most?
   a) ICT or Computer Science
   b) English or Art
   c) Economics or Business
   d) Biology or Health Science
   e) Government or Social Studies

Your answer: a

...

==================================================
                  RESULTS
==================================================
Tech: 5
Creative: 1
Business: 1
Healthcare: 1
Social Impact: 0

Recommended career path:
Technology or Software Development
```

## How the Scoring Works

Every time the user selects an answer, the program adds 1 point to the career category connected to that answer.

For example:

- Choosing a Tech answer → Tech gets 1 point
- Choosing a Business answer → Business gets 1 point
- Choosing a Creative answer → Creative gets 1 point

After all 8 questions have been answered, the program checks which category has the highest score and recommends that career path.

## Files

- `career_quiz.py` - The main Python program
- `README.md` - Information about the project and an example run
```
