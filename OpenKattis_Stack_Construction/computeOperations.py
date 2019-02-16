def computeOperations(displayMessage):
  print("about to process:" + displayMessage)
  charList = list(displayMessage)
  adding =  len(charList)
  printing = len(charList)
  removing = len(charList)
  numberOfOperations = adding + printing + removing
  return numberOfOperations


#import sys
#rows = 0
#for i in sys.stdin:
#  if not rows == 0:
#    print(computeOperations(i))
#  else:
#    rows = int(i)