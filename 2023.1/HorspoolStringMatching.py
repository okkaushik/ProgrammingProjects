Tablesize = 100
Table = [0] * Tablesize

def ShiftTable(Pattern, m):
    for i in range(Tablesize - 1):
        Table[i] = m
    for j in range(m - 2):
        Table[ord(Pattern[j]) - 32] = m - 1 - j
    return Table

def HorspoolMatching(Pattern, Text):
    m = len(Pattern)
    n = len(Text)
    count = 0
    ShiftTable(Pattern,m)
    i = m - 1

    while i <= n - 1:
        k = 0
        while k <= m - 1 and Pattern[m - 1 - k] == Text[i - k]:
            k = k + 1
        if k == m:
            return i - m + 1
        else: 
            i = i + Table[ord(Text[i]) - 32]
            count = count + 1
            print("Number of comparisons made:", count)
    return -1

def main():
    while(1):
        Text = input("Enter a text to search (or key 'q' to exit):")
        if Text == 'q':
            print("End of the program\n")
            break

        Pattern = input("Enter a pattern to search:")
        position = HorspoolMatching(Pattern, Text)
        if position == -1:
            print("No Match Found..\n\n")
        else:
            print("Pattern", Pattern, "found in position", position, "..\n")

if __name__ == '__main__':
    main()

