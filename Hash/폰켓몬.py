def solution(nums):
    answer = 0
    answer_list = []
    l = len(nums) / 2
    for i in nums:
        if len(answer_list) == l:
            break
        else:
            if not i in answer_list:
                answer_list.append(i)
                answer += 1
            else:
                continue
        
    return answer