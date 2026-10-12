class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(key = lambda car : car[0]) # sort on position

        st = [] # takes (finish_time)
        for i in range(len(cars) - 1, -1, -1):
            
            car = cars[i]
            time_to_finish = (target - car[0]) / car[1]
            st.append(time_to_finish)
            while len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        return len(st)


