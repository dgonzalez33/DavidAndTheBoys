from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view()),
	url(r'^simulation/$', views.SimulationView.as_view()), 
	url(r'^setInformation/$', views.setInformation, name ='setInformation'),
]