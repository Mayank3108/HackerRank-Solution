def minion_game(string):
    vowel = 'AEIOU'
    kevin= 0
    stuart=0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)
    if kevin>stuart:
        print("Kevin", kevin)
    elif stuart>kevin:
        print("Stuart", stuart )
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

