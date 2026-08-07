class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = k
        count = 0
        left = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                count += 1
            if right >= k-1:
                min_count = min(count,min_count)
                if blocks[left] == "W":
                    count -= 1
                left += 1
        return min_count

        