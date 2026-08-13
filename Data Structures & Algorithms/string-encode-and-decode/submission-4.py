class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in strs:
            converted = f"{len(i)}#{i}" 
            encoded_str += converted
        return encoded_str

    def decode(self, s: str) -> List[str]:
        r = 0
        strs = []
        while r < len(s):
            nos_ending_index = r
            while s[nos_ending_index] != "#" and nos_ending_index < len(s):
                nos_ending_index += 1

            length_of_string = int(s[r:nos_ending_index])

            r = nos_ending_index + 1
            str_to_add = ""

            while r < len(s) and length_of_string:
                str_to_add += s[r]
                r += 1
                length_of_string -= 1
            
            strs.append(str_to_add)
        return strs




            

