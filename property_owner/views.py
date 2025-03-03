from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group

# Create your views here.
@login_required
def index(request):
    return render(request, 'property.html')



property_owners = User.objects.filter(groups__name="property_owner")

# Print the results
for user in property_owners:
    print(user.username, user.email)