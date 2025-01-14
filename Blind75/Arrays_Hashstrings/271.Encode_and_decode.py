class Solution:
    def encode(self, strs: list[str]) ->str:
        array = []
        for word in strs:
            if word == "":
                array.append("")
                array.append(".")
                continue
            for char in word:
                array.append(str(ord(char)))
                array.append("-")
            array.append(".")
        # print(array)
        return ''.join(array)
    
    def decode (self, s:str) -> list[str]:
        if len(s) == 1:
            return [""]
        result = []
        
        a = []
        array = s.split('.')
        for word in array:
            if word == "":
                continue
            print(word)
            holder = word.split('-')
            for char in holder:
                if char!= "":
                    a.append(chr(int(char)))

            result.append(''.join(a))
            a.clear()
        return result

Solution = Solution()
code = Solution.encode(["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"])
print(code)
decrypt = Solution.decode(code)
print(decrypt)
