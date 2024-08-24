a = 5
b = 2

try:
    print(a / b)
    k = int(input("Enter a Number: "))
    print("Resource Open")
except ZeroDivisionError as e:
    print(f"Divide by zero exception Message: {e}")

except ValueError as e:
    print(f"Value Error Message: {e}")

except Exception as e:
    print(f"Exception Message: {e}")

#Whatever the case It/code works (runs) or not, finally output will always work and will print the defined output
finally:
    print("Resource Closed")