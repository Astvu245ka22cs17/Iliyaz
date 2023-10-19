class player:
  def play(self):
    print("The player is playing Cricket ")
class batsman(player):
  def play(self):
    super().play()
    print("The batsman is batting")
class bowler(player):
  def play(self):
    print("The bowler is bowling")
bt=batsman()
bw=bowler()
bt.play()
bw.play()