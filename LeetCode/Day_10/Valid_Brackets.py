def isValid(self, s):
      pairs = {
          "(":")",
          "{":"}",
          "[":"]"
      }
      stack = []

      for r in range(len(s)):
          if len(s)>1 and s[0] in pairs:
              if s[r] in pairs:
                  stack.append(pairs[s[r]])
              else:
                  if(stack and s[r] == stack[len(stack)-1]):
                    stack.pop()
                  else:
                    return False
          else:
              return False
      if(stack):
          return False
      else:
          return True