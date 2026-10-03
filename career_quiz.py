"""
Career Quiz

This program asks the user some questions about their interests
and gives them a career recommendation based on their answers.
"""

import sys


questions = [
    {
        "question": "1. What would you rather do in your free time?",
        "options": {
            "a": ("Work on a computer or build something", "Tech"),
            "b": ("Draw, write, or make something creative", "Creative"),
            "c": ("Plan an event or business idea", "Business"),
            "d": ("Learn about health or help someone", "Healthcare"),
            "e": ("Help with a community activity", "Social Impact")
        }
    },
    {
        "question": "2. Which subject do you like most?",
        "options": {
            "a": ("ICT or Computer Science", "Tech"),
            "b": ("English or Art", "Creative"),
            "c": ("Economics or Business", "Business"),
            "d": ("Biology or Health Science", "Healthcare"),
            "e": ("Government or Social Studies", "Social Impact")
        }
    },
    {
        "question": "3. Which word describes you best?",
        "options": {
            "a": ("Logical", "Tech"),
            "b": ("Creative", "Creative"),
            "c": ("Persuasive", "Business"),
            "d": ("Caring", "Healthcare"),
            "e": ("Helpful", "Social Impact")
        }
    },
    {
        "question": "4. What kind of work would you enjoy?",
        "options": {
            "a": ("Solving problems with technology", "Tech"),
            "b": ("Creating new things and sharing ideas", "Creative"),
            "c": ("Managing people or making decisions", "Business"),
            "d": ("Taking care of people's health", "Healthcare"),
            "e": ("Helping people with their problems", "Social Impact")
        }
    },
    {
        "question": "5. Which achievement would make you happiest?",
        "options": {
            "a": ("Creating an app that people use", "Tech"),
            "b": ("Making a video, design, or piece of writing", "Creative"),
            "c": ("Starting a successful business", "Business"),
            "d": ("Helping someone get better", "Healthcare"),
            "e": ("Helping improve your community", "Social Impact")
        }
    },
    {
        "question": "6. What would a friend most likely ask you for help with?",
        "options": {
            "a": ("A computer or phone problem", "Tech"),
            "b": ("An idea, design, or creative project", "Creative"),
            "c": ("Money or business advice", "Business"),
            "d": ("A health-related problem", "Healthcare"),
            "e": ("A personal or social problem", "Social Impact")
        }
    },
    {
        "question": "7. Which group project would you choose?",
        "options": {
            "a": ("Building a website or app", "Tech"),
            "b": ("Making a video or poster", "Creative"),
            "c": ("Presenting a business idea", "Business"),
            "d": ("Researching a health problem", "Healthcare"),
            "e": ("Organising a community project", "Social Impact")
        }
    },
    {
        "question": "8. What is most important to you in a future job?",
        "options": {
            "a": ("Solving interesting problems", "Tech"),
            "b": ("Having freedom to be creative", "Creative"),
            "c": ("Making money and becoming a leader", "Business"),
            "d": ("Helping people stay healthy", "Healthcare"),
            "e": ("Making a difference in people's lives", "Social Impact")
        }
    }
]


career_descriptions = {
    "Tech": "Technology or Software Development",
    "Creative": "Creative Design, Writing, or Media",
    "Business": "Business, Marketing, or Entrepreneurship",
    "Healthcare": "Healthcare or Life Sciences",
    "Social Impact": "Education, Community, or Nonprofit Work"
}


def ask_question(question):
    print(question["question"])

    for letter, option in question["options"].items():
        print(f"   {letter}) {option[0]}")

    while True:
        answer = input("Your answer: ").strip().lower()

        if answer in question["options"]:
            return question["options"][answer][1]

        print("Please choose a valid option (a, b, c, d, or e).")


def run_quiz():
    scores = {
        "Tech": 0,
        "Creative": 0,
        "Business": 0,
        "Healthcare": 0,
        "Social Impact": 0
    }

    print("=" * 50)
    print("              CAREER QUIZ")
    print("=" * 50)
    print("Answer the questions to find a career area that")
    print("matches your interests.")
    print()

    for question in questions:
        category = ask_question(question)
        scores[category] += 1
        print()

    recommended = max(scores, key=scores.get)

    print("=" * 50)
    print("                  RESULTS")
    print("=" * 50)

    for category, score in scores.items():
        print(f"{category}: {score}")

    print()
    print("Recommended career path:")
    print(career_descriptions[recommended])


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz cancelled.")
        sys.exit()
