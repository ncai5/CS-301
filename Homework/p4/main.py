
# coding: utf-8

# In[ ]:


# project: p4
# submitter-netid: hpan56
# partner-netid: ncai5


# In[ ]:


def askQuestion(Answer, Question = 1, question_hint = "check the textbook"):
    Question = 1
    count = 0
    n = int(input("How many tries do you want for each question: "))
    while Question < 4:
        if Question == 1:
            print("\nWhat is the type of the following? \"1.0\" + \"2.0\" \n a) int \n b) float \n c) str \n d) bool \n e) NoneType\n")
        elif Question == 2:
            print("\nWhat is the type of the following? \"1\" * 2")
        else:
            print("\nWhat does this expression evaluate to?\n True != (3 < 2)")
        tries = n
        answer = input("Your answer: ")
        answer_lower_strip = str.lower(str.strip(answer))                                       
        while tries > 0:
            if answer_lower_strip == Answer[Question-1]:
                print("\nCongratulations! You got it right.")
                count += 1
                break      
            elif tries == 2:
                if Question == 1:
                    question_hint = "check the textbook"
                elif Question == 2:
                    question_hint = "notice the quotes!"
                else :
                    question_hint = "Calcuate the right side first. Don't forget != means not equal to."
                print(question_hint)
                tries = tries -1
                print("You have this many remaining tries: %d" %tries)
                answer = input("Your answer: ")
                answer_lower_strip= str.lower(str.strip(answer)) 
            elif tries == 1:
                tries = tries -1 
                print("\nYou answered '%s'. The correct answer is '%s'." %(answer, Answer[Question-1])) 
                print("You have this many remaining tries: %d" %tries)
            else:
                tries = tries -1 
                print("\nYou answered '%s'. The correct answer is '%s'." %(answer, Answer[Question-1])) 
                print("You have this many remaining tries: %d" %tries)
                answer = input("Your answer: ")
                answer_lower_strip = str.lower(str.strip(answer)) 
        Question += 1
    print("You tried 3 questions and got %d right." % count)


# In[ ]:


askQuestion(Answer=['c', 'str', 'true'])

