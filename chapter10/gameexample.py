class Remote:
    pass
class Player:
    def MoveRight(self):
        pass
    def MoveLeft(self):
        pass
    def MoveTop(self):
        pass
Remote1=Remote()#object instantiation
Player1=Player()#object instantiation

if (Remote1.isLeftPressed()):
    Player.MoveLeft()
    