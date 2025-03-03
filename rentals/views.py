from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check user role and redirect accordingly
            if user.is_superuser:  # SA (Super Admin)
                return redirect('/superadmin')
            elif user.groups.filter(name='PO').exists():  # PO (Property Owner)
                return redirect('property_owner')
            else:
                return redirect('index')  # Default fallback
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def sa_dashboard(request):
    property_owners = User.objects.filter(groups__name="property_owner")
    return render(request, "superadmin.html", {"property_owners": property_owners})

def add_property_owner(request):
    """Dynamically add a user to the property_owner group."""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Add user to property_owner group
        property_owner_group, created = Group.objects.get_or_create(name="property_owner")
        user.groups.add(property_owner_group)
        user.save()

        # Return JSON response for AJAX success
        return JsonResponse({"message": f"User {username} added to Property Owner group", "username": username})

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def superadmin(request):
    return render(request, 'superadmin.html')

@login_required
def property_owner(request):
    return render(request, 'property.html')


def logout_view(request):
    logout(request)
    return redirect('/')