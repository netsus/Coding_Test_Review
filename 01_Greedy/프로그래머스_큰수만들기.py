"""
날짜 <2023/03/03 (금)>
- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
- 문제 요약
    어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
    number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
    k는 1 이상 number의 자릿수 미만인 자연수입니다.
    number	k	return
    "1924"	2	"94"

- 상상 코딩
    K를 tmp_k로 복사
    number의 첫 수를 stack에 넣고, tmp_k -= 1
    number를 n으로 반복 (for)
        stack이 존재하고 tmp_k가 0이 아니며, stack의 마지막 수보다 n이 더 큰 동안 stack pop, tmp_k-=1
    최종 출력은 stack에 대해, 앞에서 len(number)-K개 숫자 출력
    (이렇게 하는 이유는 같은 숫자가 여러개인 경우 stack에 의해 제거가 안되기 때문입니다.)

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        주어진 순간에 최적의 선택(전체 숫자가 커지도록 숫자를 빼는 것)을 해야 하므로, 그리디 입니다.
        맨 앞자리수가 최대가 되도록 수를 제거할 때, 스택을 사용합니다.

    - 시간복잡도 분석
        number의 개수가 N일 때, for문으로 N을 반복하며 내부에서 stack을 while문으로 돕니다.
        최악의 경우, 모든 수가 스택에 들어간다면 결국 stack을 처리하는 while문 역시 O(N)이므로,
        for문의 시간복잡도는 O(N^2)입니다.
        그 아래, join은 최악의 경우 주어진 모든 숫자가 포함될 때, O(N)입니다.

    - 리팩토링 방향성
        while문이 조금 복잡한 것이 걸립니다. 하지만 코드가 충분히 간결하고, 시간복잡도도 더 줄일 방향성이 보이지 않습니다. 
    
"""
number,k="1924",2 # "94"
number,k = "4177252841",4	# "775841"
number,k = "5413221",3	# "5432"

def solution(number,k):
    stack = [number[0]]
    tmp_k = k
    for n in number[1:]:
        while stack and tmp_k != 0 and stack[-1] < n:
            stack.pop()
            tmp_k -= 1
        stack.append(n)
    answer = "".join(stack[:len(number)-k])
    return answer

print(solution(number,k))


## 기존 풀이 -> 틀림 
def solution(number, k):
    stack=[]
    for n in number:
        while stack and k and stack[-1] < n:
            stack.pop()
            k-=1
        stack.append(n)
    if k:
        return number[:-k]
    else:
        return "".join(stack)
print(solution(number,k))