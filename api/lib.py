import math,random

def generateOtp(limit):

  otps  = '1234567890' 
  OTP = ""
  
  for i in range(limit):
    OTP += otps[math.floor(random.random()* 10)]
  return OTP

