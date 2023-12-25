
from Gridworld import Gridworld
game = Gridworld(size=4, mode='static')


print(game.display())
"""
『u』代表『向上』
『d』代表『向下』
『l』代表『向左』
『r』代表『向右』
"""
while True:
    move = input("Your move:")
    game.makeMove(move)
    print(game.display(),"reward:",game.reward())
    if game.reward() ==10 or game.reward() ==-10:
        print("End")
        break
