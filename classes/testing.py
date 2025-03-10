# # class Solution(object):
# #     def twoSum(self, nums, target):
# #         # """
# #         # :type nums: List[int]
# #         # :type target: int
# #         # :rtype: List[int]
# #         # """
        
# #         num_dict = {}
        
# #         for i, num in enumerate(nums):
# #             complement = target - num
            
# #             if complement in num_dict:
# #                 return [num_dict[complement], i]

# #             num_dict[num] = i
        
# #         return []

# # solution = Solution()
# # nums = [2, 7, 11, 15]
# # target = 9
# # print(solution.twoSum(nums, target))  # Output: [0, 1]


# class Banking_System:

#     def __init__(self, Account_Number, Balance):
#         self.Account_Number = Account_Number
#         self.Balance = Balance

#         def deposit(self, amount):
#             self.Balance += amount
#             print(f"Deposited {amount}. New balance: {self.Balance}")

#         def withdraw(self, amount):
#             if self.Balance >= amount:
#                 self.Balance -= amount
#                 print(f"Withdrew {amount}. New balance: {self.Balance}")
#             else:
#                 print("Insufficient funds")
        
#         def check_balance(self):
#             print(f"Current balance: {self.Balance}")

#         def transfer(self, amount, target_account):
#             if self.balance >= amount:
#                 self.balance -= amount
#                 target_account.deposit(amount)
#                 print(f"Transferred {amount} to account {target_account.Account_Number}. New balance: {self.Balance}")
#             else:
#                 print("Insufficient funds")


# Account1 = ("123456789", 1000)
# Account2 = ("987654321", 500)

# Account1()


# def primer(numbers):
#     for number in numbers:
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i) == 0:
#                     break
#             else:
#                 print(number)


# print(primer([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) - round((alice_candies + bob_candies + carol_candies) / 3) * 3 

num = (alice_candies + bob_candies + carol_candies) / 3


print(to_smash)
print(round(num, 2))

# Check your answer

def default_function():
    print("This is the default function.")

def main_function(func=default_function):
    func()

# Calling main_function without specifying a function will use default_function
main_function()  # Output: This is the default function.

# You can also pass a different function
def another_function():
    print("This is another function.")

main_function(another_function)  # Output: This is another function.


print(True or True and False)

def sign(num):
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    elif num == 0:
        print(0)
# Check your answer
sign(5)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
    print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')