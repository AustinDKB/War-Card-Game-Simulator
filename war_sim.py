import random

def war_handler():
    war_handler.count += 1
    print("War is {0} is happening.").format(war_handler.count)

    if len(player_one) > 4 and len(player_two) > 4:
        limiter = 3
    elif len(player_one) == 4 or len(player_two) == 4:
        limiter = 2
    else:  # len(player_one) < 4 or len(player_two) < 4:
        if len(player_one) > len(player_two):
            limiter = len(player_two) - 2
        else: # len(player_one) < len(player_two)
            limiter = len(player_one) - 2

    w, x, y, z = 0, 0, 0, 0

    for w in range(0, limiter):
        temp.append(player_one[w])
        temp.append(player_two[w])
    random.shuffle(temp)

    while x <= 4:
        player_one.remove(player_one[0])
        player_two.remove(player_two[0])
        x += 1

    if not player_one or not player_two:
            print("\n\n\n\n\n")
    else:
        if player_one[0] > player_two[0]:
            temp.append(player_one[0])
            temp.append(player_two[0])

            player_one.remove(player_one[0])
            player_two.remove(player_two[0])

            for y in range(0, len(temp)):
                player_one.append(temp[y])

        elif player_one[0] < player_two[0]:
            temp.append(player_one[0])
            temp.append(player_two[0])

            player_one.remove(player_one[0])
            player_two.remove(player_two[0])

            for z in range(0, len(temp)):
                player_two.append(temp[z])

        else:  #player_one[0] == player_two[0]:
            war_handler()

print("##################################################")
print("#           War Card game simulator!             #")
print("#          Written By: Austin Bakanec            #")
print("#               99.97% Accurate                  #")
print("##################################################")

# Init important variables and get players names
player_one_name = raw_input("Whats Player one's name? ")
player_two_name = raw_input("Whats Player two's name? ")
player_one = []
player_two = []
temp = ""
i = 0

# Input the players cards!
while i <= 1:
    # Get Player one's cards
    if i == 0:
        print("Input player {0}'s cards. Note: Capitals only!").format(player_one_name)
        while temp != "END":
            player_one.append(temp)
            temp = raw_input("Card: ")

        # Remove the blank in the array
        if '' in player_one: player_one.remove('')
        i += 1
    # Get Player two's cards
    if i == 1:
        temp = ''
        print("Input player {0}'s cards. Note: Capitals only!").format(player_two_name)
        while temp != "END":
            player_two.append(temp)
            temp = raw_input("Card: ")

        # Remove the blank in the array
        if '' in player_two: player_two.remove('')
        i += 1

# Switch the alphabet to numbers 1 - 10, j, q, k , a for each deck # Switch to dictionary
translation_list = ['J', 'Q', 'K', 'A']
translation_list_1 = ['11', '12', '13', '14']
for i in range(0, len(translation_list)):
    player_one = [item.replace(translation_list[i], translation_list_1[i]) for item in player_one]
    player_two = [item.replace(translation_list[i], translation_list_1[i]) for item in player_two]

# Make the lists integers
player_one = [int(num) for num in player_one]
player_two = [int(num) for num in player_two]

total_wars = 0

# Play the game!
while player_one and player_two:
    temp = []
    # War Sim
    ###################################################################################################################
    if player_one[0] == player_two[0] and len(player_one) >= 4 and len(player_two) >= 4:
        war_handler.count = 0
        war_handler()
        total_wars += war_handler.count
        # War sim over

    # Simple determination of winner
    elif player_one[0] != player_two[0]:
        temp.append(player_one[0])
        temp.append(player_two[0])

        random.shuffle(temp)

        player_one.remove(player_one[0])
        player_two.remove(player_two[0])

        if player_one > player_two:

            player_one.append(temp[0])
            player_one.append(temp[1])

        else:  # player_one < player_two

            player_two.append(temp[0])
            player_two.append(temp[1])
    else:
        continue

if not player_one:
    print("Player {0} Wins!").format(player_two_name)
elif not player_two:
    print("Player {0} Wins!").format(player_one_name)

print("War Count: {0}").format(total_wars)
