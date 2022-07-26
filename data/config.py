import os, sys
try:
 choice=input('''
1) Back to main menu
2) Exit
Choose option: ''')
 if choice=="1":
 	os.system("python main.py")
 elif choice=="2":
 	os.system("exit")
 	print("\nGoodbye :)\n")
 else:
 	print("\nInvalid option")

except KeyboardInterrupt:
	print("Happy day :)")