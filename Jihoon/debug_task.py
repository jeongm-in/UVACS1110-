# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)


def pow2(n):
    """Computes and returns the largest power of two that is no larger than n"""
    ans = 1
    while ans * 2 <= n:
        ans *= 2
    return ans


print("The Game of Nim\n")

marbles = 0
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))

turn_choice = input("Who will start? (p or c): ")
player_turn = turn_choice == 'p'

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    can_take = marbles // 2
    if player_turn:
        if can_take == 0:
            take = 1
        else:
            take = 0
            while take < 1 or take > can_take:
                take = int(input(
                    "How many marbles to you want to take (1-{}): ".format(
                        can_take)))
    else:
        target = pow2(marbles) - 1
        take = marbles - target
        if take < 1 or take > can_take:
            take = 1
        print("The computer takes", take, "marbles.")
    marbles -= take
    player_turn = not player_turn

print("The player wins!" if player_turn else "The computer wins!")
