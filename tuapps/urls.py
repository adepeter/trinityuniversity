from django.urls import include, path

app_name = 'tu'

urlpatterns = [
    path('', include('tuapps.home.urls', namespace='home')),
    path('newsletters/', include('tuapps.newsletters.urls', namespace='newsletters')),
    path('galleries/', include('tuapps.galleries.urls', namespace='galleries')),
    path('academics/', include('tuapps.academics.urls', namespace='academics')),
    path('faculties/', include('tuapps.faculties.urls', namespace='faculties')),
    path('auths/', include('tuapps.auths.urls', namespace='auths')),
    path('blogs/', include('tuapps.blogs.urls', namespace='blogs')),
    path('users/', include('tuapps.users.urls', namespace='users')),
    path('pages/', include('tuapps.pages.urls', namespace='pages')),
    path('jobs/', include('tuapps.jobs.urls', namespace='jobs')),
]
