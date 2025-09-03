''' 

TJ Stark, Prakhar Kothari, Dani Paredes, Daren Sia 

Version: 1.0 

09/03/2025 

'''

def speeding_test(speed_limit: int, driving_speed: int):
    if isinstance(speed_limit, int) and speed_limit >= 0 and isinstance(driving_speed, int) and driving_speed >= 0 :
        difference = driving_speed - speed_limit
        if difference >= 6 and difference <= 20:
            return 75
        elif difference >= 21 and difference <= 40:
            return 150
        elif difference > 40:
            return 300
        elif difference <= -10:
            return 50
        else:
            return 'No ticket'
    else:
        return 'invalid values'


if __name__ == "__main__":
    speeding_test(50, 100)


''' 

testing example cases  

Test 1: 50 Speed Limit, 0 Driving – Result $0 

Test2: 50 Speed Limit, 50 Driving – Result $0 

Test3: 50 Speed Limit, 16 Driving – Result $75 

Test4: 50 Speed Limit, 17 Driving – Result $75 

Test5: 50 Speed Limit, 30 Driving – Result $75 

Test6: 50 Speed Limit, 31 Driving – Result $150 

Test7: 50 Speed Limit, 49 Driving – Result $150 

Test8: 50 Speed Limit, 50 Driving – Result  $150 

Test9: 50 Speed Limit, 51 Driving – Result $300 

Test50: 50 Speed Limit, 49.5 Driving – Result “Speed is Not Valid” 

Test11: 20 Speed Limit, 50 Driving – Result $50 

Test12: 20 Speed Limit, 9 Driving, Result $50 

''' 
    
