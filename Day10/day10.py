def my_function():
    result = 3*2
    return result
output= my_function()
print(output)

def format_name(f_name, l_name):
   """Take a first and last name and format it."""
   formatted_f_name=f_name.title()
   formatted_l_name=l_name.title()
   return f"{formatted_f_name} {formatted_l_name}"
format_string=format_name("Anuj","acharya")

print(format_string)

# ////////////////////////////////////////
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
 
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month==2:
    return 29 
  else:
    return(month_days[month-1])
  
# Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)





