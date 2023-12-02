#!/usr/bin/env python3
# encoding: utf-8
# 4 Freedom Robotic Arm Agreement: Given the corresponding coordinates (x, y, z), and pitch angle to calculate the angle of each joint rotation
# 2020/07/20 Aiden
import logging
from math import *

# CRITICAL, ERROR, WARNING, INFO, DEBUG
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class IK:
    # Cross from bottom to top of the steering gear
    # Public parameters, that is, the connecting rod parameter of the 4 free robotic arm
    l1 = 8.00    #The distance from the center of the robotic chassis to the center of the second turbine is 6.10cm
    l2 = 6.50   #The distance from the second steering gear to the third steering gear is 10.16cm
    l3 = 6.20    #The distance from the third steering gear to the fourth steering gear 9.64cm
    l4 = 0.00    #No specific assignment here, re -assign value according to the selection of initialization

    # Pump -model unique parameter
    l5 = 4.70  #The distance from the fourth steering gear to the mouth of the mouth is 4.70cm
    l6 = 4.46  #The distance from the upper above the mouth to the mouth is 4.46cm
    alpha = degrees(atan(l6 / l5))  #Calculate the angle of L5 and L4

    def __init__(self, arm_type): #According to different clamps, adaptation parameters
        self.arm_type = arm_type
        if self.arm_type == 'pump': #If it is a gas pump robotic arm
            self.l4 = sqrt(pow(self.l5, 2) + pow(self.l6, 2))  #The fourth steering gear to the mouth sucks as the fourth link
        elif self.arm_type == 'arm':
            self.l4 = 10.00  #The distance from the fourth steering gear to the end of the robotic arm is 16.6cm, and the ends of the robotic arm refer to when the claws are completely closed

    def setLinkLength(self, L1=l1, L2=l2, L3=l3, L4=l4, L5=l5, L6=l6):
        # Change the length of the rod of the robotic arm, in order to adapt to the robotic arm of the same structure and different lengths
        self.l1 = L1
        self.l2 = L2
        self.l3 = L3
        self.l4 = L4
        self.l5 = L5
        self.l6 = L6
        if self.arm_type == 'pump':
            self.l4 = sqrt(pow(self.l5, 2) + pow(self.l6, 2))
            self.alpha = degrees(atan(self.l6 / self.l5))

    def getLinkLength(self):
        # Get the connecting rod length of the current settings
        if self.arm_type == 'pump':
            return {"L1":self.l1, "L2":self.l2, "L3":self.l3, "L4":self.l4, "L5":self.l5, "L6":self.l6}
        else:
            return {"L1":self.l1, "L2":self.l2, "L3":self.l3, "L4":self.l4}

    def getRotationAngle(self, coordinate_data, Alpha):
        # Given a specified coordinate and pitch angle, and return the angle of each joint should be rotated. If there is no solution, return false
        # Coordinate_data is the end coordinate of the holder, and the coordinate unit CM is passed in in the form of a metal group, for example (0, 5, 10)
        # Alpha is the angle between the holder and the horizontal plane, the unit degree

        # The end of the holder is p (x, y, z), the coordinate original point is O, the origin is the projection of the ground in the center of the Yundai, and the projection of P point on the ground is P_
        # The intersection of L1 and L2 is A, L2 and L3 intersection.
        # CD and PD are vertical, CD and Z axis vertical, then the pitch angle Alpha is the angle between DC and PC, AE vertical DP_, and E on DP_, CF vertical AE, and F on AE on AE
        # Angle representation: For example, the angle of AB and BC is expressed as ABC
        X, Y, Z = coordinate_data
        if self.arm_type == 'pump':
            Alpha -= self.alpha
        #Seeking the angle of rotation of the seat
        theta6 = degrees(atan2(Y, X))
 
        P_O = sqrt(X*X + Y*Y) #P_ to the origin o distance
        CD = self.l4 * cos(radians(Alpha))
        PD = self.l4 * sin(radians(Alpha)) #When the pitch angle is positive, the PD is positive, when the pitch angle is negative, the PD is negative
        AF = P_O - CD
        CF = Z - self.l1 - PD
        AC = sqrt(pow(AF, 2) + pow(CF, 2))
        if round(CF, 4) < -self.l1:
            logger.debug('Height is lower than 0, CF(%s)<l1(%s)', CF, -self.l1)
            return False
        if self.l2 + self.l3 < round(AC, 4): #The sum of the two sides is less than the third side
            logger.debug('Cant constitute a link structure, l2(%s) + l3(%s) < AC(%s)', self.l2, self.l3, AC)
            return False

        #Seeking Theta4
        cos_ABC = round((pow(self.l2, 2) + pow(self.l3, 2) - pow(AC, 2))/(2*self.l2*self.l3), 4) #Yu Xian theorem
        if abs(cos_ABC) > 1:
            logger.debug('Cant constitute a link structure, abs(cos_ABC(%s)) > 1', cos_ABC)
            return False
        ABC = acos(cos_ABC) #Anti -triangle calculates arc
        theta4 = 180.0 - degrees(ABC)

        #Seeking Theta5
        CAF = acos(AF / AC)
        cos_BAC = round((pow(AC, 2) + pow(self.l2, 2) - pow(self.l3, 2))/(2*self.l2*AC), 4) #Yu Xian theorem
        if abs(cos_BAC) > 1:
            logger.debug('Cant constitute a link structure, abs(cos_BAC(%s)) > 1', cos_BAC)
            return False
        if CF < 0:
            zf_flag = -1
        else:
            zf_flag = 1
        theta5 = degrees(CAF * zf_flag + acos(cos_BAC))

        #Seeking Theta3
        theta3 = Alpha - theta5 + theta4
        if self.arm_type == 'pump':
            theta3 += self.alpha

        return {"theta3":theta3, "theta4":theta4, "theta5":theta5, "theta6":theta6} # Return to the angle dictionary when there is a solution
            
if __name__ == '__main__':
    ik = IK('arm')
    #ik.setLinkLength(L1=ik.l1 + 1.30, L4=ik.l4)
    print('Link length:', ik.getLinkLength())
    #print(ik.getRotationAngle((0, ik.l4, ik.l1 + ik.l2 + ik.l3), 0))
