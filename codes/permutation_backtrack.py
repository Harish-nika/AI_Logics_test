#permutate combinations
#backtracking
def combos(s : str) -> list[str] :
    result =[]
    path = []
    used = [False] * len(s)
    def backtracking():
        if len(path) == len(s) :
            result.append("".join(path))
            return
        for i in range(len(s)) :
            if used[i] :
                continue
            #we are going to choose
            used[i] = True
            path.append(s[i])
            #then we explore
            backtracking()
            #remove / undo the choice
            path.pop()
            used[i] = False
    backtracking()
    return result

print(combos("abc"))
print(combos("ab"))
# permutation of str 
#s = "abc"
#op = "all possible combos"
#example : "ab" then "ab" ,"ba"
#all lowercase 
# s.length >=1 , <=8 , complexity : 0(n*n!)