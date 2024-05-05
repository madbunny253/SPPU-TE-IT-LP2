def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    towers_of_hanoi(n-1, auxiliary, target, source)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    towers_of_hanoi(n, 'A', 'C', 'B')
