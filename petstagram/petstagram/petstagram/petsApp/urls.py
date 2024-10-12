from django.urls import path, include

from petstagram.petsApp.views import home_page, register_page, login_page, profile_details, edit_profile, \
    delete_profile, add_pet

urlpatterns = [
    path('', home_page, name='home_page'),
    path('accounts/', include([
        path('register/', register_page, name='register_page'),
        path('login/', login_page, name='login_page'),
        path('profile/<int:pk>/', include([
            path('', profile_details, name='profile_details'),
            path('edit/', edit_profile, name='edit_profile'),
            path('delete/', delete_profile, name='delete_profile'),
        ]))
    ])),
    path('pets/add/', add_pet, name='add_pet'),
    path('pets/<str:username>/pet/<slug:pet_slug>/', include([
        # path('edit/',)
    ]))
]