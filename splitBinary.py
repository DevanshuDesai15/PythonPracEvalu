'''Question:-
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''
#Here input is taken as list
list = []
binary = [digit for digit in input().split(',')]
#will check if the number in binary is divisible by 5 or not
for num in binary:
    x = int(num, 2)
    if not x%5:
        list.append(num)
#will print the numbers which are divisible by 5
print(','.join(list))
