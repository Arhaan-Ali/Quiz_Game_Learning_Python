Quiz_y_N = input("would like to play a quiz!? : ")
if Quiz_y_N.upper() == "YES" :
    Choice = input(("Would you like to take a quiz on Science, History, Mathematics or Literature "
          "\n Choose S for Science "
          "\n Choose H for History"
          "\n Choose M for Mathematics"
          "\n Choose L for Literature"
                    "\n"))
    if Choice.upper() == "S" :
        questions = ("What is the powerhouse of the cell?",
                     "What planet is known as the Red Planet?",
                     "What gas do plants absorb from the atmosphere?",
                     "What is the chemical symbol for water?",
                     "Which of these elements is a noble gas?")
        options = (("A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"),
                   ("A. Earth", "B. Venus ", "C. Mars", "D. Jupiter"),
                   ("A. Oxygen", "B.Carbon dioxide ", "C. Nitrogen", "D. Hydrogen"),
                   ("A. O2", "B. H2O", "C. CO2", "D. NaCl"),
                   ("A. Nitrogen", "B. Oxygen", "C. Helium", "D. Hydrogen"))
        answers = ("B", "C", "B", "B", "C")
        Guesses = []
        score = 0
        Question_num = 0
        for question in questions :
            print("-------------------------")
            print(question)
            for option in options[Question_num] :
                print(option)
            guess = input("Enter (A, B, C, D): ").upper()
            Guesses.append(guess)
            if guess == answers[Question_num] :
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[Question_num]} is the correct option ")
            Question_num += 1
        print("-------------------------")
        print("          RESULTS        ")
        print("-------------------------")

        print("answers: ", end="")
        for answer in answers :
            print(answer, end="")
        print()

        score = int(score / len(questions) * 100)
        print(f"your score is {score}%")
    elif Choice.upper() == "H":
        questions = ("Who was the first person to set foot on the Moon?",
                    "In which year did World War II end?",
                    "Who was the last emperor of Russia?",
                    "What empire was ruled by Genghis Khan?",
                    " Who was the British Prime Minister during most of World War II?")
        options = (("A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. John Glenn"),
                   ("A. 1943", "B. 1945", "C. 1947", "D. 1950"),
                   ("A. Peter the Great", "B. Alexander II", "C. Nicholas II", "D. Ivan the Terrible"),
                   ("A. Roman Empire", "B. Ottoman Empire", "C. Mongol Empire", "D. Persian Empire"),
                   ("A. Neville Chamberlain", "B. Winston Churchill", "C. Margaret Thatcher", "D. Tony Blair"))
        answers = ("A", "B", "C", "C", "B")
        Guesses = []
        score = 0
        Question_num = 0
        for question in questions:
            print("-------------------------")
            print(question)
            for option in options[Question_num]:
                print(option)
            guess = input("Enter (A, B, C, D): ").upper()
            Guesses.append(guess)
            if guess == answers[Question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[Question_num]} is the correct option ")
            Question_num += 1
        print("-------------------------")
        print("          RESULTS        ")
        print("-------------------------")

        print("answers: ", end="")
        for answer in answers:
            print(answer, end="")
        print()
        score = int(score / len(questions) * 100)
        print(f"your score is {score}%")
    elif Choice.upper() == "M" :
        questions = ("What is the square root of 144?",
                    "If a triangle has sides of 3, 4, and 5 units, what type of triangle is it?",
                    "What is 15% of 200?",
                    "What is the next prime number after 7?",
                    "What is the value of 9 squared?")
        options = (("A. 10", "B. 12", "C. 14", "D. 16"),
                   ("A. Scalene", "B. Isosceles", "C. Equilateral", "D. Right-angled"),
                   ("A. 20", "B. 25", "C. 30", "D. 35"),
                   ("A. 9", "B. 10", "C. 11", "D. 12"),
                   ("A. 18", "B. 27", "C. 72", "D. 81"))
        answers = ("B", "D", "C", "C", "D")
        Guesses = []
        score = 0
        Question_num = 0
        for question in questions:
            print("-------------------------")
            print(question)
            for option in options[Question_num]:
                print(option)
            guess = input("Enter (A, B, C, D): ").upper()
            Guesses.append(guess)
            if guess == answers[Question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[Question_num]} is the correct option ")
            Question_num += 1
        print("-------------------------")
        print("          RESULTS        ")
        print("-------------------------")

        print("answers: ", end="")
        for answer in answers:
            print(answer, end="")
        print()
        score = int(score / len(questions) * 100)
        print(f"your score is {score}%")
    elif Choice.upper() == "L" :
        questions = ("Who wrote Moby Dick?",
                     "Which novel features the character Jay Gatsby?",
                     "Who wrote The Catcher in the Rye?",
                     "In which novel would you find the character Sherlock Holmes?",
                     "Who is the author of Pride and Prejudice?")
        options = (("A. Herman Melville", "B. Mark Twain", "C. Nathaniel Hawthorne", "D. Charles Dickens"),
                   ("A. 1984", "B. The Great Gatsby", "C. Pride and Prejudice", "D. To Kill a Mockingbird"),
                   ("A. J.D. Salinger", "B. F. Scott Fitzgerald", "C. Ernest Hemingway", "D. John Steinbeck"),
                   ("A. Dracula", "B. The Hound of the Baskervilles", "C. The Picture of Dorian Gray", "D. The Time Machine"),
                   ("A. Emily Brontë", "B. George Eliot", "C. Jane Austen", "D. Charlotte Brontë"))
        answers = ("A", "B", "C", "C", "B")
        Guesses = []
        score = 0
        Question_num = 0
        for question in questions:
            print("-------------------------")
            print(question)
            for option in options[Question_num]:
                print(option)
            guess = input("Enter (A, B, C, D): ").upper()
            Guesses.append(guess)
            if guess == answers[Question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[Question_num]} is the correct option ")
            Question_num += 1
        print("-------------------------")
        print("          RESULTS        ")
        print("-------------------------")

        print("answers: ", end="")
        for answer in answers:
            print(answer, end="")
        print()
        score = int(score / len(questions) * 100)
        print(f"your score is {score}%")
    else :
        print(f"{Choice} is not valid please choose from the options above ")
elif Quiz_y_N.upper() =="NO" :
    print("Okay! comeback later!")
else:
    print("PLEASE WRITE EITHER YES OR NO")
