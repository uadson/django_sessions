from django.shortcuts import render
from django.views.generic import FormView


class SessionView(FormView):

	def get(self, request):
		print(dir(request.session))
		print(request.session.session_key)

		print(request.user)

		request.session['user'] = {}

		print(request.session['user'])

		return render(request, 'index.html')
	
	def post(self, request):
		
		return render(request, 'index.html')
