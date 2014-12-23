CS313
=====
import functools

def main()
	
	#Open nim.txt for reading
	nim_file = open('nim.txt', 'r')

	#Read the number of games from line 1, create a loop for number of games, split line to get number of counters in each pile 

	for i in range(num_Games):
		Heaps = nim_file.readline().split()

	#Convert the number of counters into integers
		Heaps = list(map(int, Heaps))

	#Calculate the sum
		nim_sum = functools.reduce(lambda b,a: a^b, Heaps)

	#If nim sum is zero write Lose Game and continue
	if (nim_sum == 0):
		print("Lose Game")
	else:
		#Create a loop to go through each pile in that game, compute individual nim sum with that pile
		for j in range (len(Heaps)):
			heap_NimSum = Heaps[j]^nim_sum

	#If nim sum is less than the number of counters in that pile remove the difference 
			if (heap_NimSum < Heaps[j]):
				counters = Heaps[j] - heap_NimSum
	      
	#Write result
				print ("Remove", counters, "counters from Heap", j + 1)
	#Exit loop
				break

	#Close file
	nim_file.close()

main()
