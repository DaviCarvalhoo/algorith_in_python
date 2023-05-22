print("--- Moisés, welcome to Ada Poupança App ---")

i = 0
valor = 0.0
saldo = 1000.00
poupanca = 500.00

while i != 3:
    print("Enter 1 to APPLY, 2 to WITHDRAW, and 3 to EXIT: ")
    i = int(input())
    
    if i == 1:
        print("Application amount: ")
        valor = float(input())
        
        if valor > saldo:
            print("Insufficient current account balance")
        else:
            saldo -= valor
            poupanca += valor
            print("Application successful")
    else:
        if i == 2:
            print(saldo)
            print("Withdrawal amount: ")
            valor = float(input())
            
            if valor > poupanca:
                print("Insufficient savings balance")
            else:
                saldo += valor
                poupanca -= valor
                print("Withdrawal successful")
        else:
            print("Goodbye!")