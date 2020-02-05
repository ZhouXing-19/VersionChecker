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