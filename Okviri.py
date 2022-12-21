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

    print(answer,end ='')
    
if __name__ == '__main__':
    main()

