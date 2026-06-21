class Solution:

    def hash_array_set(self, dp: dict[int, dict[int, bool]], i: str, j: str, val: bool):
        """
        Allows lookup in a hash array like an array in python
        """
        try:
            assert dp[i]
        except KeyError:
            dp[i] = {}

        try:
            assert dp[i][j]
        except KeyError:
            dp[i][j] = False

        dp[i][j] = val

    def hash_array_get(self, dp: dict[int, dict[int, bool]], i: str, j: str, val: bool):
        try:
            return dp[i][j]
        except KeyError:
            return False

    def print_dp(self, dp: dict[int, int]):
        for k in dp.keys():
            print(f"For {k}: {dp.get(k)}")

    def longestPalindrome(self, s: str) -> str:

        if len(s) < 1:
            return ''

        # Check for palindromes of all length and store their values in the DP table.
        # Recurrence pattern to store
        # dp[i][j] = True means string from i..j is a palindrome
        # dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1] is True)
        # This basically means a string is palindrome only if the internals of that string are also palindrome

        # We can make DP into a hashmap to avoid storing all the data
        # E.g dp[i][j] will be hash lookup rather than a list -> if exists True if not then false
        dp = {}
        longest_palindrome = ''

        # Setup the base case
        for i in range(len(s)):
            self.hash_array_set(dp, i, i, True)

        for str_len in range(len(s) + 1):
            for idx in range(len(s) - str_len):
                i, j = idx, idx + str_len
                is_pal = (s[i] == s[j]) and (str_len <= 3 or dp[i][j])
                if is_pal:
                    print(f"Found palindrom => {s[i:j+1]}")                    
                    longest_palindrome = s[i:j+1]
                self.hash_array_set(dp, i, j, is_pal)

        print(f"Longest Palindrome: {longest_palindrome}")
        return longest_palindrome

