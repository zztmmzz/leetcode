class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        cache = dict()
        res = 0
        for r in range(len(s)):
            char_r = s[r]
            if cache.get(char_r) is None:
                cache[char_r] = True
            else: 
                while l < r:
                    char_l = s[l]
                    cache[char_l] = None
                    l += 1

                    if char_l == char_r:
                        cache[char_r] = True
                        break

            res = max(res, r - l + 1)
        return res

sol = Solution().lengthOfLongestSubstring("pwwkew")
print(sol)
