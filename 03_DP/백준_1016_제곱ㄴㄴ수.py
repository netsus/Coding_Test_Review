"""
날짜 <2023/05/06 (목)>
- 문제 링크: 
- 문제 요약

- 상상 코딩

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)

- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##

m,M = map(int,input().split())                    # 최소, 최대
division = [1] * (M-m+1)                          # 제곱수로 나누어 떨어지는 경우
squares = [i**2 for i in range(2, int(M**0.5)+1)] # 제곱수
result = M - m + 1                                # m이상, M이하 모든 수의 개수
for sq in squares:
    for z_su in range( (((m-1)//sq)+1)*sq, M+1, sq):  # 제곱수의 배수들
        if division[z_su-m]: # 제곱수의 배수로 나누어 떨어지는 경우
            division[z_su-m] = 0
            result -= 1
print(result)
            