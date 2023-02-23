# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None


class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def createBST(arr):
    #find middle of the list
    mid = len(arr)//2
    root = Node(arr[mid])

    #less than the middle of the list
    root.left = createBST(arr[:mid])

    #greater than the middle of the list
    root.right = createBST(arr[mid+1:])
    return root


class Solution(object):
    def two_sum(self, arr, targ):
        look_for = {}
        for i, num in enumerate(arr):
            sub_num = targ-num
            print(i, num)
            if sub_num in look_for:
                return arr[look_for[sub_num]],arr[i]
            look_for[num] = i

    def isPalindrome(self, x):
            to_str= str(x)
            rev_word=''
            for i in to_str:
                rev_word = i + rev_word
            if rev_word == to_str:
                return True
            return False

    def romanToInt(self, s):
        rom_tab ={'I':1,'V':5,'X':10,'L':50,'D':100,'C':500,'M':1000}
        result = 0
        for i,num in enumerate(s):
            if (i+1) == len(s) or rom_tab[num] >= rom_tab[s[i+1]]:
                result += rom_tab[num]
            else:
                result -= rom_tab[num]

        return result

    def longestCommonPrefix(self, x,y):
        while x != y:
            if x > y:
                x = x-y
            elif x < y:
                y = y-x

        print(x, y)

    def insPos(self,arr,tar):
        for i in range(len(arr)):
            if arr[i]==tar:
                return i
            elif arr[i]>tar:
                return i

        return len(arr)

    def tree_trav(self,root):
        res=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            res.append(root.val)
    def searchInsert(self,A,target):
        high = len(A)-1
        low = 0
        while(low<=high):
            mid = (high+low)//2
            if A[mid]==target :
                return mid
            elif A[mid]<target:
                high=mid-1
            else:
                low =mid+1

        return low
    def largeNum(self,arr):
        salesMap = {}
        for i in arr:
            if i in salesMap:
                salesMap[i] += 1
            else:
                salesMap[i] = 1
        return max(salesMap.keys())

    def editString(self,s):
        charArray = [char for char in s]
        for j in range(len(charArray)):
            if charArray[j] == "":
                charArray[j] = ""
        newS = "".join(charArray)

    def lonelyinteger(self,a):
        countMap= {}
        for i in a:
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1

        for i in countMap:
            if countMap[i] == 1:
                return i
    def diagonalDifference(self,arr):
        left = 0
        right = 0

        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i==j:
                    left += arr[i][j]
                    print(left)
                if i == len(arr) - j - 1:
                    right += arr[i][j]
                    print(right)

        print(left,right)

        return abs(left-right)

    def countingSort(self,arr):
        freqArr = [0]*100
        for i in arr:
            freqArr[i] +=1
        return freqArr

    def findZigZagSequence(self,a, n):
        a.sort()
        mid = int((n + 1) / 2)
        a[mid], a[n - 1] = a[n - 1], a[mid]
        print(a[mid])
        st = mid - 1
        ed = n - 1
        while (st <= ed):
            a[st], a[ed] = a[ed], a[st]
            ed = ed - 1

        for i in range(n):
            if i == n - 1:
                print(a[i])
            else:
                print(a[i], end=' ')
        return
    def towerBreakers(self,n, m):
        if m == 1:
            return 2
        elif n % 2 == 0:
            return 1
        else:
            return 2

    def caesarCipher(self,s, k):
        lowerAlphabet = list("abcdefghijklmnopqrstuvwxyz")
        upperAlphabet = list("abcdefghijklmnopqrstuvwxyz".upper())

        k = k % len(lowerAlphabet)
        lowerTarget = lowerAlphabet[k:] + lowerAlphabet[:k]
        upperTarget = upperAlphabet[k:] + upperAlphabet[:k]
        lowerTranslation = dict(zip(lowerAlphabet, lowerTarget))
        upperTranslation =  dict(zip(upperAlphabet, upperTarget))
        result = ""
        for c in s:
            if c in lowerTranslation:
                result += lowerTranslation[c]
            elif c in upperTranslation:
                result += upperTranslation[c]
            else:
                result += c

        return result

print(Solution().caesarCipher("middle-Outz",2))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
