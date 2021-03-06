# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
#
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# ex 입력 18, 출력 4

# ================================================

# 봉지무게 입력 받기
n = int(input())

count5 = n // 5     # 5kg로 배달할 수 있는 봉지 수
count3 = 0          # 3kg 봉지의 수

n = n % 5       #5kg로 배달하고 남은 설탕의 수
answer = -1     #정확하게 나눌 수 없다면 -1

while n >= 0:
    if n % 3 == 0:
        count3 = n // 3
        answer = count5 + count3
        break

    if count5 == 0:
        break

    count5 -= -1 # 5kg 봉지수 하나 감소
    n += 5 # 3kg 봉지로 나누기 위해

print(answer)



