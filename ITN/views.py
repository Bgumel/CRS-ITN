from django.shortcuts import render, redirect
from .forms import ITNDistributionForm, CustomUserCreationForm
from .models import ITNDistribution
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



#Homepage View
def Index(request):
    
    return render(request, "index.html", {})


#auth user creation
def register(request):
    if request.method == "POST":
        form =CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/login') 
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form":form})




#Distribution Form View
@login_required
def itn_distribution_view(request):
    if request.method == 'POST':
        form = ITNDistributionForm(request.POST)
        if form.is_valid():
            itn_distribution = form.save(commit=False)
            itn_distribution.distributor_id = request.user.id  # Set the distributor as the logged-in user
            itn_distribution.save()
            return redirect('/itn-distribution-success/')  # Redirect to a success page
    else:
        form = ITNDistributionForm()

    return render(request, 'itn_distribution_form.html', {'form': form})


##Distribution Success feedback
def itn_distribution_success(request):

    return render(request, 'itn_distribution_success.html', {})

#distribution View
@login_required
def distributions(request):
    # Filter ITN distributions for the logged-in user 
    distributions = ITNDistribution.objects.filter(distributor_id=request.user.id)
    
    return render(request, 'distributions.html', {'distributions': distributions})


#tech support page
@login_required
def support(request):
    return render(request, 'support.html')

