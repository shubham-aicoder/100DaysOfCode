def twoNumberSum(array,targetSum):
    """
        Input: A non-empty array of intgers along with target sum
        Expected Output: An array consisting of two integers sums to target sum
        else an empty array is returned

    """
    j=0
    d=dict.fromkeys(array,0)
    for i in d:
        d[i]=j
        j+=1
    for i in range(len(array)):
        value=targetSum-array[i]
        if value in d.keys() and array[i]!=value:
            l=[array[i],value]
            return l
    return []       
   


if __name__=='__main__':
    print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))
