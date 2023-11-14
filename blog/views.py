from django.shortcuts import render, get_object_or_404, redirect
from .models import Lieu, Animal
from .forms import MoveForm
from django.contrib import messages

def animal_list(request):
    animaux = Animal.objects.all()
    lieux = Lieu.objects.all()
    return render(request, 'blog/animal_list.html', {'animaux': animaux, 'lieux': lieux})

def post_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = animal.lieu
    form=MoveForm()
    if request.method == "POST":
        ancien_lieu = get_object_or_404(Lieu, id_lieu=animal.lieu.id_lieu)
        form = MoveForm(request.POST, instance=animal)
        if form.is_valid():
            form.save(commit=False)
            nouveau_lieu = get_object_or_404(Lieu, id_lieu=animal.lieu.id_lieu)
            if nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_lieu=="paturages" and animal.etat=='affame':
                animal.etat="repus"
                animal.save()
                nouveau_lieu.disponibilite="occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Votre cheval a bien été déplacé dans les paturages !')
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_lieu=="champs_d_entrainement" and animal.etat=='repus':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                animal.etat="fatigue"
                animal.save()
                nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Votre cheval a bien été déplacé dans le parcours d entrainement !')
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_lieu=="box_dodo" and animal.etat=='fatigue':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                animal.etat="endormi"
                animal.save()
                nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Votre cheval a bien été déplacé dans le box pour dormir !')
            elif nouveau_lieu.disponibilite=="libre" and nouveau_lieu.id_lieu=="litiere" and animal.etat=='endormi':
                ancien_lieu.disponibilite="libre"
                ancien_lieu.save()
                animal.etat="affame"
                animal.save()
                nouveau_lieu.disponibilite = "libre"
                nouveau_lieu.save()
                messages.add_message(request, messages.SUCCESS, 'Votre cheval a bien été déplacé au coin toilettes !')
            elif nouveau_lieu==ancien_lieu:
                messages.add_message(request, messages.WARNING, 'Votre cheval est déjà à cet endroit.')
            else :
                print('message')
                messages.add_message(request, messages.ERROR, 'Désolé, vous ne pouvez pas déplacer ce cheval à cet endroit.')
        return redirect('post_detail', id_animal=id_animal)
    else:
        form = MoveForm()
        return render(request,
                  'blog/post_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form})