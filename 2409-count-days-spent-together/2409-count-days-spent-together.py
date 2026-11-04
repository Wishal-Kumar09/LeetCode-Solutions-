class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]

        CummonthDays = [0] * 13

        for i in range(1, 13):
            CummonthDays[i] = CummonthDays[i-1] + monthDays[i-1]

        
        arrival_day_alice = CummonthDays[(int(arriveAlice[:2])-1)] + int(arriveAlice[3:])
        departure_day_alice = CummonthDays[(int(leaveAlice[:2])-1)] + int(leaveAlice[3:])
        arrival_day_bob = CummonthDays[(int(arriveBob[:2])-1)] + int(arriveBob[3:])
        departure_day_bob = CummonthDays[(int(leaveBob[:2])-1)] + int(leaveBob[3:])

        arrival_range = [arrival_day_alice,arrival_day_bob]
        departure_range = [departure_day_alice,departure_day_bob]

        res = (min(departure_range) - max(arrival_range) + 1)

        if res < 0:
            return 0
        else:
            return res
