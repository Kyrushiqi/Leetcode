# Question: https://leetcode.com/problems/design-underground-system
# Submission: https://leetcode.com/problems/design-underground-system/submissions/1903639694/

# Understand: 
# Underground Railway System class --> tracks customer travel time btw. diff. stations. 
# Using the data, calculate average time it takes to travel btw. 2 diff. stations.

# UndergroundSystem class: 
# void checkIn() --> Parameters of CardID, stationName, time
#   > Customer can only check into 1 place at a time. Can't be 2 or more.
# void checkOut() --> ''' 
#   > Customer can check out of 1 place. Can't be 2 or more b/c a customer can only check into 1 place.

# double getAverageTime() --> Returns the avg time it takes to travel from start to end station.
# > Calculate Average of customers who go from Start to end station.
# > Start - End != End - Start (Times can be diff b/c of delays) (Treat it as always different in this case) 
# > At least 1 customer may not be counted towards the average.

# Note: Check in time < Check out time

# Edge Cases: 
# Customer can travel to many destinations. A -> B and C -> D

class UndergroundSystem:

    def __init__(self): # O(1)
        self.customerCheckIn = {} # Used in checkIn and checkOut -- {id : (startStation, startTime)}
        self.location = {} # Used in getAverageTime -- {Location : (counter, total time)}

    def checkIn(self, id: int, stationName: str, t: int) -> None: # O(1)
        if id not in self.customerCheckIn: 
            self.customerCheckIn[id] = (stationName, t) # {id : (stationName, t)}

    def checkOut(self, id: int, stationName: str, t: int) -> None: # O(1)
        totalTime = t - self.customerCheckIn[id][1] # End - Start time
        fullStationName =  self.customerCheckIn[id][0] + " " + stationName # Concatenate StartStation + EndStation
        if fullStationName not in self.location: # O(1)
            self.location[fullStationName] = [1, totalTime]
            # Update the counter and add the total time
        else: 
            self.location[fullStationName][0] += 1
            self.location[fullStationName][1] += totalTime

        del self.customerCheckIn[id] # O(1) # Empty out the tuple/object at that id to express a customer has arrived at a destination. A new route can be checked in to. 

        # 33 A -> B, A -> B
        

    def getAverageTime(self, startStation: str, endStation: str) -> float: # O(1)
        fullStationName = startStation + " " + endStation 
        return self.location[fullStationName][1] / self.location[fullStationName][0]
        # totalTime / counter

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)