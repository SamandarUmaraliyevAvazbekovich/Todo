from .views import *
from django.urls import path

urlpatterns = [
	path('',home,name='home'),
	path('qosh/',qosh,name='qosh'),
	path('oqi/<int:oqi_id>/',oqi,name='oqi'),
	path('del/<int:del_id>/',delete,name='del'),
	path('edit/<int:edit_id>/',edit,name='edit')


]