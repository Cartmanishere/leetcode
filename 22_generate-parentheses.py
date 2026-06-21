class Solution:
    def __init__(self):
        self.dp = {0: [""], 1: ["()"]}  # Base case

    # Chatgpt explanation -
    # https://chatgpt.com/c/688dab0a-4af0-8006-9eee-7bd5b2ae67e7
    def generateParenthesis(self, n: int) -> list[str]:
        try:
            return self.dp[n]
        except KeyError:
            print(f"dp[{n}] not available - calculating")

        results = []
        for i in range(n):

            mid_idx = i
            right_idx = n - 1 - i

            lefts = [
                f"({s})" for s in self.generateParenthesis(mid_idx)
            ]
            rights = self.generateParenthesis(right_idx)

            for l in lefts:
                for r in rights:
                    results.append(f"{l}{r}")

        self.dp[n] = results[::-1]

        return results
