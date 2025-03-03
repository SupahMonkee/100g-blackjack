#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  aces = ['AC','AD','AH','AS']
  acecount = 0
  isace = 0
  for i in aces:
    if aces[acecount] in hand:
      score = []
      isace = 1
    else:
      pass
    acecount += 1
  
  
  return score


print(value(['AH','3D','4S']))


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()

