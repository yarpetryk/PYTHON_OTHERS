data = [5, 1, 4, 7, 50, 2, 7]
data.sort()

def sort_list(input: list) -> list:
    n = len(input)
    for i in range(n):
        for j in range(n-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    print(input)


sort_list(data)