# count.py
# Prog to ask user for name and number, then count by 2

print('##### Counting by 2s #####')

while True:
  name=input('What is your name? ').capitalize()
  if name.isalpha():
    print('Hello '+ name)
    break
  else:
    print('Please enter a valid name')

while True:
  num=input("Please enter a number: ")
  if num.isdigit():  
    break
  else:
    print('Invalid input, Please enter a number')    

num = int(num) #converts string to integer

input('Counting to '+ str(num)+' - press Enter to start: ')

for x in range(1,num+1,2):
			print(x)

print('Done!')
