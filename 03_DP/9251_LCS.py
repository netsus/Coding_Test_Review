"""
날짜 <2023/03/06 (월)>
- 문제 링크: https://www.acmicpc.net/problem/9251
- 문제 요약
    LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
    예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
    첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
    첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
    
- 상상 코딩
    첫번째 문자열을 행으로, 두번째 문자열을 열로해서 2차원 dp table을 통해 최장 공통 수열(LCS)를 찾는다.
    정답은 가장 오른쪽 아래 마지막 행,열에 작성한다.
    FP: dp table을 어떻게 채워나갈 것인가? 모두 채울것인가? 모두 채워야 하는가? 모두 채워야 한다.
    첫 행과, 첫 열을 채운다.
    다음부터는 왼쪽과 위중에 최대값을 채우는데, 현재 단어와 위의 단어가 같다면 +1로 채운다.
    그렇게 끝까지 채워서 마지막 행,열을 출력

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    4(아이디어가 어려움)

- 문제 분석

    - 알고리즘 유형 분석
        두 개의 문자열을 받아, 2차원 dp 테이블을 채우는 문제이므로, DP 유형입니다.

    - 시간복잡도 분석
        두 개의 문자열 길이를 각각 N, M 이라고 했을 때, 길이만큼 연산을 하므로, 전체 시간복잡도는 O(N*M)입니다.

    - 리팩토링 방향성
        첫행과 첫열을 따로 만들어주었는데, 1 based index를 사용하여 같은 규칙을 한번에 적용시킬 수 있습니다.
        또한, dp 테이블에서 각 행과 열의 의미는 거기까지의 스트링에 대한 최장 공통 수열의 길이값이 들어가기 때문에 다음 문자에서 같은 경우 mat[r-1][c-1]+1 만 해주면 됩니다.
        그 외에는 왼쪽과 위 중에 최대값을 가져오면 됩니다.
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
#### 첫번쨰 풀이
import sys
input = sys.stdin.readline
r_str = input().rstrip()
c_str = input().rstrip()
R,C = map(len,(r_str,c_str))
mat = [[0 for _ in range(C)] for _ in range(R)]
mat[0][0] = int(r_str[0]==c_str[0])
r_frst,c_frst = r_str[0],c_str[0]
c_1 = c_str.find(r_frst)
r_1 = r_str.find(c_frst)
mat[0] = [1 if c_1 != -1 and c_1<=i else 0 for i in range(C)]
for i in range(R):
    mat[i][0] = 1 if r_1 != -1 and r_1<=i else 0
for r in range(1,R):
    for c in range(1,C):
        if r_str[r]==c_str[c]:
            mat[r][c] = min(mat[r-1][c-1],mat[r-1][c],mat[r][c-1]) + 1
        else:
            mat[r][c] = max(mat[r-1][c],mat[r][c-1])
print(mat[-1][-1])
        
#### 리팩토링 풀이
import sys
input = sys.stdin.readline
r_str = input().rstrip()
c_str = input().rstrip()
R,C = map(len,(r_str,c_str))
mat = [[0 for _ in range(C+1)] for _ in range(R+1)]
for r in range(1,R+1):
    for c in range(1,C+1):
        if r_str[r-1]==c_str[c-1]:
            mat[r][c] = mat[r-1][c-1] + 1
        else:
            mat[r][c] = max(mat[r][c-1],mat[r-1][c])
print(mat[-1][-1])