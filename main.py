import random

password = input("\nEnter your password: ")

songs = {
    "Kanye": "Off The Grid",
    "Future": "Life Is Good",
}

song_artist = list(songs.keys())
song_names = list(songs.values())

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
    pass

choice1 = str(song_names[1])
choice1_m = list(choice1)
b = 0


for i in range(len(choice1_m)):
    if i == 0:
        pass
    else:
        choiceindex = choice1.find(choice1[i])
        if choice1[i] != " " and choice1[i].isupper() != True:
            choice1_m[choiceindex] = "_"
            if i < len(choice1_m)-1 and choice1[i] == choice1[i+1]:
                choice1_m[choiceindex+1] = "_"
        else:
            choice1_m[choiceindex] = choice1[i]

e = "".join(choice1_m)
print(e)