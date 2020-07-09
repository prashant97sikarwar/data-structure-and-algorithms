class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        try:
            des = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except:
            des = 100000
        
        for i in range(2,len(coordinates)):
            try:
                slope = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0])
            except:
                slope = 100000
            if slope != des:
                    return False
                
        return True