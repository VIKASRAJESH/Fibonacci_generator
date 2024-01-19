def fibonacci_generator():
    n=input("Enter How many Fibonaccis to generate?(n):")
    n=int(n)
    a=0
    b=1
    if n < 0:
        print("Invalid 'n' value.")
    elif n == 0:
        print(0)
    else:
        for i in range(n):
            print(b)
            a,b= b,a+b
 
fibonacci_generator()
