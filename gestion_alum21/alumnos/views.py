from django.shortcuts import render, redirect
from .forms import AlumnoForm

def alumno_nuevo(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_lista')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/alumno_form.html', {'form': form})
def alumno_lista(request):
    return 0
