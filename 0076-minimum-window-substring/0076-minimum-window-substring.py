class Solution:
    def minWindow(self, s: str, t: str) -> str:
    

        lengthS = len(s)
        lengthT = len(t)

        # first case t cannot be a substring of s
        if lengthT > lengthS: return ""

        # Create initial dictionary
        tDict = dict.fromkeys(t,0)

        for letter in t:
            tDict[letter] = tDict[letter] + 1
        
        #print(tDict)
        #yes works
        #print(tDict)

        # so now we can iterate through the string s looking for substrings.
        # first we try to find a mw substring.
        # then we 

        foundSubstring = ""
        cursor = 0
        endCursor = 0

        # first find first instance of letter appearing,  iterate from there.
        # then find first substring.
        # now that you have all substrings, you can search iteratively through the rest.

        for letterIndex in range(len(s)):
            if s[letterIndex] in tDict.keys():
                cursor = letterIndex
                break
        
        for letterIndex in range(cursor, len(s)):
            currentLetter = s[letterIndex]
            if currentLetter in tDict.keys():
                tDict[currentLetter] = tDict[currentLetter] - 1
                if all(value <= 0 for value in tDict.values()):
                    endCursor = letterIndex + 1          
                    foundSubstring = s[cursor:letterIndex+1]
                    #print(foundSubstring)
                    break

        if foundSubstring == "": return ""
        if endCursor == len(s):
            done = False
            while not done:
                #print("length of new = " + str(endCursor - cursor))
                #thing not in keys
                cursorLetter = s[cursor]
                if cursorLetter not in tDict.keys():
                    cursor = cursor + 1
                    continue
                # if there is still more of that letter to "spend"
                done = tDict[cursorLetter] >= 0
                if not done:
                    tDict[cursorLetter] = tDict[cursorLetter] + 1
                    cursor = cursor + 1
                if (endCursor - cursor) < len(foundSubstring):
                        #print("found new substring")
                        foundSubstring = s[cursor:endCursor]
            
            return foundSubstring

        #print(str(len(foundSubstring)))

        # now lets see if we can reduce the start
        done = False
        while not done:
            print("length of new = " + str(endCursor - cursor))
            #thing not in keys
            cursorLetter = s[cursor]
            if cursorLetter not in tDict.keys():
                cursor = cursor + 1
                continue
            # if there is still more of that letter to "spend"
            done = tDict[cursorLetter] >= 0
            if not done:
                tDict[cursorLetter] = tDict[cursorLetter] + 1
                cursor = cursor + 1
            if (endCursor - cursor) < len(foundSubstring):
                   # print("found new substring")
                    foundSubstring = s[cursor:endCursor]

        # so there are more letters to check!

        for letterIndex in range(endCursor, len(s)):
            #print(tDict)
            currentLetter = s[letterIndex]
            endCursor = endCursor + 1
            if currentLetter in tDict.keys():
                tDict[currentLetter] = tDict[currentLetter] - 1

                # now lets see if we can reduce the start
                done = False
                while not done:
                    #print("length of new = " + str(endCursor - cursor))
                    #thing not in keys
                    cursorLetter = s[cursor]
                    if cursorLetter not in tDict.keys():
                        cursor = cursor + 1
                        continue
                    # if there is still more of that letter to "spend"
                    done = tDict[cursorLetter] >= 0
                    if not done:
                        tDict[cursorLetter] = tDict[cursorLetter] + 1
                        cursor = cursor + 1
                    if (endCursor - cursor) < len(foundSubstring):
                            #print("found new substring")
                            foundSubstring = s[cursor:endCursor]

        return foundSubstring
        