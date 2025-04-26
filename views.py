from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserRegisterForm, ConsultationRequestForm
from .models import ConsultationRequest

def home(request):
    slider_images = [
        'img/slider/slide1.jpg',
        'img/slider/slide2.jpg',
        'img/slider/slide3.jpg',
     
    ]
    return render(request, 'PlotnikovApp/home.html', {
        'slider_images': slider_images
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'PlotnikovApp/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            return redirect('profile')
    else:
        form = ConsultationRequestForm()
    
    consultations = ConsultationRequest.objects.filter(user=request.user)
    return render(request, 'PlotnikovApp/profile.html', {
        'form': form,
        'consultations': consultations
    })

@staff_member_required
def admin_panel(request):
    consultations = ConsultationRequest.objects.all()
    return render(request, 'PlotnikovApp/admin_panel.html', {
        'consultations': consultations
    })

@staff_member_required
def update_status(request, pk):
    consultation = ConsultationRequest.objects.get(pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        consultation.status = new_status
        if new_status == 'canceled':
            consultation.cancel_reason = request.POST.get('cancel_reason', '')
        consultation.save()
        return redirect('admin_panel')
    return render(request, 'PlotnikovApp/update_status.html', {
        'consultation': consultation
    })