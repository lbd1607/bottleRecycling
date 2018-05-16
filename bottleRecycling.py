#Laura Davis
#13 March 2016
#This program will aggregate a total number of bottles
#returned to a grocery store for seven days. It will then 
#calculate and print the amount paid out by multiplying the 
#total bottles collected by the rate of .10 cents.

#Lab 5-4 The Bottle Return Program

#The main function
def main():
#Declare variables
	totalBottles = 0
	todayBottles = 0
	counter = 1
	totalPayout = 0
	endProgram = "no"
	while endProgram == "no":
#Function calls
		totalBottles = getBottles()
		totalPayout = calcPayout(totalBottles)
		printInfo(totalBottles, totalPayout)
		endProgram = raw_input("Do you want to end the program? (Enter yes or no): ")
#This function will get the number of bottles returned.
def getBottles():
	totalBottles = 0
	todayBottles = 0
	counter = 1
	while counter <= 7:
		todayBottles = input("Enter number of bottles for day #" + str(counter) + "--> ")
		totalBottles = totalBottles + todayBottles
		counter = counter + 1
	return totalBottles
#This function will calculate the payout.
def calcPayout(totalBottles):
	totalPayout = totalBottles * .10
	return totalPayout
#This function will display the information.
def printInfo(totalBottles, totalPayout):
	print "The total number of bottles collected is", totalBottles
	print "The total paid out is $", totalPayout
#calls main
main()
