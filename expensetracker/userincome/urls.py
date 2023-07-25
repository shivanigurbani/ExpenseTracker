from .import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='income'),
    path('add-income',views.add_income,name="addincome"),
    path('edit/<int:id>',views.income_edit,name="income-edit"),
     path('delete/<int:id>',views.delete_income,name="income-delete"),
     path('search-income', csrf_exempt(views.search_income),
         name="search_income"),
    path('income_source_summary', views.income_source_summary,
         name="income_source_summary"),
    path('userincome',views.userincome_view,name="userincome")
    
]
