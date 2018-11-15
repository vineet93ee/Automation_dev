def pig_letter(word):

	first_letter = word[0]
	#print(first_letter)
	if first_letter in 'aeiou':
		#print(first_letter)
		pig_word = word + 'ay'
		print(pig_word)
	else:
		pig_word = word[1:] + first_letter + 'ay'		
		
		return pig_word

result = pig_letter("cpple")
reu = type(print(result))