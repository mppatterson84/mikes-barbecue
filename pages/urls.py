from django.urls import path
from .views import HomePageView, AboutPageView, ParallaxPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('parallax/', ParallaxPageView.as_view(), name='parallax')
]