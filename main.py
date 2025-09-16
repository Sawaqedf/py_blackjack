import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def decide_winner(player_cards_array, computer_cards_array):
    """Takes the cards of 2 players in a blackjack game to decide the winner"""
    total_player_score = sum(player_cards_array)
    total_computer_score = sum(computer_cards_array)

    if total_player_score == 21 and len(player_cards_array) == 2:
        print("You win with a Blackjack!!")
    elif total_computer_score == 21 and len(computer_cards_array) == 2:
        print("Opponent has a Blackjack. You Lose!")
    elif total_player_score == 21 and len(player_cards_array) == 2 and total_computer_score == 21 and len(computer_cards_array) == 2:
        print("Both players have a Blackjack. It is a draw!")
    elif total_computer_score > 21 >= total_player_score:
        print("Opponent went over. You win!")
    elif total_computer_score > 21 and total_player_score > 21:
        print("Both players went over. It is a draw!")
    elif total_player_score > 21 >= total_computer_score:
        print("You went over. You lose!")
    elif total_player_score > total_computer_score:
        print("You scored higher than the opponent. You win!")
    elif total_computer_score > total_player_score:
        print("Your opponent scored higher than you. You lose!")
    elif total_player_score == total_computer_score:
        print("Both opponents have the same score. It is a draw!")
    else:
        print("Ending missed, fix code to improve!")

def computer_controller(player_cards_array, computer_cards_array):
    """Takes the cards of 2 players in a blackjack game to decide how the computer will play the game"""
    computer_final_hand = computer_cards_array
    computer_total_score = sum(computer_cards_array)
    computer_has_finished = False
    while not computer_has_finished:
        if computer_total_score >= 17:
            computer_has_finished = True
        elif 12 <= computer_total_score <= 16 and 2 <= player_cards_array[0] <= 6:
            computer_has_finished = True
        elif computer_total_score <= 11:
            new_card = random.choice(cards)
            computer_final_hand.append(new_card)
            computer_total_score += new_card
        elif 12 <= computer_total_score <= 16 and player_cards_array[0] >= 7:
            new_card = random.choice(cards)
            computer_final_hand.append(new_card)
            computer_total_score += new_card
        else:
            computer_has_finished = True
            print("Error: Missed Ending, try fixing")

        while 11 in computer_final_hand and computer_total_score > 21:
            ace_index = computer_final_hand.index(11)
            computer_final_hand[ace_index] = 1
            computer_total_score -= 10

    return computer_final_hand

start_game = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower()
start_new_game = True

if start_game == "n":
    start_new_game = False
elif start_game == "y":
    start_new_game = True
else:
    print(f"{start_game} is not a valid input, so it will be regarded as no.")
    start_new_game = False

while start_new_game:
    if start_game == "y":

        print("\n" * 100)
        print(art.logo)

        player_cards = random.choices(cards, k=2)
        player_current_score = sum(player_cards)

        computer_cards = random.choices(cards, k=2)
        computer_score = sum(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_current_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        get_card = input("Type 'y' to get another card, or type 'n' to pass: ").lower()

        if get_card == "n":
            computer_final_cards = computer_controller(player_cards, computer_cards)
            computer_final_score = sum(computer_final_cards)

            print(f"Your final hand: {player_cards}, final score: {player_current_score}")
            print(f"Computer's final hand: {computer_final_cards}, final score: {computer_final_score}")

            decide_winner(player_cards, computer_cards)

            play_again = input("Do you want to play a new game of Blackjack? Type 'y' for yes for 'n' for no: ")

            if play_again == "n":
                start_new_game = False
            elif play_again == "y":
                start_new_game = True
            else:
                print(f"{play_again} is not a valid input, so it will be regarded as no.")
                start_new_game = False
        elif get_card == "y":
            more_cards = True
            player_final_score = 0

            while more_cards:
                new_player_card = random.choice(cards)
                player_cards.append(new_player_card)
                player_final_score = sum(player_cards)

                while 11 in player_cards and player_final_score > 21:
                    ace_index = player_cards.index(11)
                    player_cards[ace_index] = 1
                    player_final_score -= 10

                print(f"Your cards: {player_cards}, current score: {player_final_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                if player_final_score > 21:
                    more_cards = False

                if more_cards:
                    get_another_card = input("Type 'y' to get another card, or type 'n' to pass: ").lower()

                    if get_another_card == "n":
                        more_cards = False
                    elif get_another_card == "y":
                        more_cards = True
                    else:
                        print(f"{get_another_card} is not a valid answer, so it will be used as a pass")
                        more_cards = False

            computer_final_cards = computer_controller(player_cards, computer_cards)
            computer_final_score = sum(computer_final_cards)

            print(f"Your final hand: {player_cards}, final score: {player_final_score}")
            print(f"Computer's final hand: {computer_final_cards}, final score: {computer_final_score}")

            decide_winner(player_cards, computer_final_cards)

            play_again = input("Do you want to play a new game of Blackjack? Type 'y' for yes for 'n' for no: ")

            if play_again == "n":
                start_new_game = False
            elif play_again == "y":
                start_new_game = True
            else:
                print(f"{play_again} is not a valid input, so it will be regarded as no.")
                start_new_game = False
    else:
        pass
