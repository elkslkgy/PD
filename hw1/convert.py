import sys

for i in range(len(sys.argv)):
	print (sys.argv[i])
	
paper = open(sys.argv[1], "r")
melody = open("melody.txt", "w")
chord = open("chord.txt", "w")

count = 0
tone = ["do", "re", "mi", "fa", "sol", "la", "si", "do2", "re2", "mi2", "fa2", "sol2", "la2", "si2", "do3"]
chord_choice = ["C", "Dm", "F", "G"]
number = [0, 0, 0, 0]

while (True):
	char = paper.read(1)
	if (not char):
		if (count % 4 != 0):
			max = 0;
			for i in range(1, count % 4):
				if (number[i] > number[max]): max = i
			input2 = str(time*4)+" "+chord_choice[max]+" 1;\n"
			chord.write(input2)
		break

	if (count == 0):
		time = 0
		forward_inside = ord(char) % 15
		inside = tone[forward_inside]	
	else: time = int(sys.argv[2])

	a = ord(char) % 15
	if (a > forward_inside):
		forward_inside = (forward_inside + (a % 3)) % 15
	else:
		forward_inside = (forward_inside - (a % 3)) % 15
	inside = tone[forward_inside]
	input = str(time)+" "+inside+" 1;\n"
	melody.write(input)

	if (forward_inside == 0 or forward_inside == 2 or forward_inside == 4 or forward_inside == 9): number[0] += 1
	elif (forward_inside == 1 or forward_inside == 5 or forward_inside == 10): number[1] += 1
	elif (forward_inside == 3 or forward_inside == 7 or forward_inside == 12 or forward_inside == 14): number[2] += 1
	else: number[3] += 1

	if (count % 4 == 3):
		max = 0;
		for i in range(1, 4):
			if (number[i] > number[max]): max = i
		if (count == 3): time = 0
		input2 = str(time*4)+" "+chord_choice[max]+" 1;\n"
		chord.write(input2)
		number = [0, 0, 0, 0]

	count += 1

paper.close()
melody.close()
chord.close()