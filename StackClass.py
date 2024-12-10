#Luke Brudnok
#12/5/24

class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = 0



  def push(self, el):
    """Append an element to the end of the stack"""
    self.__stack.append(el)
    self.__size += 1

  def pop(self):
    """Remove the last element in the stack and return it"""
    if self.__is_empty() == False:
      n = self.__stack[-1]
      self.__stack.delete[-1]
      self.__size -= 1
      return n
    else:
      raise IndexError("cannot pop from empty stack")

  def top(self): 
    """Return the last element in the stack"""
    if self.__is_empty() == False:
      return self.__stack[-1]
    else:
      raise IndexError("cannot return from empty stack")

  def __is_empty(self):
    return (len(self.__stack) == 0)

  def __len__(self):
    """Return the number of elements in the stack"""
    return self.__size

  def __str__(self):
      """Display contents of stack"""
      out = ""
      for ele in self.__stack:
          out += str(ele) + ' '

      out += "<TOP"
      return out
