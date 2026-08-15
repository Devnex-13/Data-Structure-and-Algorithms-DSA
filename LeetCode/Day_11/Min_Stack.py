class MinStack(object):

  def init(self):
    self.stack = []
    self.minStack = []

  def push(self, value):
    if(self.stack):
      self.minStack.append(min(value,self.minStack[-1]))
    else:
      self.minStack.append(value)
    self.stack.append(value)

  def pop(self):
    self.stack.pop()
    self.minStack.pop()

  def top(self):
    return self.stack[-1]

  def getMin(self):
    return self.minStack[-1]