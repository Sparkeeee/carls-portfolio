from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ContactForm, UpdatePortfoliosForm, PortfolioForm
from .models import UserProfile, Blog, Portfolio, Testimonial, Certificate

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('main:home')  # Redirect to the home page after login
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.filter(is_active=True)
        context["certificates"] = Certificate.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.filter(is_active=True)
        context["portfolio"] = Portfolio.objects.filter(is_active=True)
        return context

class ContactView(CreateView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. I will be in touch soon.')
        return super().form_valid(form)

class PortfolioView(ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

from .forms import PortfolioForm

def dashboard_view(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'create':
            form = PortfolioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Portfolio item created successfully.')
                return redirect('main:dashboard')
        elif operation == 'update':
            portfolio_id = request.POST.get('portfolio_id')
            portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
            form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
            if form.is_valid():
                form.save()
                messages.success(request, 'Portfolio item updated successfully.')
                return redirect('main:dashboard')
    else:
        form = PortfolioForm()
    portfolios = Portfolio.objects.all()
    return render(request, 'main/dashboard.html', {'portfolios': portfolios, 'form': form})


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['name', 'description', 'body', 'url', 'image']
    template_name = 'main/dashboard.html'  # Create a new template for the form
    success_url = reverse_lazy('main:portfolio')  # Redirect to the portfolio page after successful creation

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def portfolio_update_view(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            # Redirect to dashboard or display a success message
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'main/portfolio_update_modal.html', {'form': form, 'portfolio': portfolio})

class PortfolioDataView(View):
    def get(self, request, portfolio_id):
        portfolio = Portfolio.objects.get(pk=portfolio_id)
        data = {
            'name': portfolio.name,
            'description': portfolio.description,
            'body': portfolio.body,
            'url': portfolio.url,
            
            # Include other fields as necessary
        }
        return JsonResponse(data)

class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = Portfolio
    success_url = reverse_lazy('main:dashboard')  # Redirect to the portfolio page after successful deletion

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"

class BlogView(ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = "main/blog-detail.html"

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'], is_active=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj