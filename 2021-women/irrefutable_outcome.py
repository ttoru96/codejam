def solve(s):
    turn = True
    while True:
        
        print("inside while loop")
        print(turn)
        turn = not turn


if __name__ == "__main__":
    T = int(input()) # the number of testcases
    for i in range(T):
        s = input()
        print(f'Case #{T}: {solve(s)}')
