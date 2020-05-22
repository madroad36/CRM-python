from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', 					views.home, 		name = "home"),
    path('user/', 				views.userPage, 	name = "user-page"),
    path('products/', 			views.products, 	name = "products"),
    path('customers/<str:id>/', views.customers,	name = "customer"),
    

    path('create_order/<str:id>/',	views.createOrder, name = "create_order"),
    path('update_order/<str:id>/', 	views.updateOrder, name = "update_order"),
    path('delete_order/<str:id>/', 	views.deleteOrder, name = "delete_order"),

    path('register/', 	views.registerPage, 		name="register"),
	path('login/', 		views.loginPage, 			name="login"),
	path('logout/', 	views.logoutUser, 			name="logout"),

    path('setting/',    views.accountSettings,      name = "account"),


    # Password RESET Process
    path('reset_password/',              auth_views.PasswordResetView.as_view(),            name = "reset_password"),
    path('reset_password_sent/',         auth_views.PasswordResetDoneView.as_view(),        name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',      auth_views.PasswordResetConfirmView.as_view(),     name = "password_reset_confirm"),
    path('reset_password_complete/',     auth_views.PasswordResetCompleteView.as_view(),    name = "password_reset_complete"),
]

