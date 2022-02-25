from django.urls import path

from rest_framework_jwt.views import refresh_jwt_token

from myapp.views import ( 
    CreateSnippestsView,
    CreateTagView,
    DetailSnippestsView,
    DetailTagView,
    LoginView,
    SignupView,
    
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('refresh', refresh_jwt_token),
    path('signup', SignupView.as_view(), name='signup'),

    path('snippests', CreateSnippestsView.as_view(), name='snippests.create'),
    path('snippests/<pk>', DetailSnippestsView.as_view(), name='snippests.details'),

    path('tags', CreateTagView.as_view(), name='tags.create'),
    path('tags/<pk>', DetailTagView.as_view(), name='tags.details'),

]
