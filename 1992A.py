t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))

    for i in range(5):
        nums.sort()
        nums[0] += 1
        
    maxm = nums[0] * nums[1] * nums[2]

    print(maxm)
