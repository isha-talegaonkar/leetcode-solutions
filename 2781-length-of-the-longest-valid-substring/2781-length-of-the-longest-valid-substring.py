class Solution:
    def longestValidSubstring(self, word, forbidden):
        forbidden_set, max_val, right = set(forbidden), 0, len(word)-1

        for left in range(len(word)-1,-1,-1):
            # print("left",left)
            for k in range(left,min(left+10,right+1)):
                # print("k: ", k)
                if word[left:k+1] in forbidden_set:
                    # print(word[left:k+1])
                    right = k-1
                    break 

            max_val = max(max_val,right-left+1)

        return max_val