class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for i in range(len(encoded)):
            answer.append(encoded[i] ^ answer[-1])
        return answer