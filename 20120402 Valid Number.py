'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip();
        # dfa status 
        err = -1 # error
        srt = 0  # start
        sgd = 1  # integer part sign 
        did = 2  # integer part number
        ddp = 3  # xx. (there are some numbers before '.')
        dnp = 3  # .
        dii = 5  # decimal part number
        exe = 6  # e
        sge = 7  # exp part sign
        die = 8  # exp part number
        end = 9 # end
        # construct a dfa
        dfa = [[err] * 128 for i in range(9)]
        dfa[srt][ord('+')] = dfa[srt][ord('-')] = sgd
        dfa[srt][ord('.')] = dfa[sgd][ord('.')] = dnp
        dfa[did][ord('.')] = ddp
        dfa[did][ord('e')] = dfa[ddp][ord('e')] = dfa[dii][ord('e')] = exe
        dfa[exe][ord('+')] = dfa[exe][ord('-')] = sge
        dfa[dii][0] = dfa[ddp][0] = dfa[did][0] = dfa[die][0] = end
        for i in range(10):
            t =  ord('0') + i
            dfa[srt][t] = dfa[sgd][t] = dfa[did][t] = did
            dfa[ddp][t] = dfa[dnp][t] = dfa[dii][t] = dii
            dfa[exe][t] = dfa[sge][t] = dfa[die][t] = die
        # run dfa with s
        s = s.strip()
        status = srt
        for c in s:
            status = dfa[status][ord(c)]
            #print status
            if (status == err):
                return False
        return True if dfa[status][0] == end else False
        
        
        