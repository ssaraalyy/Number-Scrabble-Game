# This code Number scrabble game in which two players take turns to pick a number form a list until the two players pull out all the numbers in the list
# Then we check who collected three numbers the sum of them is 15
# By : Sara Ali Abdelbaki : 20210513


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = []
player2 = []
target = 15
print(list)
while list:
    num1 = int(input("Player1 Please choose a number: "))
    player1.append(num1) # adding number to player1 list
    list.remove(num1) # removeing the chosen number from the main list 
    print(list)
    if list == []: # if the main list is empty
        break
    num2 = int(input("Player2 Please choose a number: "))
    player2.append(num2) # adding number to player1 list
    list.remove(num2) # removeing the chosen number from the main list 
    print(list)

print(player1)
print(player2)


def winner1(): # to check if player1 has collected 3 numbers sum of them is 15
    if player1[0] + player1[1] + player1[2] == 15:
        return True
    elif player1[0] + player1[1] + player1[3] == 15:
        return True
    elif player1[0] + player1[2] + player1[3] == 15:
        return True
    elif player1[1] + player1[2] + player1[3] == 15:
        return True
    elif player1[0] + player1[1] + player1[4] == 15:
        return True
    elif player1[0] + player1[2] + player1[4] == 15:
        return True
    elif player1[0] + player1[3] + player1[4] == 15:
        return True
    elif player1[2] + player1[1] + player1[4] == 15:
        return True
    elif player1[3] + player1[1] + player1[4] == 15:
        return True
    elif player1[2] + player1[3] + player1[4] == 15:
        return True


def winner2(): # to check if player2 has collected 3 numbers sum of them is 15
    if player2[0] + player2[1] + player2[2] == 15:
        return True
    elif player2[0] + player2[1] + player2[3] == 15:
        return True
    elif player2[0] + player2[2] + player2[3] == 15:
        return True
    elif player2[1] + player2[2] + player2[3] == 15:
        return True


winner1()
winner2()

if winner1():
    print("Player1 Wins!!")
elif winner2():
    print("Player2 Wins!!")
else:
    print("Tie!")
