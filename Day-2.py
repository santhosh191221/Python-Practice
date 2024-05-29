# Write a Python program to get the Fibonacci series between 0 to 50.


f = 0
s = 1

for i in range(0,50):
    print(f)
    t = f
    f = s
    s = s + f

