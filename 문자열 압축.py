def solution(s):
    length = len(s)

    if length > 1:
        wordLengths = []
        for sp in range(1, length//2+1):  # 설명 2
            w = s[:sp]  # 압축할 문자
            idx = sp  # 비교 시작 위치
            cnt = 1  # 문자 중복 횟수
            word = ''  # 최종 압축 문자
            last = length - length % sp  # 단위 문자로 비교할 수 있는 단어 수

            while idx < last:
                if w == s[idx: idx+sp]:  # 설명 3
                    cnt += 1
                    if idx == last - sp:  # 설명 5
                        word += f'{cnt}{w}'
                else:  # 설명 4
                    if cnt == 1:
                        word += w
                    else:
                        word += f'{cnt}{w}'
                    w = s[idx: idx+sp]
                    cnt = 1
                    if idx == last - sp:  # 설명 5
                        word += w
                idx += sp

            # 설명 6
            word += s[idx:]
            wordLengths.append(len(word))

        answer = min(wordLengths)  # 설명 7

    else:  # 설명 1
        return 1

    return answer