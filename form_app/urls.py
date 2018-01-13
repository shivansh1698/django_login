from django.conf.urls import url
from form_app import views

# template tagging
app_name = 'form_app'

urlpatterns = [
    url(r'^index',views.index,name = 'index'),
    url(r'^sample/',views.sample,name = 'sample'),
    url(r'^test/',views.test,name = 'test'),
    url(r'^log/',views.form_log,name='form_log'),
    url(r'^sign/',views.form_sign,name='form_sign'),
    url(r'^data/',views.read_data,name='read_data'),
    url(r'^user_logout',views.user_logout,name = 'user_logout')

]