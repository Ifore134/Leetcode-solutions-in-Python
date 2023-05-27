class Solution:
    def addBinary(self, a: str, b: str) -> str:
        fir = a[::-1]
        sec= b[::-1]

        val=0
        for i in range(len(fir)):
            if fir[i]=="1":
                val+=2**i
        val2=0
        for i in range(len(sec)):
            if sec[i]=="1":
                val2+=2**i
        ans = val+val2

        answer=""
        while ans>0:
            if ans%2>0:
                answer+="1"
            else:
                answer+="0"
            ans=ans//2
        if answer=="":
            return "0"
        return answer[::-1]
