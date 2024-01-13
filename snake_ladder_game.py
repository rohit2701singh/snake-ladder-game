import random
from time import sleep  # sleep function will be used to delay the program
from art import logo
print("welcome to py snake-ladder game.")

print(logo)
dice = [1, 2, 3, 4, 5, 6]
ladder_numbers = [2, 9, 24, 31, 57, 63]
ladder_number_change = [40, 12, 43, 68, 65, 81]
snake_number = [30, 39, 75, 89, 91, 99]
snake_number_change = [13, 6, 25, 64, 51, 84]
player_sum_list = [94, 95, 96, 97, 98, 99]
dice_number_list = [6, 5, 4, 3, 2, 1]


def dice_choice():
    return random.choice(dice)


def found_six(players_dice):
    if players_dice == 6:
        return 1
    elif players_dice != 6:
        return 0


def snake(sum_of_player):
    if sum_of_player in snake_number:
        changing_sum = snake_number_change[snake_number.index(sum_of_player)]
        if sum_of_player == user_sum:
            print(f"🚨🐍 You found a snake at position {sum_of_player}.🐍🚨 your position reduce to {changing_sum}.\n")
        else:
            print(f"🚨🐍 computer found a snake at position {sum_of_player}.🐍🚨 computer's position reduce to "
                  f"{changing_sum}.\n")
        return changing_sum
    else:
        return sum_of_player


def ladder(sum_of_player):
    if sum_of_player in ladder_numbers:
        changing_sum = ladder_number_change[ladder_numbers.index(sum_of_player)]
        if sum_of_player == user_sum:
            print(f"🚨🪜 You found a ladder at position {sum_of_player}.🪜🚨 Your position increased to {changing_sum}\n")
        elif sum_of_player == computer_sum:
            print(f"🚨🪜computer found a ladder at position {sum_of_player}.🪜🚨 computer's position increased to"
                  f" {changing_sum}\n")
        return changing_sum
    else:
        return sum_of_player


def got_hundred_check(player_sum, player_dice):
    if player_sum < 100 and not player_sum > 100:
        if player_sum in player_sum_list:
            if player_dice <= dice_number_list[player_sum_list.index(player_sum)]:
                return player_sum + player_dice
            else:
                return player_sum
        else:
            return player_sum + player_dice
    elif player_sum > 100:
        return player_sum
    elif player_sum == 100:
        print("YOU WIN.")
        return player_sum + player_dice


user_sum = 0
computer_sum = 0
game_on = True
while game_on:
    print('----------------------------------')
    user = input("🎲 Press 'enter' roll the dice.\n----------------------------------\n")
    user_dice = dice_choice()
    sleep(0.3)
    print(f"your dice number is: {user_dice}.\ncomputer's turn.....")
    sleep(0.6)
    computer_dice = dice_choice()
    print(f"computer's dice number is: {computer_dice}\n")

    if user_sum == 0:
        user_sum = found_six(user_dice)
    elif user_sum != 0:
        user_sum = got_hundred_check(user_sum, user_dice)
        user_sum = snake(user_sum)
        user_sum = ladder(user_sum)
        if user_sum == computer_sum and computer_sum != 1:
            computer_sum = 0
            print("🚨 you are on computer's position. computer position becomes 0. 🚨\n")

    if computer_sum == 0:
        computer_sum = found_six(computer_dice)
    elif computer_sum != 0:
        computer_sum = got_hundred_check(computer_sum, computer_dice)
        computer_sum = snake(computer_sum)
        computer_sum = ladder(computer_sum)
        if computer_sum == user_sum and user_sum != 1:
            user_sum = 0
            print("🚨 computer is at your position. your position becomes 0. 🚨")

    print(f"your final total: {user_sum}\ncomputer's final total: {computer_sum}\n")

    print(f"your final position: {user_sum}\ncomputer final position: {computer_sum}\n")

    if user_sum == 100 or computer_sum == 100:
        if user_sum == 100:
            print("You reached at final position.\n🎉 YOU WIN.🎉")
            game_on = False
        elif computer_sum == 100:
            print("computer reached at final position.\n🎉YOU LOST.\n")
            game_on = False
