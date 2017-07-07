numbers = []

def generatenumbers(start, end):
    while(start <= end):
        numbers.append(start)
        start=start+1
    return(numbers)
print(generatenumbers(1,9))
