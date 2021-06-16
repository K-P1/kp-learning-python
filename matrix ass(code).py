"""
Write a class that'll accept the rows of a 3X3 matrix line by line.
One method to get the determinant. One method to get the inverse
"""
class Matrix:

    def __init__(self,row1,row2,row3):
        self.r1=row1
        self.r2=row2
        self.r3=row3

    def getDeterminant(self):
        first_term = self.r1[0] * (self.r2[1] * self.r3[2] - self.r3[1] *self.r2[2])
        second_term = self.r1[1] * (self.r2[0] * self.r3[2] - self.r3[0] *self.r2[2])
        third_term = self.r1[2] * (self.r2[0] * self.r3[1] - self.r3[0] *self.r2[1])
        
        return first_term-second_term+third_term
    def getInverserow1(self):
        a11=(self.r2[1]*self.r3[2] - self.r2[2]*self.r3[1])#//self.getDeterminant
        a12=-(self.r1[1]*self.r3[2] - self.r1[2]*self.r3[1])#//self.getDeterminant
        a13=(self.r1[1]*self.r2[2] - self.r1[2]*self.r2[1])#//self.getDeterminant
        return a11,a12,a13
    def getInverserow2(self):
        a21=-(self.r2[0]*self.r3[2] - self.r2[2]*self.r3[0])#//self.getDeterminant
        a22=(self.r1[0]*self.r3[2] - self.r1[2]*self.r3[0])#//self.getDeterminant
        a23=-(self.r1[0]*self.r2[2] - self.r1[2]*self.r2[0])#//self.getDeterminant
        return a21,a22,a23
    def getInverserow3(self):
        a31=(self.r2[0]*self.r3[1] - self.r2[1]*self.r3[0])#//self.getDeterminant
        a32=-(self.r1[0]*self.r3[1] - self.r2[1]*self.r3[0])#//self.getDeterminant
        a33=(self.r1[0]*self.r2[1] - self.r1[1]*self.r2[0])#//self.getDeterminant
        return a31,a32,a33

        

rowa=[1,2,3]
rowb=[3,2,2]
rowc=[1,1,1]
vector= Matrix(rowa,rowb,rowc)

print("| 1    2    3 |")
print("| 3    2    2 |")
print("| 1    1    1 |")
print("\n")
print(f"The Determinant of the matix above is: {vector.getDeterminant()}")
print("\n")
print("while the inverse is:")
print(vector.getInverserow1())
print(vector.getInverserow2())
print(vector.getInverserow3())



