from django.urls import path, include

urlpatterns = [
    path('authentication/', include('api.authentication.urls')),
    path('user/', include('api.users.urls')),
    path('book/', include('api.book.urls')),
    path('question/', include('api.question.urls')),
    path('comment/', include('api.comment.urls')),
]
