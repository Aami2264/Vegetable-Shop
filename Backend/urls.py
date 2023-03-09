from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('AddAdmin/',views.AddAdmin,name="AddAdmin"),
    path('saveadmin/',views.saveadmin,name="saveadmin"),
    path('displayadmin/',views.displayadmin,name="displayadmin"),
    path('edit/<int:dataid>',views.edit,name="edit"),
    path('update/<int:dataid>',views.update,name="update"),
    path('delete/<int:dataid>',views.delete,name="delete"),
    path('AddCategory/',views.AddCategory,name="AddCategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('DisplayCategory/',views.DisplayCategory,name="DisplayCategory"),
    path('Editcategory/<int:dataid>',views.Editcategory,name="Editcategory"),
    path('updatecategory/<int:dataid>',views.updatecategory,name="updatecategory"),
    path('Deletecategory/<int:dataid>',views.Deletecategory,name="Deletecategory"),
    path('AddProducts/',views.AddProducts,name="AddProducts"),
    path('Saveproducts/',views.Saveproducts,name="Saveproducts"),
    path('DisplayPro/',views.DisplayPro,name="DisplayPro"),
    path('EditProduct/<int:dataid>',views.EditProduct,name="EditProduct"),
    path('Updateproduct/<int:dataid>',views.Updateproduct,name="Updateproduct"),
    path('DeleteProduct/<int:dataid>', views.DeleteProduct, name="DeleteProduct"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('Msgdisplay/',views.Msgdisplay,name="Msgdisplay"),
    path('DeleteMsg/<int:dataid>',views.DeleteMsg,name="DeleteMsg")
]