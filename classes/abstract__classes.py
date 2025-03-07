# Abstract class: 
#   => A class that cannot be instantiated on its own; Meant to be subclassed.
#   => They contain abstract methods, which are declared but have no implementation.

# Abstract classes benefits:
#       1.Prevents instantiation of the class itself
#       2.Requires children to use inherited abstract methods

class Solution(object):
    def mergeAlternately(self, word1, word2):
        # Convert strings to lists
        list1 = list(word1)
        list2 = list(word2)
        
        # Initialize an empty list to store the merged word
        merged_word = []
        
        # Merge words alternately
        while list1 or list2:
            if list1:
                merged_word.append(list1.pop(0))
            if list2:
                merged_word.append(list2.pop(0))
        
        # Join the list back into a string
        return ''.join(merged_word)

# Example usage
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"


