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
      index = stack.index(char)
      pops = len(stack)-index -1
      for p in range(pops):
        stack.pop()
        removing += 1
      assert (stack[-1] == char) 
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

