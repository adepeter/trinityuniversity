from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('staffs/', include('tuapps.users.urls.staff', namespace='staff'))
]
