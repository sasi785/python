n=int(input("Enter a number:"))
for i in range(n+1):
      isprime = True
      for n in range(2,i):
          if i%n == 0:
              isprime = False
if isprime:
      print("Prime Number")
else:
    print("Not Prime")
