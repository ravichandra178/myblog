from myapp.views import index,detail,CreateBlog,like

from django.urls import path

app_name = 'myapp'

urlpatterns = [
	path('',index,name = 'index'),
	path('blog/<int:pk>/',detail,name = 'detail'),
	path('create/',CreateBlog.as_view(),name = 'create'),
	path('ajax/likes/',like,name = 'like'),
	]