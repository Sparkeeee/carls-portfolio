from django.urls import path
from . import views
from .views import DashboardView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView

app_name = 'main'

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('portfolio/add/', PortfolioCreateView.as_view(), name='portfolio_add'),
    path('portfolio/<int:pk>/update/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('portfolio/<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]