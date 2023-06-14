
def fibonacci(n):
    if n<=0:
        print("Enter a valid number to find fibonacci series")
        return
    if n==1:
        return [0]
    elif n==2:
        return [1]

    series = [0,1]
    while len(series)<n:
        next_num = series[-1]+series[-2]
        series.append(next_num)
    return series

num=int(input("Enter the number of fibonacci terms you want to generate: "))
fibonacci_series=fibonacci(num)
print(fibonacci_series)

