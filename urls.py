
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path('login/', views.login),
    path('add_design/',views.add_design),
    path('add_design_post/',views.add_design_post),
    path('add_post/',views.add_post),
    path('add_post_post/', views.add_post_post),
    path('viewdesign/',views.viewdesign),
    path('viewdesign_post/', views.viewdesign_post),
    path('edit_design/<id>', views.edit_design),
    path('edit_design_post/', views.edit_design_post),
    path('addcategory/',views.addcategory),
    path('addcategory_post/',views.addcategory_post),
    path('view_category/', views.view_category),
    path('view_category_post/',views.view_category_post),
    path('edit_category/<id>', views.edit_category),
    path('edit_category_post/', views.edit_category_post),
    path('addproduct/', views.addproduct),
    path('view-product/', views.view_product),
    path('view-product_post/', views.view_product_post),
    path('change_password/', views.change_password),
    path('change_password_post/', views.change_password_post),
    path('edit_post/<id>', views.edit_post),
    path('edit_post_post/', views.edit_post_post),
    path('view_orders/', views.view_orders),
    path('view_orders_post/', views.view_orders_post),
    path('view_post/', views.view_post),
    path('view_post_post/',views.view_post_post),
    path('verifi_orders/<id>',views.verifi_orders),
    path('view_users/', views.view_users),
    path('view_users_post/', views.view_users_post),
    path('verifycustomised_orders/<id>',views.verifycustomised_orders),
    path('view_verifiedorders/', views.view_verifiedorders),
    path('view_verifiedorders_post/', views.view_verifiedorders_post),
    path('viewcustomised_order/', views.viewcustomised_order),
    # path('viewcustomised_order/', views.viewcustomised_order),
    path('viewcustomised_order_post/', views.viewcustomised_order_post),
    path('viewrating/', views.viewrating),
    path('viewrating_post/', views.viewrating_post),
    path('viewverified_customisedorder/', views.viewverified_customisedorder),
    path('viewverified_customisedorder_post/', views.viewverified_customisedorder_post),
    path('choose_category/', views.choose_category),
    path('choose_category_post/', views.choose_category_post),

    path('register/', views.register),
    path('register_post/', views.register_post),
    path('send_review/', views.send_review),
    path('send_review_post/', views.send_review_post),
    path('delete_category/<id>',views.delete_category),
    path('delete_design/<id>',views.delete_design),
    path('delete_post/<id>',views.delete_post),

    path('AddAmounttocustomisedproduct/<id>',views.AddAmounttocustomisedproduct),
    path('AddAmounttocustomisedproduct_post/',views.AddAmounttocustomisedproduct_post),



    # path('send_customized_request/', views.sendcustomized_request),
    path('view_customizedrequeststatus/', views.view_customizedrequeststatus),
    path('view_customizedrequeststatus_post/', views.view_customizedrequeststatus_post),

    path('viewverifiedCustomiserequest_get/', views.viewverifiedCustomiserequest_get),



    path('view_orderstatus/',views.view_orderstatus),
    path('view_orderstatus_post/',views.view_orderstatus_post),
    path('viewposts_post/',views.viewposts_post),
    path('viewposts_post_post/',views.viewposts_post_post),
    path('view_product/', views.view_product),
    path('view_product_post/', views.view_product_post),
    path('adminhome/',views.home),
    path('home_user/',views.home_user),
    path('login_post/',views.login_post),
    path('view_profile/', views.view_profile),
    path('sendcustomized_request/', views.sendcustomized_request),
    path('edit_profile/', views.edit_profile),
    path('edit_profilepost/', views.edit_profilepost),
    path('send_review_post/<id>', views.send_review_post),
    path('view_review/<id>', views.view_review),
    path('send_review/<id>', views.send_review),
    path('userviewdesign/<id>',views.userviewdesign),
    path('send_order/<id>', views.send_order),
    path('send_order_post/', views.send_order_post),
    path('choose_category/', views.choose_category),
    path('choose_category_post/', views.choose_category_post),
    path('raz_pay/<amount>/<id>', views.raz_pay),
    path('userviewdesign<id>', views.viewdesign),
    path('viewposts_post<id>',views.viewposts_post),
    path('viewposts_post_post',views.viewposts_post_post),
    path('addCustomisedproduct_post/', views.addCustomisedproduct_post),
    path('edit_cust_product/<id>', views.edit_cust_product),
    path('edit_Customised_product/', views.edit_Customised_product),
    path('delete_Customised_product/<id>', views.delete_Customised_product),

]

