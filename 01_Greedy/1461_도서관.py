"""
날짜 <2023/03/03 (금)>
- 문제 링크: https://www.acmicpc.net/problem/1461
- 문제 요약
    세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성
    세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.
- 상상 코딩
    양과 음으로 끝에 있는 책들부터 M개씩 끊어서, 끝에있는 책들의 좌표를 모두 더하고, 2배한다.
    양과 음중 더 멀리있는 책의 좌표는 따로 가지고 있다가. 위에서 2배한거에서 빼면 정답
- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3

- 문제 분석

    - 알고리즘 유형 분석
        책의 위치를 양수와 음수로 나누어, M개의 책을 들고 가져다 둘 때, 최선의 선택을 해서 가져다 두어야 하므로 그리디 알고리즘.

    - 시간복잡도 분석
        주어진 N개의 책에 대해 양, 음을 나누어 정렬 -> O(NlogN)
        M개씩 건너 뛰며 책의 좌표 저장 -> O(N)
        전체 시간 복잡도는 정렬인 O(NlogN)

    - 리팩토링 방향성
        양수와 음수를 나누어 잘 진행. 따로 개선 방향이 보이지 않습니다.
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
book_cords = [*map(int,input().split())]
neg_cords = []; pos_cords = []
result=max_cord=0
for cord in book_cords:
    max_cord = max(max_cord, abs(cord))
    if cord > 0:
        pos_cords.append(cord)
    else:
        neg_cords.append(-cord)
pos_cords.sort(reverse=True)
neg_cords.sort(reverse=True)
for i in range(0,len(pos_cords),M):
    result += pos_cords[i]
for i in range(0,len(neg_cords),M):
    result += neg_cords[i]
print(2*result - max_cord)