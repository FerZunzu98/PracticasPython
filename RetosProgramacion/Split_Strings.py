def solution(string):

    if not(string): return []

    result = []

    i = 0
    while i < len(string):
        result.append(string[i:i+2])
        i+=2

    if len(result[-1])  == 1: result[-1] = result[-1] +"_" 

    return result

print(solution(""))