class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1=version1.split('.')
        n2=version2.split('.')
        if len(n1)<len(n2):
            for i in range(len(n2)-len(n1)):
                n1.append('0')
        else:
            for i in range(len(n1)-len(n2)):
                n2.append('0')
        for i in range(len(n1)):
            if int(n1[i])>int(n2[i]):
                return 1
            elif int(n2[i])>int(n1[i]):
                return -1
        return 0