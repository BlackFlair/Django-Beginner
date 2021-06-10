from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PhoneBook.models import PhoneBook


# Create your views here.

# id

@csrf_exempt
def display(request):
    phonebook = PhoneBook.objects.all()

    # ---------- SEARCH ----------
    if 'searchBtn' in request.POST:
        search = request.POST.get('search')
        if search:
            phonebook = PhoneBook.objects.filter(name=search)

    # ---------- EDIT ----------
    elif request.POST.get('editBtn')=='Edit':
        global _id
        _id = request.POST.get('_edit')
        print("ID in update request: ", _id)

        return redirect('/update')

    # ---------- DELETE ----------
    elif request.POST.get('deleteBtn')=='Delete':
        _id = request.POST.get('delete')
        print("ID in delete request: ", _id)
        PhoneBook.objects.filter(id=_id).delete()

        return redirect('/display')

    return render(request, 'display.html', {'phonebook':phonebook})


@csrf_exempt
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        altPhone = request.POST.get('altPhone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        PhoneBook.objects.create(name=name, phone=phone, altPhone=altPhone, email=email, address=address)

        return redirect('/display')

    return render(request, 'add.html')


@csrf_exempt
def update(request):
    print("ID in update(): ", _id)
    contact = PhoneBook.objects.filter(id=_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        altPhone = request.POST.get('altPhone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        PhoneBook.objects.filter(id=_id).update(name=name, phone=phone, altPhone=altPhone, email=email, address=address)

        return redirect('/display')

    return render(request, 'update.html', {'contact':contact[0]})
