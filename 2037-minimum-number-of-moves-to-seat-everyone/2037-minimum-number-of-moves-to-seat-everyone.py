class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        f=0
        for i in range(len(seats)):
            f+=abs(students[i]-seats[i])
        return f