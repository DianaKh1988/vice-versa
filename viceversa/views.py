
from django.shortcuts import render


def main(request):
	return render(request, 'main.html')

def reverse(request):
	user_text = request.GET['usertext']
	count_word = 0
	count_word = len(user_text.split())  
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {
		'usertext':user_text,
		'reversedtext':reversed_text,
		'countword': count_word
	})