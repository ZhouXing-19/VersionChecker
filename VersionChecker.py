"""
@author: Zhou Xing
@software: PyCharm
@file: VersionChecker.py
@time: 2020-Jan-30 08:38
"""

'''
write a web service that takes in two
strings and returns a string indicating if the first string is before, after, or equal to the second string. Where "before", "after" and "equal" are based interpretation as software version numbers.
Examples:
1.0.0
 is "before" 1.0.1
2.0
 is "after" 1.0.0
You
 can use any language. When completed, please upload to a public repository, such as GitHub, and provide us with the link.

'''

class Solution:
    def VersionChecker(self,version1,version2):
        if not version1 or not version2:
            return False
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        # Turn parts into integers, if this position does not exist, use 0
        for i in range(0,max(len(v1_list),len(v2_list))):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            if v1 > v2:
                return version1 + ' is \"after\" '+ version2
            elif v1 < v2:
                return version1 + ' is \"before\" '+ version2
        return version1 + ' is \"the same as\" '+ version2

s = Solution()
version1 = "2.0"
version2 = "1.0.1"
print(s.VersionChecker(version1,version2))
