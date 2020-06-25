
import math
import os

def formatCommand(stringCommand):
    # Make it to where all elems are separated by 1 whitespace
    oneSpaceAlr = False
    formatStr = ''
    stringCommand = stringCommand.lstrip()
    stringCommand = stringCommand.rstrip()
    for i in stringCommand:
        if i.isspace() and oneSpaceAlr == False:
            formatStr += ' '
            oneSpaceAlr = True
        if i.isalpha():
            oneSpaceAlr = False
            formatStr += i
        if i.isdigit():
            oneSpaceAlr = False
            formatStr += i
    formatStr += ' '
    return formatStr
    
def returnArray(str0):
    # Take the formatted string and return array
    array = []
    temp = ''
    for i in str0:
        if i.isalpha():
            temp += i
        if i.isdigit():
            temp += i
        if i.isspace():
            if temp.isdigit():
                array.append(int(temp))
            else:
                array.append(temp)
            temp = ''
            
    return array


arr = []

if __name__ == '__main__':
    N = int(input())
    
    for i in range(N):
        comm = formatCommand(input())
        commArr = returnArray(comm)
        #print(comm)
        #print('length ', len(comm))
        #print(returnArray(comm))
        if commArr[0] in 'insert':
            arr.insert(commArr[1], commArr[2])
        if commArr[0] in 'print':
            print(arr)
        if commArr[0] in 'remove':
            arr.remove(commArr[1])
        if commArr[0] in 'append':
            arr.append(commArr[1])
        if commArr[0] in 'sort':
            arr.sort()
        if commArr[0] in 'pop':
            arr.pop()
        if commArr[0] in 'reverse':
            arr.reverse()
            
        
        
        '''
        Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
        
        
