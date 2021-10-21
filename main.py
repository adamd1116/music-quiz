import random

password = input("\nEnter your password: ")

songs = {
    "kanye": "Off the Grid",
}

song_artist = ['kanye']

def rand_selection():
    return random.randint(0,6)

#chosenSong = songs[random.choice(song_artist)]

with open('password.txt', 'r') as f:
    if password == f.read():
        print("\n\tCorrect")
        passw_correct = True
    else:
        print("\n\tIncorrect")
        passw_correct = False

test = list(songs.keys())
print(test)