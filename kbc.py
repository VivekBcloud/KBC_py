from questions import QUESTIONS

def isAnswerCorrect(question, answer):
    return True if answer == question["answer"] else False

def lifeLine(ques):
    correct_answer ="option" + str(ques["answer"])
    deleted_options = 0
    i = 1
    while deleted_options < 2:
        option = "option" +str(i)
        if option != correct_answer:
            ques[option] = "Option deleted!"
            deleted_options += 1
        i += 1
    return ques

def is_input_valid(ans):
    try:
        ans = int(ans)
        if 0 < int(ans) < 5:
            return True
        else:
            return False
    except ValueError:
        return False
    
        
        
def kbc():

    round = 0
    money_won = 0
    lifeLine_available = 'Available'
    while round < 15:
         
        print(f'\tMoney:',QUESTIONS[round]["money"])
        print(f'\tQuestion {round+1}: {QUESTIONS[round]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[round]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[round]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[round]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[round]["option4"]}')
        print(f'\tLifeline: {lifeLine_available} (type lifeline to use)')
        ans = input('Your choice ( 1-4 )(type quit - to quit) : ')
        if ans.lower() == 'lifeline' and lifeLine_available == 'Available' and round < 14:
            QUESTIONS[round] = lifeLine(QUESTIONS[round])
            lifeLine_available = 'Not Available'
        else:
            if ans.lower() =='quit':
                print("Congratulation you won:", QUESTIONS[round-1]["money"] if round > 0 else 0)
                print("The Correct Answer was:",QUESTIONS[round]["answer"])
                return
            # check for the input validations
            if is_input_valid(ans):

                if isAnswerCorrect(QUESTIONS[round], int(ans) ):
                    print('\nCorrect ! \n')
                    round += 1
                    if round == 5:
                        print(f'\t\tCongratulation you have crossed the First level!!! the minimum reward becomes Rs. 10,000')
                        money_won = 10000
                    if round == 11:
                        print(f'\t\tCongratulation you have crossed the Second level!!! the minimum reward becomes Rs. 3,20,000')
                        money_won = 320000
                    if round == 15:
                        print("*** Congrats You have become a Millionaire now |o| ***")
                else:
                    print('\nIncorrect !')
                    print("The Correct Answer was:",QUESTIONS[round]["answer"] )
                    print("Congratulation you won:", money_won)
                    return
                
            else:
                print("Invalid Input")

kbc()
