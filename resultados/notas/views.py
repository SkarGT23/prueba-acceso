from django.shortcuts import render
from django.utils import timezone  # Importa timezone para obtener la fecha y hora actual
from .forms import NotasForm
from .models import Notas

def notas_view(request):
    resultado = None  # Inicializamos el resultado como None
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            # Obtener las notas desde el formulario
            matematicas_o_historia = form.cleaned_data['matematicas_o_historia']
            lengua_y_litertura = form.cleaned_data['lengua_y_litertura']
            idioma = form.cleaned_data['idioma']
            prueba_especifica = form.cleaned_data['prueba_especifica']

            # Calcular la nota media
            nota_media = (matematicas_o_historia + lengua_y_litertura + idioma + prueba_especifica) / 4

            # Crear una nueva instancia de Notas con la fecha automática
            nueva_nota = Notas(
                matematicas_o_historia=matematicas_o_historia,
                lengua_y_litertura=lengua_y_litertura,
                idioma=idioma,
                prueba_especifica=prueba_especifica,
                nota_media=nota_media,
                fecha=timezone.now()  # Asigna la fecha y hora actuales automáticamente
            )
            nueva_nota.save()  # Guarda el objeto en la base de datos

            # Mensajes de resultado según la nota media
            if nota_media >= 10:
                resultado = "We are the champions, my friends... (Nota muy alta)"
            elif 9 <= nota_media < 9.99:
                resultado = "Aprobado - ¡ qué vas a hacer con toda esta SENSUALIDAD !"
            elif 8 <= nota_media < 9:
                resultado = "Aprobado - ¡ DIOSSS, ASI SI. RESTRIEGASELO A TU MADRE EN TODA LA CARA POR DUDAR DE TI!"
            elif 7 <= nota_media < 8:
                resultado = "Aprobado - ¡ que vas a hacer con toda esta SENSUALIDAD !"
            elif 6 <= nota_media < 7:
                resultado = "Aprobado - ¡ como diría CRISTIANO ... SHUUUUUUUUUUUUU!!"
            elif 5 <= nota_media < 6:
                resultado = "Aprobado - ¡ abrio los ojos y por fin Vio a DIOS y comprendió que era bueno !"
            elif 4 <= nota_media < 5:
                resultado = "Suspenso - ¡ como diría MANOLO LAMA, ¡ Pero madre mía, qué tiro tan malo! Este elemento no le daría a una vaca ni chutando un melón a un metro !"
            elif 3 <= nota_media < 4:
                resultado = "Suspenso - Jugaste a cara o cruz y te salió la raya"
            elif 2 <= nota_media < 3:
                resultado = "Suspenso - No haber salido ayer"
            elif 1 <= nota_media < 2:
                resultado = "Suspenso - La isla de las tentaciones ayer bien, ¿no?"
            elif 0 < nota_media < 1:
                resultado = "Suspenso - ESPARTANOS!! ¿Cuál es vuestro oficio? ¡SALIR, SALIR, SALIR!"
            else:
                resultado = "Suspenso - No mereces vivir"

            # Renderizar la página con el resultado
            return render(request, 'notas/resultados.html', {'resultado': resultado, 'nota_media': nota_media})

    else:
        form = NotasForm()

    return render(request, 'notas/notas.html', {'form': form})

def listar_notas(request):
    # Obtener todas las notas almacenadas en la base de datos
    notas = Notas.objects.all()
    return render(request, 'notas/listar_notas.html', {'notas': notas})
