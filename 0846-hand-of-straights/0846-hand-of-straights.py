class Solution:
    def isNStraightHand(self, hand, groupSize):
        hand.sort()
        s = Counter(hand)
        for card in hand:
            if s[card] > 0:
                for i in range(groupSize):
                    if s[card + i] > 0:
                        s[card + i] -= 1
                    else:
                        return False
        return True
