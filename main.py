import random

password = input("\nEnter your password: ")

songs = {
    "kanye": "Off the Grid",
}

song_artist = ['kanye']

def rand_selection(x):
    return random.choice(x)

with open('password.txt', 'r') as f:
    if password == f.read():
        print("\n\tCorrect")
        passw_correct = True
    else:
        print("\n\tIncorrect")
        passw_correct = False

if passw_correct == True:
    chosen 