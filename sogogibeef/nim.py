# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

marbles = 0

def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while ans * 2 <= n:
        ans *= 2
    return ans


print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))

player_turn = input("Who will start? (p or c): ") == 'p'

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    can_take = marbles // 2
    if player_turn:
        take = 0
        if can_take == 0:
            take = 1
        else:
            while not 1 <= take <= can_take:
                take = int(input("How many marbles to you want to take (1-" + str(can_take) + "): "))
    else:
        target = pow2(marbles) - 1
        take = marbles - target
        if not 1 <= take <= can_take:
            take = 1
        print("The computer takes", take, "marbles.")

    marbles -= take
    player_turn = not player_turn

if player_turn:
    print("The player wins!")
else:
    print("The computer wins!")
