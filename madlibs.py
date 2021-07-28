#importing modules from libraries
import random
import time, sys


#This is a cool animation I found in a tutorial
def introduction():
    print_fast(
        "\033[1;37;50m ----------------------Welcome 𝖙𝖔 the 𝖌𝖆𝖒𝖊 𝖔𝖋 Madlibs!--------------------- \033[3;2;15m\n"
    )
    print_slow(
        "Basic Rules: Fill in each of the blank spaces with the appropriate type of word.Each blank notes what kind of word goes there, such as a noun, verb or adjective.\n"
    )


#The code for animation
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)


def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.03)


#calling the function
introduction()


#This converts list to string
def print_board(board):
    for i in range(board):
        print(" ".join([str(x) for x in board[i]]))


#setting nothing in noun value
noun_list = []

#defining nouns and repeating 2 times


def nouns():
    for x in range(2):
        user_nouns = input("To get started, enter a noun: ")
        noun_list.append(user_nouns)


verb_list = []


#defining verbs and repeating 2 times
def verbs():
    for i in range(2):
        user_verbs = input("Enter a verb: ")
        verb_list.append(user_verbs)


adjective_list = []


#defining adjectives and repeating 2 times
def adjectives():
    for j in range(2):
        user_adjectives = input("Enter an adjective: ")
        adjective_list.append(user_adjectives)


adverb_list = []


#defining adverbs and repeating 2 times
def adverbs():
    for y in range(2):
        user_adverbs = input("Enter an adverb: ")
        adverb_list.append(user_adverbs)


pastense_list = []


#defining past verbs and repeating 2 times
def past_verbs():
    for z in range(2):
        user_tense = input("Enter a pastense verb: ")
        pastense_list.append(user_tense)


def main():
    while True:

        genre_list = ['Trip to the zoo', 'Monkey king']
        print(genre_list)
        genre = input(
            "Press 1 for Trip to the zoo.Press 2 for monkey king: ")
        if (genre == "1"):
            print_slow(
                "Today I went to the zoo and I saw a(n) " +
                random.choice(adjective_list) + "" +
                random.choice(noun_list) +
                " jumping up and down on its tree. " + " "
                "He" + " " + random.choice(pastense_list) + " " +
                random.choice(adverb_list) +
                " through the large tunnel that led to its " + "" +
                random.choice(adjective_list) + " " + " " +
                random.choice(noun_list) +
                " I got some peanuts and passed them through the cage to a gigantic gray \n"
                + random.choice(noun_list) + "\n " +
                "towering above my head." + "I went to get a \n" +
                random.choice(adjective_list) + " scoop of ice cream." +
                "It filled my stomach.\n" + "\n" + "Afterwards, I had to " +
                random.choice(verb_list) + " " + random.choice(adverb_list) +
                " to catch our bus.\n" + "When I got home, I \n" +
                random.choice(pastense_list) + " my mom for a  " +
                random.choice(adjective_list) + " day at the zoo.")
            break
        elif(genre=="2"):

            print_fast(
                "The day I saw the monkey king " + random.choice(verb_list) +
                "was one of the most interesting days of the year. " +
                "After he did that, the king played chess on his brother's " +
                random.choice(noun_list) + " and then combined his " +
                random.choice(adjective_list) + " " +
                "hair with a comb made out of old fish bones. " +
                "Later that same day, I saw the monkey king dance " +
                random.choice(adverb_list) + " " +
                "infront of an audience of kangaroos and wombats.")
            break
        else:
          print_fast("You have entered an invalid option.")
          genre = input("Press 1 for Trip to the zoo.Press 2 for monkey king: ")
          
              
                


#Calling out each function for output.
nouns()
verbs()
adjectives()
adverbs()
past_verbs()
main()
