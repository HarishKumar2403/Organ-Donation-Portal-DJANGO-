from django.shortcuts import render,redirect
from django.contrib import messages
import re
from .models import *
import random
import requests
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    return render(request,'home.html')

def send_otp(request):
    if request.method == 'POST':
        PhoneNumber = request.POST.get("PhoneNumber")
        phone_pattern = re.compile(r'^\d{10}$')  
        if not phone_pattern.match(PhoneNumber):
            messages.error(request, "Please enter a valid phone number")
            return render(request, 'send_otp.html')
        if PhoneNumber:
            num = random.randint(1000, 9999)
            otp_num = str(num)

            # msg = "Your Otp for Donation Form Verification "
            # url = "https://www.fast2sms.com/dev/bulkV2"
            # payload = "message="+ otp_num +"&language=english&route=q&numbers=" + PhoneNumber
            # headers = {
            # 'authorization': "AteTGYEM6fnU3O5uKLIPzWcBvmyo4jwkpVaXiSH9Zh1CqNlsF0WXVjMZKxzSp3OBT50nckdyvsDEglfH",
            # 'Content-Type': "application/x-www-form-urlencoded",
            # 'Cache-Control': "no-cache",
            # }
            # response = requests.request("POST", url, data=payload, headers=headers)

            # print(response.text)
            # if response:        
            #     messages.success(request,"otp send")        
            #     return(redirect,'register')
           
            if otp_num:
                request.session['otp']=otp_num
                messages.success(request, f"OTP Sent: {otp_num}") 
                return redirect('register')  # Assuming you want to redirect to the register page after sending OTP
        else:
            messages.error(request, "Invalid Mobile number")
    return render(request, 'send_otp.html', {'otpp': 'send'})

def register(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        PhoneNumber = request.POST.get("PhoneNumber")
        CustomerEmail = request.POST.get("CustomerEmail")
        CustomerPassword = request.POST.get("CustomerPassword")

        # Validate email format
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(CustomerEmail):
            messages.error(request, "Please enter a valid email address")
            return render(request, 'register.html')

        # Validate phone number format
        phone_pattern = re.compile(r'^\d{10}$')
        if not phone_pattern.match(PhoneNumber):
            messages.error(request, "Please enter a valid phone number")
            return render(request, 'register.html')

        # Validate OTP
        entered_otp = request.POST.get('otp')
        if 'otp' in request.session:
            stored_otp = request.session['otp']
            if entered_otp == str(stored_otp):
                del request.session['otp']
                # Create user
                customer = Customer.objects.create(Name=Name, PhoneNumber=PhoneNumber,
                                                    CustomerEmail=CustomerEmail,
                                                    CustomerPassword=CustomerPassword)
                if customer:
                    messages.success(request, "User profile has been registered successfully! Please login to continue")
                    return redirect('home')
            else:
                messages.error(request, "Invalid OTP")
        else:
            messages.error(request, "OTP verification failed. Please try again.")
    
    return render(request, 'register.html')

def user_login(request):
    if request.session.has_key('username'):  
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get("Email")
            password = request.POST.get("CustomerPassword")
            session = Customer.objects.filter(CustomerEmail=email, CustomerPassword=password)
            if session.exists():
                user = session.first()
                request.session['username'] = user.CustomerEmail  
                request.session['user_id'] = user.id
                messages.success(request,'Login Successful!')                 
                return redirect('home')
            else:
                messages.error(request, 'Invalid Email or Password! Please Try Again')

    return render(request, 'login.html')

def edit_users(request, id):
    useredit = Customer.objects.get(id=id)
    if request.method == 'POST':
        Name = request.POST.get("Name")
        PhoneNumber = request.POST.get("PhoneNumber")
        CustomerEmail = request.POST.get("CustomerEmail")
        CustomerPassword = request.POST.get("CustomerPassword")
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(CustomerEmail):
            messages.error(request, "Please enter a valid email address")
            return render(request, 'home.html')

        phone_pattern = re.compile(r'^\d{10}$')  
        if not phone_pattern.match(PhoneNumber):
            messages.error(request, "Please enter a valid phone number")
            return render(request, 'home.html')

        useredit.Name = Name
        useredit.PhoneNumber = PhoneNumber
        useredit.CustomerEmail = CustomerEmail
        useredit.CustomerPassword = CustomerPassword
        useredit.save()
        if useredit:
            messages.success(request, "User profile has been updated successfully!")
            return redirect('home')
    return render(request, 'profile.html', {'useredit': useredit})

def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
        messages.success(request,'Logout Successful!')
    return redirect('user_login')


def user_admin(request):
    return render(request,'admin.html')
def page_404(request):
    return render(request,'error.html')

def donation_form(request):
    username=request.session['user_id']
    user_id=Customer.objects.get(id=int(username))
    if request.method=="POST":
        Name=request.POST.get('Name')
        Birthdate=request.POST.get('Birthdate')
        Gender=request.POST.get('Gender')
        Nationality=request.POST.get('Nationality')
        Bloodgroup=request.POST.get('Bloodgroup')
        Mobilenumber=request.POST.get('Mobilenumber')
        Email=request.POST.get('Email')
        Address=request.POST.get('address')
        Pancard=request.POST.get('pancard')
        Aadharcard=request.POST.get('aadharcard')
        News=request.POST.get('news')
        DonateType=request.POST.get('interest')
        Beforedeath=request.POST.get('beforedeath')
        Afterdeath=request.POST.get('afterdeath')
        Question1=request.POST.get('question1')
        Question2=request.POST.get('question2')
        Question3=request.POST.get('question3')
        Question4=request.POST.get('question4')
        Question5=request.POST.get('question5')
        Question6=request.POST.get('question6')
        Question7=request.POST.get('question7')
        Question8=request.POST.get('question8')
        Question9=request.POST.get('question9') 
        Question10=request.POST.get('question10')

        if DonateType:

            phone_pattern = re.compile(r'^\d{10}$')
            if not phone_pattern.match(Mobilenumber):
                messages.error(request, "Please enter a valid phone number")
                return render(request,'home.html')
            email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if not email_pattern.match(Email):
                messages.error(request, "Please enter a valid email address")
                return render(request,'home.html')
            questions = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10']
            if all([Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10]):
                no_answers_count = sum(1 for question in questions if request.POST.get(question) == 'No')
                total_questions = len(questions)

                # Calculate percentage eligibility
                percentage_eligible = (no_answers_count / total_questions) * 100

                # Check eligibility threshold
                eligibility_threshold = 75  # Adjust as needed
                if percentage_eligible >= eligibility_threshold:
                    record=DonationForm.objects.create(user=user_id,name=Name,birthdate=Birthdate,gender=Gender,nationality=Nationality,
                                                bloodgroup=Bloodgroup,mobilenumber=Mobilenumber,
                                                email=Email,address=Address,pancard=Pancard,aadharcard=Aadharcard,
                                                news=News,donate_type=DonateType,beforedeath=Beforedeath,afterdeath=Afterdeath,
                                                question1=Question1,question2=Question2,question3=Question3,
                                                question4=Question4,question5=Question5,question6=Question6,
                                                question7=Question7,question8=Question8,question9=Question9,question10=Question10)
                    if record:
                        messages.success(request,'Donation Form Submitted Successfully!')
                        return redirect('home')    
                else:
                    messages.error(request,'Your Form is not eligible')
                    return redirect('home')
            else:
                return redirect('page_404')

        else:
            return redirect('page_404')                


    return render(request,'donation_form.html')

def Hospital_login(request):
    if request.session.has_key('hospitalname'):  
        return redirect('Hospital_main')
    else:
        if request.method == 'POST':
            Hospital_Name = request.POST.get("Hospital_Name")
            Hospital_Password = request.POST.get("Hospital_Password")
            session = Hospital.objects.filter(hospital_name=Hospital_Name, password=Hospital_Password)
            if session.exists():
                user = session.first()
                request.session['hospitalname'] = user.hospital_name
                request.session['user_id'] = user.id
                                 
                return redirect('Hospital_main',id=user.id)
            else:
                messages.error(request, 'Invalid Name or Password! Please Try Again')
    return render(request,'Hospital_login.html')

def Hospital_main(request,id):
    hospital=Hospital.objects.get(id=id)
    donor=DonationForm.objects.all()
    
    data=DonationForm.objects.all()
    Name=request.POST.get('search_key')
    if Name!='' and Name is not None:
        data = data.filter(name__icontains=Name) or data.filter(donate_type__icontains=Name) or data.filter(gender__icontains=Name) or data.filter(beforedeath__icontains=Name) or data.filter(afterdeath__icontains=Name) or data.filter(bloodgroup__icontains=Name) or data.filter(mobilenumber__icontains=Name)
 
    context = {
        'data':data,
        'hospital':hospital,
        'donor':donor
                }
    return render(request,'hospital-main-page.html',context)

def Hospital_logout(request):
    if 'hospitalname' in request.session:
        del request.session['hospitalname']
        messages.success(request,'Logout Successful!')
    return redirect('home')

