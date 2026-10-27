# minimum window substring :
from collections import Counter #haspmap freq
def min_win_substr(s :str ,t : str) -> str :
    if not s or not t or len(t)>len(s):
        return ""
    need = Counter(t)
    window = {}
    left = 0
    formed = 0
    required = len(need)
    min_len = float("inf")
    start = 0
    
    for right , ch in enumerate(s) :
        window[ch] = window.get(ch ,0) + 1
        if ch in need and window[ch] == need[ch] :
            formed +=1
        while formed == required :
            if right - left +1 < min_len :
                min_len = right - left +1
                start = left
            left_ch = s[left]
            window[left_ch] -=1
            
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -=1
            left +=1
    return "" if min_len == float("inf") else s[start : start + min_len]


print(min_win_substr("ADOBECODEBANC","ABC"))
print(min_win_substr("a","a")) 
#s = "ADOBECODEBANC" ,t = "ABC"
# op - "BANC"
# s = "a" ,t = "a"
#output : "a"
#1 <= s.length <= 10^5
#   <= t.length
#normalize upper case lowercase eng
# complexity : O(|S|+|t|)
