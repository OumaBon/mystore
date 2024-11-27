from django.urls import path
from .views import *

# app_name = 'accounts'

urlpatterns = [
    path('', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('address/', AddressBookView.get, name='address'),
    path('create_address/', AddressBookView.create, name='add_address'),
    path('dia-chi/xoa-dia-chi/<int:id>/', AddressBookView.delete, name='delete_address'),
    path('dia-chi/sua-dia-chi/<int:id>/', AddressBookView.update, name='edit_address'),
    path('dia-chi/cap-nhat-dia-chi/<int:id>/', AddressBookView.update, name='update_address'),
    path('dia-chi/thiet-lap-dia-chi/', AddressBookView.set_default, name='set_main_address'),
    path('quen-mat-khau/', forgot_password, name='forgot_password'),
]