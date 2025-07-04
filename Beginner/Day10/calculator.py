from art import logo

def add(n1,n2):
    return n1+n2    
def sub(n1,n2):
    return n1-n2    
def mul(n1,n2):
    return n1*n2    
def div(n1,n2):
    return n1/n2    

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    print(logo)
    num1 = float(input("Enter the first number? : "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        operation_symbol=input("Pick a symbol: ")
        num2 = float(input("Enter the next number? : "))
        calculato =  operations[operation_symbol]
        ans=calculato(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {ans}")
        yesno=input(f"Type 'y' to continue calculationg with {ans}, or 'n' to exit:")
        
        if yesno == "y":
            num1=ans
        else:
            calculator()
            
calculator()
    



