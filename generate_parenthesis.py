def generateParenthesisBacktrack(n):

    results = []

    def backtrack(brackets, open_count, close_count):
        if len(brackets) == 2 * n:
            results.append(brackets)
            return

        if open_count < n:
            brackets += "("
            backtrack(brackets, open_count + 1, close_count)

        if close_count < n:
            brackets += ")"
            backtrack(brackets, open_count + 1, close_count)

    backtrack("", 0, 0)
    return results
