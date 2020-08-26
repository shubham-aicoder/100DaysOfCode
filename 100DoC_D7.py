def monoArray(array):
    # Write your code here.
    if array==sorted(array) or array==sorted(array,reverse=True):
        return True
    return False


if __name__ == "__main__":
  array = [1,100,1000]
  print(monoArray(array))
