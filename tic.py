#have a coinflip event
import random

wins1 = 0
wins2 = 0
while True:
    rounds = input("Please enter the number of games you want to play\n")
    rounds = int(rounds)
    if (wins1 + wins2) >= rounds:
        if (wins1 > wins2):
            print("Player one wins overall")
            print("The game-ending score is " + str(wins1) + " to " + str(wins2))
        if (wins2 > wins1):
            print("Player two wins overall")
            print("The game-ending score is " + str(wins2) + " to " + str(wins1))
    while (wins1 + wins2) < rounds:

        if (wins1 + wins2) < 1:
            choice = input("Discuss amongst yourselves who wants heads or tails, then hit enter\n")

            if random.randint(0, 1) == 0:
                print('coin is heads!')
            else:
                print('coin is tails!')

        arr = [[0]*3 for _ in range(3)]
        win = True
        track = 0
        while win:
            if track % 2 == 0:
                sane = True
                while sane:
                    move = input("Player one input: ")
                    move1 = move.split(" ")
                    xy = [int(x.strip()) for x in move1]
                    if arr[xy[0]][xy[1]] == 0:
                        sane = False
                    else:
                        print("Invalid move")
                arr[xy[0]][xy[1]] = "x"
            else:
                sane = True
                while sane:
                    move = input("Player two input: ")
                    move1 = move.split(" ")
                    xy = [int(x.strip()) for x in move1]
                    if arr[xy[0]][xy[1]] == 0:
                        sane = False
                    else:
                        print("Invalid move")
                arr[xy[0]][xy[1]] = "o"
            print(arr[0])
            print(arr[1])
            print(arr[2])
            track += 1
            #check for winner
            #across
            one = 0
            two = 0
            for x in arr[0]:
                if x == "x":
                    one += 1
                if x == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
            one = 0
            two = 0
            for x in arr[1]:
                if x == "x":
                    one += 1
                if x == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
            one = 0
            two = 0
            for x in arr[2]:
                if x == "x":
                    one += 1
                if x == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
            #down
            one = 0
            two = 0
            j = 0
            for x in arr[0]:
                if arr[j][0] == "x":
                    one += 1
                if arr[j][0] == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
                j+=1
            one = 0
            two = 0
            j = 0
            for x in arr[0]:
                if arr[j][1] == "x":
                    one += 1
                if arr[j][1] == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
                j+=1
            one = 0
            two = 0
            j = 0
            for x in arr[0]:
                if arr[j][2] == "x":
                    one += 1
                if arr[j][2] == "o":
                    two += 1
                if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
                if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
                j+=1
            #diagonal
            #right
            one = 0
            two = 0
            temp = arr[0][2]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1
            temp = arr[1][1]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1
            temp = arr[2][0]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1 
            if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
            if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break
            #left
            one = 0
            two = 0
            temp = arr[0][0]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1
            temp = arr[1][1]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1
            temp = arr[2][2]
            if temp == "x":
                one+=1
            if temp == "o":
                two+=1 
            if one == 3:
                    wins1 += 1
                    print("Player one is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins1) + " to " + str(wins2))
                    win = False
                    break
            if two == 3:
                    wins2 += 1
                    print("Player two is the winner")
                    if (wins1 + wins2) < rounds:
                        print("The score is " + str(wins2) + " to " + str(wins1))
                    win = False
                    break