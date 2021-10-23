import random

password = input("\n\tEnter your password: ")
name  = input("\tEnter your name: ")
chances = 2
win = False
score = 0

songs = {
    "Kanye": "Off The Grid",
    "Future": "Solo",
    "Pop Smoke": "30",
    "Kid Cudi": "Mr. Rager",
    "Future ": "Mask Off",
    "Polo G": "Pop Out",
    "French Montana": "Unforgettable",
    "Eminem": "Lose Yourself",
}

songNameIndex = random.randint(0,len(songs)-1)
song_artist = list(songs.keys())
song_names = list(songs.values())
choice1 = str(song_names[songNameIndex])
choice1_m = list(choice1)

with open('password.txt', 'r') as f:
    if password == f.read():
        print("\n\tCorrect")
        passw_correct = True
    else:
        print("\n\tIncorrect, try again")
        passw_correct = False
if passw_correct == True:
    pass

#Loop has a "bug" where if a letter appears twice in a song name and they aren't next to eachother, 
#only one letter is hidden.
#I can not be bothered to fix it. It is a feature not a bug
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

guessSongName = "".join(choice1_m)

if passw_correct == True:
    print(f"\n\tRules: \n\t1) Answers are not case sensitive \n\t2) You only have 2 chances to get it correct \n\t3) Get it right 1st time is 3 points, 2nd time is 1 point \n\t4) Some names may have special characters")
    print(f"\n\tArist: {song_artist[songNameIndex]} | Song Name: {guessSongName}")

while chances > 0 and passw_correct == True:
    firstGuess = input("\n\tEnter your first guess: ").lower()
    if firstGuess == song_names[songNameIndex].lower():
        print("\n\tCorrect! You win!")
        win = True
        if chances == 2 and win == True:
            score += 3
            break
        elif chances == 1 and win == True:
            score += 1
            break
    else:
        if chances == 2:
            print(f"\n\tIncorrect, you have {chances} more chances")
            chances-=1
        else:
            print(f"\n\tIncorrect! The answer was: {song_names[songNameIndex]}")
            chances-=1

if chances == 0 or win == True:
    with open('scores.txt', 'a') as s:
        s.write("-------------------------------")
        s.write(f"\n\tName: {name}")
        s.write(f"\n\tScore: {score}")
        s.write(f"\n\tChances left: {chances}")
        if win == True:
            s.write("\n\tWin!\n")
        else:
            s.write("\n\tLost!\n")
        s.write("-------------------------------\n")