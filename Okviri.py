text = input("")
answer = ''
# #.A.#.B.*.C.*.D.#
for i in range(5):
    for j in range(1,len(text)):
            if i == 0 or i == 4:
                answer += '.'
                answer += '.#.'
                if len(text) == 1:
                    answer += '.'
                print(answer,end = '')
            elif i == 1 or i == 3:
                answer += '.'
                answer += '#.#'
                if j == len(text)-1:
                    answer += '.'
                print(answer,end = '')
            elif i == 2:
                answer = f'#.{text[j]}.'
                if len(text) == 1:
                    answer += '#'
                print(answer,end = '')

    print("")
    answer = ''



