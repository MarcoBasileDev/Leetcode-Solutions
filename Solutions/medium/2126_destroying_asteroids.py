class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for a in asteroids:
            if mass < a:
                return False

            mass += a
        
        return True
    
        # Time complexity: O(n log n) -> sorting
        # Space complexity: O(n) or O(log n) -> based on which sorting algorithm is used