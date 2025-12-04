# Honors ML Foundations 25-26
# To run this file, type 'python3 chatbot.py' in terminal. Make sure you are in the same folder as chatbot.py


topic = "Key Club"


# TODO: Import libraries here
import random
from spellchecker import SpellChecker
spell = SpellChecker()

from fuzzywuzzy import process


knowledge = {
    # TODO: update this dictionary to store answers to questions
    "What is Key Club?": "Key Club's an organization that allows high school students too participate in service projects in their local communities.",
    "When did you join the club?": "I joined Key Club in my freshman year of high school",
    "Why did you join the club?": "I originally joined Key Club because I wanted to start building my college application and my parents wanted me to join a club.",
    "What is your role in the club?": "My current role in the club is President.",
    "Do you actually enjoy serving your community or are you just doing it to look good among your peers?": "After spending 2-3 years in Key Club, I have come to actually enjoy going to service projects and giving back to my local community.",
    "Do you think you have actually had a meaningful impact on your community?": "I would think so, as we have heard from multiple organizations that we have supported previously that Key club has played a major role in running community events.",
    "Do you actually like your fellow officers and advisors?": "Yes, the officers and advisors for our club and our division are very helpful in completing monthly tasks and organizing the club.",
    "What was your favorite Key Club project?": "My favorite service project would most likely be the mochitsuki event where we gor to pound and make mochi to sell.",
    "What was your least favorite Key Club project?": "My least favorited service project would probably be poster making because I am not very creative and I am not skilled in design.",
    "How do you join Key Club?": "If you want to join KeyClub, go and find a Key Club advisor and ask them for a membership form.",
    "Why should you join Key Club?": "It's a great way to give back to your local community and stat pad your college app.",
    "Is Key Club even good?": "Definetly",
    "Why is it callen Key Club?": "Because bread tastes better than key",
    "Who is Key Club?": 'What type of question is that bro?",
    "Is there food at Key Club?": "Sometimes",
    "How many hours do you need to be in key Club?": "Like 6-7 hours",
    "What is KeyClub even about?": "Service projects and collaboration.",
    "Do you want to leave Key Club?": "Never",
    "When was Key Club made?": "Sometime a hwile ago",
    "What if I don't have any hours in Key Club?": "That's on you bro",
    "Can you give me hours in Key Club?": "No",
    "Can you give me a officer position in Key Club?": "No, but you can apply for it",
    "What if I have 67 hours?": "Congrats ig",
    "what do you think about the advisors?": "They're actually helpful"


}


# TODO:Add helper functions to improve the organization of your code.





# TODO: Update this function to provide a response to the input question q
# NOTE: q is a list of words, for example ['hi', 'how', 'are', 'you?']

def correct_spelling(question):
    words = question.split()
    corrected_words = [spell.correction(word) or word for word in words]
    return " ".join(corrected_words)


def getResponse(q):                                                                                                                 
    q = correct_spelling(q)
    
    match, score = process.extractOne(q, knowledge.keys())

    if score >= 90:
        return knowledge[match]
    else:
        fallback_responses = [
            "bro what",
            "idk",
            "what are yall talking afout"
        ]
        return random.choice(fallback_responses)











# ------------------ You probably do not need not modify below this line ------------------
print("Welcome to my chatbot about: ", topic)
while True:
    q = input("Enter a question or stop ")
    if q.lower() == "stop":
        break

    words = q.split() # splits sentence into a list of words
    a = getResponse(q)
    print(a)