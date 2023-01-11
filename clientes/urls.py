from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_user', views.create_user, name='create_user'),
    path('cadastro_cliente/new/', views.cadastrar_cliente, name='cadastro_cliente' ),
    path('listar_agenda', views.listar_agendas, name='listar_agenda'),
    path('detalhar_agenda/<int:id>/', views.detalhar_agenda, name='detalhar_agenda'),
    path('marcar_consulta/<int:id>/<int:pk>/', views.marcar_consulta, name='marcar_consulta'),
    path('area_cliente/<int:id>/',views.area_do_cliente, name= 'area_cliente'),
    path('autenticar_administrador', views.autenticar_administrador,name='autenticar_administrador'),
    path('administracao/<int:id>/',views.administracao, name='administracao'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),

]