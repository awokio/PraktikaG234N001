#№1
n = 100
F = [0] * (n + 1)
F[0] = 1
F[1] = F[0]
F[2] = F[1] + F[0]
for i in range(3, n + 1):
    F[i] = F[i - 3] + F[i - 1]
print(F[i])



#№2
def min_cost_jump(n, Price):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = Price[1]
    dp[2] = Price[2]

    for i in range(3, n):
        dp[i] = min(dp[i-1] + Price[i], dp[i-3] + Price[i])
    return dp[i]

n = 10
Price = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



min_cost = min_cost_jump(n, Price)
print(f"Минимальная стоимость маршрута кузнечика из точки 0 в точку {n} : {min_cost}")