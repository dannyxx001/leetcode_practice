class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = [A,C,E,G]
        y = [B,D,F,H]
        x.sort()
        y.sort()
        if (x != [A,C,E,G] and x != [E,G,A,C]) and (y != [B,D,F,H] and y != [F,H,B,D] ):
            return (C-A)*(D-B) + (G-E)*(H-F) - (x[2]-x[1])*(y[2]-y[1])
        else:
            return (C-A)*(D-B) + (G-E)*(H-F)