text = input("")
# #.A.#.B.*.C.*.D.#
def main():
    answer = ''
    for i in range(5):
        for j in range(len(text)):
            track = j +1
            if track % 3 != 0 or j == 0:
                if i == 0 or i == 4:
                    answer += '..#.'
                    if len(text)-1 == j:
                        answer += '.\n'
                elif i == 1 or i == 3:
                    answer += '.#.#' 
                    if len(text)-1 == j:
                        answer += '.\n'
                elif i == 2:
                    if track % 2 == 0 and (track -1) % 3 == 0:
                        answer += f'.{text[j]}.'
                    else:
                        answer += f'#.{text[j]}.'
                    if len(text)-1 == j:
                        answer += '#\n'  
            elif track % 3 == 0:
                if i == 0 or i == 4:
                    answer += '..*.'
                    if len(text)-1 == j:
                        answer += '.\n'
                elif i == 1 or i == 3:
                    answer += '.*.*' 
                    if len(text)-1 == j:
                        answer += '.\n'
                elif i == 2:
                    answer += f'*.{text[j]}.'
                    if len(text)-1 == j:
                        answer += '*\n' 
                    elif len(text) > j:
                        answer += '*'
    print(answer,end ='')







if __name__ == '__main__':
    main()

