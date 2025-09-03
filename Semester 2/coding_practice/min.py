number = [4, 5, 2, 1, 7]

minimumNumber = numbers[0]
#take index 0 , take that number

# for currentNumberIndex in range( len(numbers) ):

# print( list( range(6))
      
# print(numbers(currentNumberIndex) )

# if numbers( currentnumberindex ) < minimumNumber

for currentNumberIndex in range( len(numbers) ):
    if numbers[ currentNumberIndex ] < minimumNumber:
        minimumNumber = numbers[ currentNumberIndex ]

print( minimumNumber)