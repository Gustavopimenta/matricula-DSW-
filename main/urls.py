from django.contrib import admin
from django.urls import path
from aluno  import views
from hospedagem.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('aluno/editar/<int:id>/', views.AlunoEditar.as_view(), name='aluno_editar'),
    path('aluno/criar/', views.AlunoCriar.as_view(), name='aluno_criar'),
    path('aluno/remover/<int:id>/', views.AlunoRemover.as_view(), name='aluno_remover'),
    path('aluno/listar/', views.AlunoListar.as_view(), name='aluno_listar'),
    
    path('hospedagem/listar/', HospedagemList.as_view(), name='hospedagem_listar'),
    path('hospedagem/criar/', HospedagemCreate.as_view(), name='hospedagem_criar'),
    path('hospedagem/editar/<int:pk>/', HospedagemUpdate.as_view(), name='hospedagem_editar'),
    path('hospedagem/remover/<int:pk>/', HospedagemDelete.as_view(), name='hospedagem_remover'),
]