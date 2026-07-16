class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for p, s in zip(position, speed):
            cars.append([p, s])
        
        cars.sort(reverse=True)
        print(cars)

        st = []
        for car in cars:
            p, s = car[0], car[1]
            time = (target - p) / s
            st.append(time)
            while len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)