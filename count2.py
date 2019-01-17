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
    print('Please enter a number')

input('Counting to '+ str(num)+' - press Enter to start: ')

for x in range(0, num+1, 2):
  print(x)

#while True:
# try:
#   endNum = int(input("Please enter a number: "))
#   break
# except ValueError:
#   print("That is not a number")

# endNum = input('Enter a number: ')
#while True:
 # name=input('What is your name? ').capitalize()
  #if name.isalpha():
   # print('Hello '+ name)
    #break
  #else:
   # print('Please enter a valid name')

#num=4
#for x in range(0, num+1, 2):
 # print(str(x))


 #functions
 # def checkRange1(greaterThan)
 # greaterThan = int(greaterThan)
 # If greaterThan >100;
  #print()
  #greaterThan = 100
  #return greaterThan
  #else:
  #return greaterThan
 # def checkRange2(LessThan)
  #If lessThan < 3;
  # return ture
  #else:
  #return False

 #checkRange(num) 