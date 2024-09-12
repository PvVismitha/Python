"""
Task - Counters

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N , the number of customers.
The next N lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Output Format

Print the amount of money earned by .

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output

200

hackerrank problem
https://www.hackerrank.com/challenges/collections-counter/
"""




from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_shoes = int(input())
size_list = [int(a) for a in input().split()]
num_of_customers = int(input())
cust_list = list()
for i in range(num_of_customers):
    cust_list.append([int(a) for a in input().split()])

total_amount = 0
size_counter = Counter(size_list)
for k,v in cust_list:
    print(k,v)
    if size_counter[k] > 0:
        size_counter[k] -=  1
        total_amount = total_amount + v
        print(size_counter)

print(total_amount)

