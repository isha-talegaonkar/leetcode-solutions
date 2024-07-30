class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        taskHashmap = {}
        currentDay = 1
        
        for i in range(len(tasks)):
            if tasks[i] in taskHashmap and taskHashmap[tasks[i]] > currentDay:
                currentDay = taskHashmap[tasks[i]] 
                
            taskHashmap[tasks[i]] = currentDay + space + 1            
            currentDay += 1
                       
        return currentDay-1
        
        
            