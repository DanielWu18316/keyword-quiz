import random


def setup():
    global info, keywords, desc
    f = open("keywords.txt")
    info = f.readlines()
    f.close()
    keywords = []
    desc = []
    for i in range(0, len(info), 2):
        keywords.append(info[i])
    for i in range(1, len(info), 2):
        desc.append(info[i])
    process()


def process():
    user_choice = 0
    user_choice = input(
        "Choose an option:\n1. Show Keywords + Description\n2. Play Quiz\n> ")
    if user_choice == "1":
        print("Selected: Show Keywords + Description")
        for i in range(0, len(info) // 2):
            print("\n-",keywords[i][:-1] + ":")
            print(desc[i][:-1])
        user_choice = input(
            "\nWould you like to play the quiz now? [Y] or [N]\n> ")
        if user_choice == "Y":
            quiz()
        elif user_choice == "N":
            print("Okay")
    elif user_choice == "2":
        quiz()


def quiz():
    question_number = 1
    points = 0
    user_answer = ""
    print("\nEnter '-1' to stop quiz")
    while user_answer != "-1":
        question = random.choice(desc)
        print("\n- Question", question_number, "-\n" + question)
        user_answer = input("- Answer:\n> ")
        if user_answer.lower() == str(keywords[(desc.index(question))][:-1]):
            points = points + 1
            print("Correct! +1\nPoints:", points)
        elif user_answer == "-1":
            print("\nEnding Quiz...")
            break
        else:
            print("Incorrect.\nThe answer was",
                  keywords[(desc.index(question))][:-1])
        question_number = question_number + 1
    print("You got", points, "/", question_number - 1, "questions correct")
    if points == 0:
        print("You did not attempt the quiz\n")
    elif points > question_number // 2:
        print("You passed!\n")
    else:
        print("You did not pass.\n")
    setup()


setup()
