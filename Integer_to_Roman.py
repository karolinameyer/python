class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        wyraz = ""
        x = ["I", "V", "X", "L", "C", "D", "M"]
        for i in range(len(num)):
            l = num[-1-i]
            if l in "123":
                wyraz += int(l) * x[2*i]
            elif l == "4":
                wyraz += x[2*i+1] + x[2*i]
            elif l == "5":
                wyraz += x[2*i+1]
            elif l in "678":
                wyraz += (int(l)-5) * x[2*i] + x[2*i+1] 
            elif l == "9":
                wyraz += x[2*i+2] + x[2*i]
            elif l == "0":
                continue
        return wyraz[::-1]
