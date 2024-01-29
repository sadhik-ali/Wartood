from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import (
    BangaloreStone,
    Category,
    Contact,
    Email,
    Enquiry,
    EnquiryForm,
    Project,
    ServiceImage,
    TandurStone,
    Update,
    kadappaStone,
    BeforeAfter,
    Testimonial,
)

# Create your views here.


def index(request):
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    context = {
        "is_index": True, 
        "updates": Update.objects.all(),
        "before_after": BeforeAfter.objects.all(),
        "testimonial": Testimonial.objects.all()
               }
    return render(request, "web/index.html", context)


def about(request):
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    context = {
        "testimonial": Testimonial.objects.all()
               }
    return render(request, "web/about.html", context)


def blog(request):
    context = {"update": Update.objects.all()}
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    return render(request, "web/blog.html", context)


def blogdetails(request, id):  # Add the 'id' parameter here
    context = {
        "update": Update.objects.get(id=id),
    }
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    return render(request, "web/blogdetails.html", context)


def contact(request):
    if request.method == "POST":
        email = request.POST.get("start_email")
        if email:
            Email.objects.create(email=email)

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name:
            Contact.objects.create(
                name=name, email=email, subject=subject, message=message
            )

    return render(request, "web/contact.html")


def project(request):
    context = {"projects": Project.objects.all(), "category": Category.objects.all()}
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    return render(request, "web/project.html", context)


def service(request):
    context = {"enquiry": Enquiry.objects.all()}
    if request.method == "POST":
        email = request.POST.get("start_email")
        order_6 = Email(email=email)
        order_6.save()
    return render(request, "web/service.html", context)


def servicedetails(request, id):
    ServiceImage.objects.all()
    context = {
        "enquiry": Enquiry.objects.get(id=id),
    }
    if request.method == "POST":
        if "subscribe" in request.POST:
            email = request.POST.get("start_email")
            if email:
                pass
        else:
            if request.method == "POST":
                Product = request.POST.get("Product")
                Name = request.POST.get("Name")
                Phone = request.POST.get("Phone")
                Message = request.POST.get("Messege")

            if Name:
                EnquiryForm.objects.create(
                    Product=Product, Name=Name, Phone=Phone, Message=Message
                )

            # Whatsapp Enquiry
            phone_number = "918086111003"
            starting_message = "Enquiry:\n\n"
            text = f"{starting_message}Product: {Product}\nName: {Name}\nPhone: {Phone}\nMessage: {Message}"
            whatsapp_url = f"https://wa.me/{phone_number}?text={text}"
            return HttpResponseRedirect(whatsapp_url)

    return render(request, "web/servicedetails.html", context)


def stone(request):
    context = {
        "tandurs": TandurStone.objects.all(),
        "kadappas": kadappaStone.objects.all(),
        "bangalores": BangaloreStone.objects.all(),
        "s": Enquiry.objects.all(),
    }
    if request.method == "POST":
        if "subscribe" in request.POST:
            email = request.POST.get("start_email")
            if email:
                pass
        else:
            if request.method == "POST":
                Product = request.POST.get("Product")
                Name = request.POST.get("Name")
                Phone = request.POST.get("Phone")
                Message = request.POST.get("Messege")

            if Name:
                EnquiryForm.objects.create(
                    Product=Product, Name=Name, Phone=Phone, Message=Message
                )

            # Whatsapp Enquiry
            phone_number = "918086111003"
            starting_message = "Enquiry:\n\n"
            text = f"{starting_message}Product: {Product}\nName: {Name}\nPhone: {Phone}\nMessage: {Message}"
            whatsapp_url = f"https://wa.me/{phone_number}?text={text}"
            return HttpResponseRedirect(whatsapp_url)

    return render(request, "web/stone.html", context)
