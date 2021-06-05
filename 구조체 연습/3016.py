# 세종이는 정보과학 선생님인 JH를 도와주기 위해 정보과학 성적처리 프로그램을 만들기로 했다.
# JH 선생님은 특정 과목에서 1등한 학생이 다른 과목에서는 어떤 성적을 얻었는지 관심이 많다.
# 다음 조건을 만족하는 프로그램을 작성해 보자.

# 첫째 줄에 데이터의 개수 n (3<=n<=100)
# 둘째 줄부터 n+1줄에 학생 이름과 3과목 점수들이 공백으로 구분되어 입력된다. (입력 예시 참고)
# 단 이름의 길이는 최대 10바이트 이내이다

# 첫 번째 과목을 1등한 학생의 이름과 두 번째, 세 번째 과목의 석차를 공백으로 구분하여 출력한다.
# 단 첫 번째 과목의 1등은 1명이라고 가정한다.

def findRanking(name, arr, n, sid):
    cnt = 0
    rank = 0
    for i in range(n):
        if arr[i][0] == name:
            rank = i + 1
            for j in range(i - 1, -1, -1):
                if arr[j][sid] == arr[i][sid]:
                    if j == 0:
                        rank = 1
                        break;
                    else:
                        cnt = cnt + 1
                else:
                    rank = i - cnt + 1
                    break
            break
    
    return rank


n = int(input())
arr = []
for i in range(n):
    temp = input().split()
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    arr.append(temp)

sorted_first = sorted(arr, key=lambda score: score[1], reverse=True)
sorted_second = sorted(arr, key=lambda score: score[2], reverse=True)
sorted_third = sorted(arr, key=lambda score: score[3], reverse=True)
sorted_arr = [sorted_first, sorted_second, sorted_third]

print(sorted_arr[0][0][0], findRanking(sorted_arr[0][0][0], sorted_arr[1], n, 2), findRanking(sorted_arr[0][0][0], sorted_arr[2], n, 3))