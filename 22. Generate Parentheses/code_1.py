class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        open_count = 0
        close_count = 0
        res = []

        def backtrack(pair, open_count, close_count):
            if open_count + close_count == 2 * n:
                return res.append(pair)

            if open_count > close_count:
                backtrack(pair+")", open_count, close_count+1)
            
            if open_count > close_count and open_count < n:
                backtrack(pair+"(", open_count+1, close_count)

            if open_count == close_count:
                backtrack(pair+"(", open_count+1, close_count)

        backtrack("", 0, 0)
        return res

        # n = 3
        # (  |  1 0
        #   ()  |  1 1
        #      ()(  |  2 1
        #           ()()  |  2 2
        #                 ()()(  |  3 2
        #                        ()()()  |  3 3
        #           ()((  |  3 1
        #                 ()(()  |  3 2
        #                        ()(())  |  3 3
        #   ((  |  2 0
        #      (()  |  2 1
        #           (())  |  2 2
        #                 (())(  |  3 2
        #                        (())()  |  3 3
        #           (()(  |  3 1
        #                 (()()  |  3 2
        #                        (()())  |  3 3
        #      (((  |  3 0
        #           ((()  |  3 1
        #                 ((())  |  3 2
        #                        ((()))  |  3 3
