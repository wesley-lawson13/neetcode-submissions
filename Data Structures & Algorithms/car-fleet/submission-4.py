class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = []
        for p, s in zip(position, speed):
            cars.append([p, s])
        
        sorted_cars = sorted(cars, reverse=True)
        st = []
        for p, s in sorted_cars:
            time = (target - p) / s
            st.append(time)
            while len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        
        return len(st)
