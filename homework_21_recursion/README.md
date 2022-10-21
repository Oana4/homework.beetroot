#############################################

# All tasks should be solved using recursion

#############################################

<br /> 

**Task 1**

from typing import Optional
<br />
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    pass
    
    # Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
 

<br />

**Task 2**

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    pass
   
    # Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    

 <br />

**Task 3**

def mult(a: int, n: int) -> int:
    pass
    # This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
   

 <br />

**Task 4**

def reverse(input_str: str) -> str:
 
    # Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
  

 <br />

**Task 5**

def sum_of_digits(digit_string: str) -> int:
 
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
 
