from random import randint
with open("input.txt", "w") as file:
    n = 4
    [[file.write(f"{randint(1, n+1)} {randint(1, n+1)} ") if (i != j) else None for j in range(randint(1, n+1))] for i in range(randint(1, n+1))]