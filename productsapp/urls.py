from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('store',views.store,name='store'),
    path('addcategory',views.addcategory,name='addcategory'),
    

    path('addpro',views.addpro,name='addpro'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
    path('deletedetails/<int:pk>',views.deletedetails,name='deletedetails'),
    # path('logout',views.logout,name='logout'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('login_user',views.login_user,name='login_user'),
    path('log_out',views.log_out,name='log_out'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('showuser',views.showuser,name='showuser'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('items',views.items,name='items'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem')


]