from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # Customer Orders    
    path('orders/<int:itemid>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),

    # Updating Customer Orders
    path('updorders/<int:orderid>/<int:itemid>/', views.UpdateOrders, name='updorders'),

    # Customer Rating and Feedback
    path('crf/<int:itemid>/<int:pc>/', views.CusRatFeedView, name='crf'),

    # Updating Customer Ratings and Feedbacks
    path('updcrf/<int:detailid>/<crfid>/', views.UpdateCRF, name='updcrf'),

    # Deleting Customer Ratings and Feedbacks
    path('delcrf/<int:detailid>/<int:crfid>/', views.DeleteCRF, name='delcrf'),

    # paypal checkout button
    path('buy/<int:amt>/<int:qnt>/', views.Payment, name='buy'),

    # paypal on approve
    path('oa/', views.OnApprove, name='oa'),

    # paypal payment success
    path('ps/', views.PaymentSuccess, name='ps'),
]