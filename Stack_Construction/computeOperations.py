def computeOperations(displayMessage):
  #print("about to process:" + displayMessage)
  charList = list(displayMessage)
  stack = []
  adding =  0
  printing = 0
  removing = 0
  for char in charList:
    if not stack:
      stack.append(char)
      adding += 1
    elif char in stack:
      while char != stack[-1]:
        removing += 1
        stack.pop()
    else:
      stack.append(char)
      adding += 1
    printing += 1
  removing += len(stack)
  #print("adding:" +  str(adding))
  #print("priting:" +  str(printing))
  #print("removing:" +  str(removing))
  numberOfOperations = adding + printing + removing
  return numberOfOperations

