def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = 0
        freq1 = {}
        freq2 = {}
        window_size = len(s1)

        for i in s1:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1

        for r in range(len(s2)):
            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1

            if r - l + 1 > window_size:
                freq2[s2[l]] -= 1

                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]

                l += 1

            if r - l + 1 == window_size:
                if freq1 == freq2:
                    return True

        return False

s1 = "ab"
s2 = "sjdbalsj"
print(checkInclusion(s1, s2))