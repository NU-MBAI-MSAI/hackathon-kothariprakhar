''' 

TJ Stark, Prakhar Kothari, Dani Paredes, Daren Sia 

Version: 1.0 

09/03/2025 

'''

def max_profit(prices):  

    max = 0  

    try:  

        min_price = prices[0]  

    except IndexError:  

        return 0 

  

    min = prices[0]  

    for price in prices:  

        if price < min:  

            min = price  

        profit = price - min  

        if profit > max:  

            max = profit   

    return max 


def run_tests():

    assert max_profit([]) == 0 
    assert max_profit([1]) == 0                   
    assert max_profit([1,2]) == 1                                
    assert max_profit([1,2,3,4,5,6,7,8,9]) == 8                             
    assert max_profit([9,8,7,6,5,4,3,2,1]) == 0                                                   

    print("All tests passed!")

if __name__ == "__main__":
    max_profit([1,2,3,4,5,6,7,8,9])



''' 

testing example cases  

print(max_profit([]))   

# result = 0 

print(max_profit([1]))  

# result = 0 

print(max_profit([1,2])) 

# result = 1 

print(max_profit([1,2,3,4,5,6,7,8,9])) 

# result = 8 

print(max_profit([9,8,7,6,5,4,3,2,1])) 

# result = 0 

''' 