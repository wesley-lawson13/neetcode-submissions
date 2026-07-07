class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        sorted_cars = sorted(cars, key = lambda car: car[0], reverse = True)
        print(f"cars: {sorted_cars}")

        time_st = []
        for p, s in sorted_cars:
            time_st.append((target - p) / s)        
            if len(time_st) >= 2 and time_st[-1] <= time_st[-2]:
                time_st.pop()
            
        return len(time_st)

        
