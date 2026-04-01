class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse = True)
        stack = []

        for pos, sp in cars:
            time = (target - pos) / sp
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
