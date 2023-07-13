"""
날짜 <2023/06/08 (목)>
- 문제 링크: https://www.acmicpc.net/problem/1068
- 문제 요약
    트리가 주어지고, 떼어넬 노드 번호가 주어졌을 때 → 남은 트리에서 리프노드의 개수 출력

- 상상 코딩

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)

- 문제 분석

    - 알고리즘 유형 분석
        트리 구조 생성 -> 이중 리스트
        DFS 순회

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
##
import sys
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N)]
root = answer =  0
for node,parent in enumerate(map(int,input().split())):
    if parent == -1:
        root = node
        continue
    tree[parent].append(node)
trg=int(input())
print(tree)
def dfs(node):
    global answer
    if node==trg:
        return
    else:
        if not tree[node]:
            answer += 1
        elif len(tree[node])==1 and tree[node][0]==trg:
            answer += 1
    for node in tree[node]:
        dfs(node)
dfs(root)
print(answer)




