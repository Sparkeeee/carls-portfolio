from django.urls import path, include
from . import views
from .views import PortfolioCreateView, portfolio_update_view, PortfolioDeleteView, PortfolioDataView, PortfolioDetailView
from .views import dashboard_view
from .views import custom_login

app_name = 'main'

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('accounts/', include('allauth.urls')),
	path('login/', custom_login, name='login'),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('dashboard/', dashboard_view, name='dashboard'),
    path('portfolio/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
	path('portfolio/data/<int:portfolio_id>/', PortfolioDataView.as_view(), name='portfolio_data'),
	path('portfolio/<int:portfolio_id>/update/', portfolio_update_view, name='portfolio_update'),
    path('portfolio/<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]