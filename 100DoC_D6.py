def moveElementToEnd(array, toMove):
    # Write your code here.
    for i in array:
        if i==toMove:
            array.append(i)
            array.remove(i)
    return array


if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
