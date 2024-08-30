def solution(s):
    data = s
    L = len(data)
    ans = 1000      # min length

    new_str = ''    # 압축된 문자열
    for length in range(1, L//2+1): # 문자열 길이 1개~N개일 때 결과값 (단, L==1이면 진행x)
        i = 0                   # 현재 검사하는 문자의 인덱스
        now = data[i:length]    # 반복문자
        cnt = 1                 # 반복 수
        while i + length <= L:
            i += length
            if now == data[i:i+length]:     # 반복문자(now)와 현재 검사하는 문자(data)가 같으면, 반복수+1
                cnt += 1
            else:                           # 반복문자(now)와 현재 검사하는 문자(data)가 다르면,
                if cnt == 1:
                    new_str = ''.join([new_str, now])           # 압축된 문자열에 '반복문자' 추가
                else:
                    new_str = ''.join([new_str, str(cnt), now]) # 압축된 문자열에 '반복수' '반복문자' 추가
                    cnt = 1                                     # 반복 수 초기화
                now = data[i:i+length]      # 반복문자 갱신

        # 검사 종료 후, data의 뒤에서 length 길이만큼은 검사하지 않았으므로, 압축된 문자열에 추가
        if cnt == 1:
            new_str = ''.join([new_str, now])
        else:
            new_str = ''.join([new_str, str(cnt), now])

        ans = min(ans, len(new_str))        # 압축된 문자열을 최소길이로 갱신
        new_str = ''                        # 압축된 문자열 초기화

    if ans == 1000: # 문자열 길이가 1일 때
        ans = 1

    return ans