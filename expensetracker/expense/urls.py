from .import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_expense,name="addexpenses"),
    path('edit/<int:id>',views.expense_edit,name="expense-edit"),
     path('delete/<int:id>',views.delete_expense,name="expense-delete"),
     path('search-expenses', csrf_exempt(views.search_expenses),
         name="search_expenses"),
    path('expense_category_summary', views.expense_category_summary,
         name="expense_category_summary"),
    path('stats',views.stats_view,name="stats")
    
    
]
