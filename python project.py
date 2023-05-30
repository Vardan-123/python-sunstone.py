print("Welcome To The Quiz! ")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
  quit()

print("Yes, Lets play!")
score = 0
answer = input("How many players in the cricket? ")
if answer.lower() == "11":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What is the drs full form ? ")
if answer.lower() == 'decision review system ':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("who is called as god of cricket? ")
if answer.lower() == 'sachin tendulkar':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("who is the most followed cricketer in indian cricket team  ")
if answer.lower() == 'virat kohli':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What is the full name of MSD ? ")
if answer.lower() == 'mahendra singh dhoni ':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What is the length cricket pitch? ")
if answer.lower() == '20.12 M':
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 6) * 100) + "%")
