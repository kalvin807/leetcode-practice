class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        seens = set()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            if not num[i] in seens:
                seens.add(num[i])
                j, k = i + 1, len(num) - 1
                while j < k:
                    sum = num[i] + num[j] + num[k]
                    if sum == target:
                        return sum
                    if abs(sum - target) < abs(result - target):
                        result = sum
                    # Tweak point by diff
                    if sum < target:
                        j += 1
                    elif sum > target:
                        k -= 1
        return result
