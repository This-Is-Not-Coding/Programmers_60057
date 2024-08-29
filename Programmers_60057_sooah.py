def solution(s):
    data = s
    L = len(data)
    ans = 1000 # min length

    new_str = ''
    for length in range(1, L//2+1): # 문자열 길이 1개~N개일 때 결과값
        i = 0           # 현재 검사하는 문자의 인덱스
        now = data[i:length]   # 이전 문자
        cnt = 1         # 현재 검사하는 문자 개수
        while i + length <= L:
            i += length
            if now == data[i:i+length]:  # 현재 검사하는 문자가 이전 문자와 같으면, 숫자 +1
                cnt += 1
            else:               # 현재 검사하는 문자가 이전 문자와 다르면, new_str 숫자, 검사문자 추가 -> 숫자 0
                if cnt == 1:
                    new_str = ''.join([new_str, now])
                else:
                    new_str = ''.join([new_str, str(cnt), now])
                    cnt = 1
                now = data[i:i+length] # 이전 문자 갱신


        if cnt == 1:
            new_str = ''.join([new_str, now])
        else:
            new_str = ''.join([new_str, str(cnt), now])

        # new_str = ''.join([new_str, data[-length:]])
        ans = min(ans, len(new_str))        # 문자열 최소길이 갱신
        new_str = ''

    if ans == 1000:
        ans = 1

    return ans