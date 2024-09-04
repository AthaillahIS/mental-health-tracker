from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275683',
        'name': 'Athaillah Sifa Tanudatar',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)