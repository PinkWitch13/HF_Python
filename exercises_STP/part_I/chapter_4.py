"""1. Write a function that takes a numberas an input
    and returnes that number squared.  """

def num_squared(num: int) -> int:
    return num ** 2

result = num_squared(5)
print(result)


"""2. Create a function that accepts a string as a parameter 
    and prints it.  """

def prt_string(s: str) -> str:
    print(s)

prt_string('Lusia')


"""3. Write a function that takes three parameters 
    and two optional parameters.  """

def multi_prm(num1, num2, num3, num4= 4, num5= 5) -> int:
    result = num1 + num2 + num3 + num4 + num5
    return result

result_prm = multi_prm(1, 2, 3)
print(result_prm)

result_opt = multi_prm(1, 2, 3, 6, 7)
print(result_opt)


"""4. Write a program with two functions. 
    The first function should take an integer as a parameter
    and return the result of the integer division by 2.
    The second function should take an integer as a parameter
    and return the result of integer multiplied by 4.
    Call the first functionn, save the result as a variable, 
    and pass it a as a parameter to the second function.  """

def first_fun(par1) -> int:
    result = par1 / 2
    return result

def second_fun(par2):
    final_result = int(par2* 4)
    return final_result

result = first_fun(6)
print(f"{second_fun(result)=}")

"""5. Write a function that converts a string into a float
    and returns the result. Use exception handling to catch
    all of the exeption that could occur.  """

def str_to_float(string1):
    result = None
    try:
        result = float(string1)
    except ValueError:
        print('Wrong string value, value has to be a float!')
    except TypeError:
        print('Wrong value type, type has to be a string!')
    return result

result1 = str_to_float('Kuba')
print(result1)
result2 = str_to_float('6')
print(result2)
result3 = str_to_float(None)
print(result3)
result4 = str_to_float('0,5')
print(result4)
result5 = str_to_float('0.5')
print(result5)

"""6. Add a docstring to all of the functions you wrote in challenges 1-5"""