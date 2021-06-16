"""
Write a class constructed by 3 rows of a 3X3 matrix.
One method to get the determinant. One method to get the inverse
"""

class Matrix:

    def __init__(self, row1, row2, row3):
        self.r1 = row1
        self.r2 = row2
        self.r3 = row3

    def getDeterminant(self):
        first_term = self.r1[0] * (self.r2[1] * self.r3[2] - self.r3[1] *self.r2[2])
        second_term = self.r1[1] * (self.r2[0] * self.r3[2] - self.r3[0] *self.r2[2])
        third_term = self.r1[2] * (self.r2[0] * self.r3[1] - self.r3[0] *self.r2[1])

        return first_term - second_term + third_term


    def get2X2Det(self,row1,row2):
        return row1[0] * row2[1] - row1[1] * row2[0]

    def getInverse(self):
        d = self.getDeterminant()
        if d == 0:
            return "Matrix has no Inverse"
        else:
            #Co-Factor
            a1 = self.get2X2Det([self.r2[1],self.r2[2]],[self.r3[1],self.r3[2]])/d
            a2 = self.get2X2Det([self.r2[0],self.r2[2]],[self.r3[0],self.r3[2]])/d
            a3 = self.get2X2Det([self.r2[0],self.r2[1]],[self.r3[0],self.r3[1]])/d
            b1 = self.get2X2Det([self.r1[1],self.r1[2]],[self.r3[1],self.r3[2]])/d
            b2 = self.get2X2Det([self.r1[0],self.r1[2]],[self.r3[0],self.r3[2]])/d
            b3 = self.get2X2Det([self.r1[0],self.r1[1]],[self.r3[0],self.r3[1]])/d
            c1 = self.get2X2Det([self.r1[1],self.r1[2]],[self.r2[1],self.r2[2]])/d
            c2 = self.get2X2Det([self.r1[0],self.r1[2]],[self.r2[0],self.r2[2]])/d
            c3 = self.get2X2Det([self.r1[0],self.r1[1]],[self.r2[0],self.r2[1]])/d
            a2 = -a2
            b1 = -b1
            b3 = -b3
            c2 = -c2

            return [
                [a1,b1,c1],
                [a2,b2,c2],
                [a3,b3,c3]
                ]
    def printInverse(self):
        inv = self.getInverse()
        print("The Inverse of the matrix is below")
        for row in inv:
            for entry in row:
                entry = round(entry,2)
                print(f"{entry:^6}", end = "")
            print()

rowa = [1,2,3]
rowb = [3,2,2]
rowc = [1,1,1]
vector = Matrix(rowa,rowb,rowc)
print(vector.getDeterminant())
print(vector.printInverse())
