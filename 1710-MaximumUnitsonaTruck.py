class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0

        for box in boxTypes:
            can_take = min(truckSize, box[0])
            total += can_take * box[1]
            truckSize -= can_take
            if truckSize == 0:
                return total
        return total
    
    # Time complexity = O(nlogn), sorting
    # Space complexity = O(1)
