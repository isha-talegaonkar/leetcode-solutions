class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = defaultdict(int)
        
        for frm, to, amt in transactions:
            balances[frm] += amt
            balances[to] -= amt
        
        balance_list = [amt for amt in balances.values() if amt]
        balanceLength = len(balance_list)
        
        def dfs(current):
            while current < balanceLength and not balance_list[current]:
                current += 1
            if current == balanceLength:
                return 0
            
            cost = float("inf")
            for nxt in range(current+1, balanceLength):
                if balance_list[nxt] * balance_list[current] < 0:
                    balance_list[nxt] += balance_list[current]
                    cost = min(cost, 1 + dfs(current + 1))
                    balance_list[nxt] -= balance_list[current]
            return cost
                
            
        return dfs(0)
        