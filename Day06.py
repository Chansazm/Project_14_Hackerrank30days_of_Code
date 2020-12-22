# Enter your code here. Read input from STDIN. Print output to STDOUT
Test_cases = int(input())

for i in range(Test_cases):
    Test_string = input()
    even = ''
    odd = ''
    for j in range(len(Test_string)):
        if (j % 2 == 0):
            even += Test_string[j]
        else:
            odd += Test_string[j]
    print('{} {}'.format(even,odd))

