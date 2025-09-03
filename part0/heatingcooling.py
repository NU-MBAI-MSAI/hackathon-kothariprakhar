''' 

TJ Stark, Prakhar Kothari, Dani Paredes, Daren Sia 

Version: 1.0 

09/03/2025 

'''

def heating_cooling():  

    heating = 0  
    cooling = 0 

    while True: 
        #checking for integer values
        try: 
            temp = int(input("Enter the average daily temperature: ")) 
        except ValueError: 
            print("Please enter a valid integer.") 
            continue 
    
        if temp < -459: 
            break 
        elif temp < 60: 
            heating += 1 
        elif temp > 80: 
            cooling += 1 
    
    print(f"Heating days: {heating}") 
    print(f"Cooling days: {cooling}") 

if __name__ == "__main__":
    heating_cooling()




''' 

TestCase1: Enter non-integer. Result = “Must Enter Integer” 

TestCase2: Day1 = 59, Day2 = -460. Result = “Cooling Days: 0 Heating Days: 1” 

TestCase3: Day1 = 80, Day2 = 81, Day3 = -460 Result = “Cooling Days: 1 Heating Days: 0” 

TestCase4: Day1 = 60, Day2 = 59, Day3 = -460. Result = “Cooling Days: 0 Heating Days: 1” 

TestCase5: Day3 = -460, Day2 = 62 Result = “Cooling Days: 0 Heating Days: 0” 

TestCase6: Day7 = -460, Day2 = -458, Day3 = 59, Day4 = 60, Day5 = 70, Day6 = 80, Day1 = 81 Result = “Cooling Days: 1 Heating Days: 2” 

 

''' 





    