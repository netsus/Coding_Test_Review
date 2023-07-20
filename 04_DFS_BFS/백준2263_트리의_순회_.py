"""
날짜 <2023/07/20 (목)>
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
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

inorder_idx = [0] * (n+1)
for i in range(n):
    inorder_idx[inorder[i]] = i # 각 노드가 인덱스, 값은 해당 노드의 inorder 순서

def preorder(inStart, inEnd, postStart, postEnd):
    # 루트 -> 왼쪽 -> 오른쪽
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd] # 루트 노드

    leftTreeNodeNum = inorder_idx[root] - inStart # 왼쪽 서브트리 노드 개수
    rightTreeNodeNum = inEnd - inorder_idx[root] # 오른쪽 서브트리 노드 개수

    print(root, end=" ")
    preorder(inStart, inStart+leftTreeNodeNum-1, postStart, postStart+leftTreeNodeNum-1) # 왼쪽 서브트리
    preorder(inEnd-rightTreeNodeNum+1, inEnd, postEnd-rightTreeNodeNum, postEnd-1) # 오른쪽 서브트리

preorder(0, n-1, 0, n-1)
