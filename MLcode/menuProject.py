import os

print("""
1 - to open chrome
2 - to open vscode here 
3 - to show date
4 - to check your ip
5 - to exit
""")

while(True):
    x = int(input("Enter your choice: "))
    if x == 1:
        os.system('start chrome')
    elif x == 2:
        os.system('code .')
    elif x==3:
        os.system('date')
    elif x==4:
        os.system('ipconfig')
    elif x == 5:
        break
