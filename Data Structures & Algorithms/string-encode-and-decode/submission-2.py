class Solution:
    # Instead of: "hello" + "world" (lost boundaries)
    # Do this: "5#hello5#world"
    #          ↑ length  ↑ word  ↑ length ↑ word

    # "5#hello5#world"
    # Read: 5 → take 5 chars → "hello"
    # Read: 5 → take 5 chars → "world"
    # Perfect! You know exactly where boundaries are

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for item in strs:
            length = len(item)
            result += str(length) + "#" + item
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Read the length here
            j = s.index("#", i)
            length = int(s[i:j])
            
            # Skip the '#' and read that many characters
            word = s[j+1:j+1+length]
            result.append(word)
            
            i = j + 1 + length
        
        return result