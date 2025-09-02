# Honors ML Foundations 25-26
# To run this file, type 'python3 chatbot.py' in terminal. Make sure you are in the same folder as chatbot.py


topic = "Space Odessy" # TODO: Replace this with your topic


# TODO: Import libraries here
import random




knowledge = {
    # TODO: update this dictionary to store answers to questions


}


# TODO:Add helper functions to improve the organization of your code.





# TODO: Update this function to provide a response to the input question q
# NOTE: q is a list of words, for example ['hi', 'how', 'are', 'you?']
def getResponse(q):
    # remove this line of code and add your code here. 
    return "IDK"  











# ------------------ You probably do not need not modify below this line ------------------
print("Welcome to my chatbot about: ", topic)
while True:
    q = input("Enter a question or stop ")
    if q.lower() == "stop":
        break

    words = q.split() # splits sentence into a list of words
    a = getResponse(q)
    print(a)