def extract_even(l):
    result = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            result.append(l[i])
    return result  # cach 2 [return n for n in l if n % 2==0] 



n = input("enter many numbers: " )
num = [int (i) for i in n.split()]
even_num = extract_even(num)
print(even_num)