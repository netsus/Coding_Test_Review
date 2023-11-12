"""
날짜 <2023/11/13 (월)>
- 문제 링크: https://www.acmicpc.net/problem/1744
- 문제 요약
    주어진 수열중에 두 수를 묶으면 곱해진다. 이렇게 수를 묶거나 묶지 않아서. 수열의 합이 최대가 되게 출력하세요.

- 상상 코딩
    양수 리스트에 대해 내림차순해서 2개씩 묶어 곱합니다. 홀수개인 경우 마지막 남은 가장 작은 원소를 빼고 2개씩 짝지어 곱해줍니다.
    0이 있는지 확인합니다.
    음수 리스트가 짝수개인 경우 오름차순에서 2개씩 묶어 곱해줍니다.
    음수 리스트가 홀수 개인 경우 오름차순해서 2개씩 묶어 곱하고, 마지막 남은 원소1개를 저장해줍니다. -> 0이 있으면 곱해서 없애 버립니다. 0이 없으면 놔두기
    그렇게 처리해서 모두 더해주면 됩니다.

- 체감 난이도 (1:쉬움 ~ 5:매우 어려움)
    3.5
- 문제 분석

    - 알고리즘 유형 분석

    - 시간복잡도 분석

    - 리팩토링 방향성
    
"""
## 파일로 예제 입력 읽기
import sys
sys.stdin = open("input.txt",'r')
## 풀이1 이후에 복습하고 다시 풀어본 것
import sys
input = sys.stdin.readline

N = int(input())
positive_arr=[];negative_arr=[];zero_exist=False;num_one=0
for _ in range(N):
    num = int(input())
    if num==1:
        num_one+=1
    elif num > 1:
        positive_arr.append(num)
    else:
        negative_arr.append(num)
positive_arr.sort(reverse=True)
negative_arr.sort()
multiple = lambda l: l[0]*l[1] if len(l)==2 else l[0]
pos_mlt_arr = [multiple(positive_arr[i:i+2]) for i in range(0,len(positive_arr),2)]
neg_mlt_arr = [multiple(negative_arr[i:i+2]) for i in range(0,len(negative_arr),2)]
result = sum(neg_mlt_arr)+sum(pos_mlt_arr)
result += num_one
print(result)



# ## 풀이1
# import sys
# input = sys.stdin.readline

# N = int(input())
# positive_arr=[];negative_arr=[];zero_exist=False;num_one=0
# for _ in range(N):
#     num = int(input())
#     if num==1:
#         num_one+=1
#     elif num > 1:
#         positive_arr.append(num)
#     elif num < 0:
#         negative_arr.append(-num)
#     else:
#         zero_exist=True
# positive_arr.sort(reverse=True)
# negative_arr.sort(reverse=True)
# multiple = lambda l: l[0]*l[1] if len(l)==2 else l[0]
# pos_mlt_arr = [multiple(positive_arr[i:i+2]) for i in range(0,len(positive_arr),2)]
# neg_mlt_arr = [multiple(negative_arr[i:i+2]) for i in range(0,len(negative_arr),2)]
# if len(negative_arr)%2==1:
#     if zero_exist:
#         neg_mlt_arr[-1] = 0
#     else:
#         neg_mlt_arr[-1] = -neg_mlt_arr[-1]
# result = sum(neg_mlt_arr)+sum(pos_mlt_arr)
# result += num_one
# print(result)




