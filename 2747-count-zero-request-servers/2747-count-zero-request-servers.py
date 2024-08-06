class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        result = []
        queries = [(i, q - x, q) for i, q in enumerate(queries)]

        queries.sort(key = lambda x: x[1])

        empty = [n] * len(queries)
        logs.sort(key=lambda x: x[1])
        logs += [[0, float("inf")]]

        l, r = 0, 0
        window = defaultdict(int)

        for i, start, end in queries:
            while logs[r][1] <= end:
                window[logs[r][0]] = window[logs[r][0]] + 1
                r += 1
            while logs[l][1] < start:
                window[logs[l][0]] -= 1
                if window[logs[l][0]] == 0: 
                    del window[logs[l][0]]

                l += 1

            empty[i] -= len(window)

        return empty