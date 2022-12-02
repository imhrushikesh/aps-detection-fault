import sys,os

def error_message_detail(error, error_detail: sys):
     pass 
  



class SensorException(Exception):

     def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

     def __str__(self):
        return self.error_message


