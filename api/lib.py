
from random import Random


def generateOtp(limit):
  
  otps  = []
  for otp in range(limit):  
    otp = otp + 1  # it start from 0 whole number , so we add 1 to each number for narutal number
    otps.append(otp)

  print(otps)


generateOtp(6)