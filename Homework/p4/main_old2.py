# -*- coding: utf-8 -*-
def askQuestion(Correct_an, question_hint = "Check the textbook"):
    count = 0
    n = int(input("How many tries do you want for each question: "))
    try1 = n
    print("\nWhat is the type of the following? '1.0' + '2.0'\n a) int \n b) float \n c) str \n d) bool \n e) NoneType")
    while try1 > 0:
        answer1 = str.lower(str.strip(input("Your Answer: ")))
        if answer1 == Correct_an[0]:
            print("\nCongratulations! You got it right.")
            count += 1
            break      
        elif try1 == 2:
            print(question_hint)
            print("Try again! You have %d more tries.\n" %(try1-1))
            try1 = try1 -1
        else:
            print("Try again! You have %d more tries.\n" %(try1-1))
            try1 = try1 -1             
    try2 = n    
    print("\nWhat is the type of the following? '1' * 2")
    while try2 > 0:            
        answer2 = str.lower(str.strip(input("Your Answer: ")))  
        if answer2 == Correct_an[1]:
            print("\nCongratulations! You got it right.")
            count += 1
            break
        elif try2 == 2:
            print(question_hint)
            print("Try again! You have %d more tries.\n" %(try2-1))
            try2 = try2 -1   
        else:
            print("Try again! You have %d more tries.\n" %(try2-1))
            try2 = try2 -1   
    try3 = n        
    print("\nWhat does this expression evaluate to?\n True != (3 < 2)")
    while try3 > 0:
        answer3 = str.lower(str.strip(input("Your Answer: ")))
        if answer3 == Correct_an[2]:
            print("\nCongratulations! You got it right.")
            count += 1
            break
        elif try3 == 2:
            print(question_hint)
            print("Try again! You have %d more tries.\n" %(try3-1))
            try3 = try3 -1
        else :
            print("Try again! You have %d more tries.\n" %(try3-1))
            try3 = try3 -1
    print("You tried 3 questions and got %d right." % count)
    







