from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def secret_page(request):
  return render(request, 'flatpages/default.html', {'flatpage': {'content': 'Секретная информация!'}})

def styled_page(request):
    return render(request, 'my_app/styled_page.html')
