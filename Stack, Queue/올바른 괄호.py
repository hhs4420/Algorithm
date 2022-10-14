def solution(s):
    answer = True
    print(s[len(s) - 1])
    result_a = 0
    result_b = 0
    
    result_False = 0
    
    if s[0] == ')' or s[len(s) - 1] == '(':
        result_False = 1
    else:
        for i in range(len(s)):
            if s[i] == '(':
                result_a += 1
            else:
                result_b += 1
            
            if result_b > result_a:
                result_False = 1
                break
            
            if i == len(s) - 1 and result_a != result_b:
                result_False = 1
    
    if result_False == 1:
        return False
    else:
        return True