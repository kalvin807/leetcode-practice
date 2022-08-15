import collections
import itertools

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        history = collections.defaultdict(list)
        
        for time, user, web in sorted(zip(timestamp, username, website)):
            history[user].append(web)
        
        hottest = 0
        pattern_cnt = collections.defaultdict(int)
        for user_hist in history.values():
            if not len(user_hist) >= 3:
                continue
            patterns = list(set(itertools.combinations(user_hist, 3)))
            for p in patterns:
                pattern_cnt[p] += 1
                hottest = max(hottest, pattern_cnt[p])

        hottest_p = [k for k, v in pattern_cnt.items() if v == hottest]
        return sorted(hottest_p)[0]
