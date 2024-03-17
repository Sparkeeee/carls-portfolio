from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib import messages
from . forms import ContactForm
from django.views.generic import TemplateView
from django.views import generic
from .models import  (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView

# Create your views here.
class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. I will be in touch soon.')
        return self.success_url


class PortfolioView(LoginRequiredMixin, generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'main/dashboard.html'
    form_class='UpdatePortfoliosForm'
    success_url = "main/portfolio.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The portfolio item is uploaded.')
        return self.success_url

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['name', 'description', 'body', 'url', 'image']
    template_name = 'main/portfolio_form.html'  # Create a new template for the form
    success_url = reverse_lazy('main:portfolio')  # Redirect to the portfolio page after successful creation

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    fields = ['name', 'description', 'body', 'url', 'image']
    template_name = 'main/portfolio_form.html'  # Use the same template for updating
    success_url = reverse_lazy('main:portfolio')  # Redirect to the portfolio page after successful update

class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = Portfolio
    success_url = reverse_lazy('main:portfolio')  # Redirect to the portfolio page after successful deletion

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"



class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10
    
    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"