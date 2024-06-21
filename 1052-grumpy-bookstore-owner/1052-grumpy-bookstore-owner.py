class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate the initial satisfied customers without using the technique
        total_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Calculate potential increase in satisfied customers when using the technique
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        for i in range(n):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    current_additional_satisfied -= customers[i - minutes]
            
            if i >= minutes - 1:
                max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        return total_satisfied + max_additional_satisfied
