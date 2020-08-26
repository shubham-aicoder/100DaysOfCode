def num_conversion(input_number):
  #write your code here
    int_to_roman=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    res=[]
    for (i,j) in int_to_roman:
        (factor,input_number) = divmod(input_number,i)
        res.append(j * factor)
        if input_number == 0:
            break
    return "".join(res)
if __name__ == "__main__":
  input_number = 1994
  print(num_conversion(input_number))






















