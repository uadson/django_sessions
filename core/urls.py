from django.urls import path

from core.views.index import SessionView

# from core.views.index import session_view


app_name = 'core'

urlpatterns = [
	path('', SessionView.as_view(), name='index'),

	#path('', session_view, name='index'),
]