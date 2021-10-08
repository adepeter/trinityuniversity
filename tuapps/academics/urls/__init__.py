from django.urls import include, path

app_name = 'academics'


urlpatterns = [
    path('programmes/', include('tuapps.academics.urls.programme', namespace='programme')),
]
