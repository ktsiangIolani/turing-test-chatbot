# ML Foundations
# Perceptron 

# Name: Tanner Young
# Purpose of Perceptron (ie what decision is it making): A perceptron is an artificial judgement-making process that is supposed to mimic the proceses of a nueron. It's purpose is to make binary classifications using inputs, weights, and sums.

# TODO 0 Define variables inputs, bias and activation
inputs = ["How chunky is your dog (1-10)?", "How many hours ago did they last eat?", "How active has the dog been today (1-10)?", "How much is the dog begging to be fed (1-10)?"]
weights = [-3, -7, -2, 1]
bias = 0.3

def activation(x):
	max(0,x)

    

def perceptron():
	# TODO 1 Ask the user to answer questions in the inputs array
	# Store each answer in the array answers (use .append to add a new item to the array)
	answers = []
	
	for question in inputs:
		a = int(input(question))
		answers.append(a)
	print(answers)

	# TODO 2 Compute a score based on answers, weights and inputs
	# Recall that the score is the sum of every answer multiplied by it's wieght,
	# multiplied by the bias and then passed through the activation function

	sum = 0
	for i in range(len(answers)):
		sum = sum + answers[i] * weights[i]
    
	# TODO 3 Print out and return the final score
	
	score = activation(sum + bias)
	return score

# TODO 4 Call your function perceptron.
# If the score is above 0, print out what the user should do if the answer is yes
if perceptron() > 0:
	print("Feed your dog!")

# Otherwise, print out what the user should do if the answer is no
else:
	print("Don't feed your dog!... yet!")




