#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            # Stop at first match
            return [lookup[complement], i]
        lookup[num] = i
    return None
# Solution in O(n)
# Tests
print("RESULTS 01")
print(twoSum([2,3,4,2,7],10))
print(twoSum([2,5,7,9,1],10))
# Test empty result or no match - even though not asked
print(twoSum([],10))
print(twoSum([1,2,3,4,5],100))
print("===========")
#Time and space complexity:

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(strs):
    if not strs: return None
    prefix = strs[0]

    for s in strs[1:]:
        # Shorten the prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return None
    return prefix

# Tests
print("\n")
print("RESULTS 02")
print(findMostCommonPrefix(["flower","flow","flight"]))
print(findMostCommonPrefix(["chocolate","cyan","chinchilla"]))
print(findMostCommonPrefix(["lalala","lalalalo","lalalaloli"]))
print("===========")

#Time and space complexity:

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def threeSum(nums):
    n = len(nums)
    for i in range(n):
        seen = {}
        target = -nums[i]
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                # Found triple: nums[i] + nums[j] + nums[k] == 0
                return [i, seen[complement], j]
            seen[nums[j]] = j
    return None 

print("\n")
print("RESULTS 03")
print(threeSum([1, 2, -2, -1, 3]))
print(threeSum([0, 1, 3, -2, -2, 4]))
print("===========")

#Time and space complexity:

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

printList(head)

def reverseList(head):
    prev = None
    current = head
    while current:
        nxt = current.next   # Save next node
        current.next = prev  # Reverse link
        prev = current       # Move prev forward
        current = nxt        # Move current forward
    return prev  # New head

#Time and space complexity:
print("\n")
print("RESULTS 04")
printList(reverseList(head))

head = Node(9)
middle_1 = Node(8)
middle_2 = Node(7)
middle_3 = Node(6)
tail = Node(5)

head.next = middle_1
middle_1.next = middle_2
middle_2.next = middle_3
middle_3.next = tail
tail.next = None
printList(reverseList(head))
print("===========")



