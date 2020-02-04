##################################################################
#   Function : isElementValid
#
#   Description: It performs the following:
#               1. Checks if length of string is > 1024, if yes,
#                   returns True
#               2. Checks if the string contains the valid integer
#                  if yes, returns True
#                  else returns False
#   Input: String
#
#   Output: True if element is valid, False otherwise
##################################################################

def isElementValid(element):
    if(len(element) > 1024):
        return False

    try:
        int(element)
        return True
    except:
        return False


##################################################################
#   Function: findSecondLargestOfArray
#
#   Description: This function traverse the array elements one by 
#                one and does the following:
#              1. Checks if element is valid,
#              2. find secondLargest of the array, if it exists,
#              3. return -1 if there is no such element
#
#   Input: array of strings
#   
#   Output: second Largest of array in string form, if exists, 
#           -1 otherwise
###################################################################
def findSecondLargestOfArray(array):
    number = 0
    largest = float('-inf')
    secondLargest = float('-inf')
    isEleNotCorrect = False

    if(len(array) == 0):
        return -1
    
    for ele in array:
        if(True == isElementValid(ele)):
            number = int(ele)

            if(number > largest):
                secondLargest = largest
                largest = number

            elif((number != largest) and (number > secondLargest)):
                secondLargest = number
    
        else:
            isEleNotCorrect = True
            break

    if((True == isEleNotCorrect) or (float('-inf') == secondLargest)):
        return -1
    else:
        return str(secondLargest)


################################################################
#   Function : main()
#   Description: This is main driver function which takes array 
#               size and array element fron user.
#               It also calls the findSecondLargestOfArray() and 
#               prints the result returned.
#
#   Input: None
#
#   Output: None
################################################################
def main():
    arrSize = 0
    arr = []
    result = 0
    
    arrSize = int(input("Enter Number Of Elements in array\n"))
    if(arrSize == 0):
        result = -1
        print("\nResult is {}".format(result))
    
    print("Enter Array Elements\n")
    
    for i in range(0, arrSize):
        element = input()
        arr.append(element)

    result = findSecondLargestOfArray(arr)
    print("\nResult is {}".format(result))

if __name__ == "__main__":
    main()

