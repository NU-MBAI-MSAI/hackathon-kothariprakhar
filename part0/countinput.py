''' 

TJ Stark, Prakhar Kothari, Dani Paredes, Daren Sia 

Version: 1.0 

09/03/2025 

''' 


def countchars(input_string):  

    # excluding intended characters
    exclude_chars = (' ', '.', '!', ',')   
     # filtering out unwanted characters                          
    filtered_string = ''.join(char for char in input_string if char not in exclude_chars)   
    character_count = len(filtered_string) 
    return character_count   

def run_tests():
    # Black-box tests
    assert countchars("Listen, Mr. Jones, calm down.") == 21  
    assert countchars("Hello World!") == 10                    
    assert countchars("No exclusions here") == 17             

    # Clear-box tests
    assert countchars("") == 0                                 
    assert countchars(" ,.!") == 0                             
    assert countchars("1234!?") == 5                           
    assert countchars("Test...") == 4                          

    print("All tests passed!")

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = countchars(user_input)
    run_tests()





''' 

testing example cases  

print(countchars('?')) result = 0 

print(countchars('!')) result = 0 

print(countchars('Welcome to Hackathon')) result = 18 

print(countchars(',')) result = 0 

print(countchars('Here! I am, Where are, you?')) result = 19 

''' 