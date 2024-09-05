n = int(input())


sequence = [0, 1, 2]

for i in range(n):
    if i < 2:
        print(sequence[i] + 1)  
    else:
        next_number = sequence[0] + sequence[1] + sequence[2]
        print(next_number)
        
        sequence[0], sequence[1], sequence[2] = sequence[1], sequence[2], next_number