from django.db import models



class Customer(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=10)
    CustomerEmail = models.EmailField(unique=True)
    CustomerPassword = models.CharField(max_length=50)
    
    def __str__(self):
        return self.CustomerEmail
    
class DonationForm(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    #Step 1
    name=models.CharField(max_length=100)
    birthdate=models.DateField()
    gender=models.CharField(max_length=6)
    nationality=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    pancard=models.CharField(max_length=20)
    aadharcard=models.CharField(max_length=24)
    news=models.CharField(max_length=100)
    #Step 2
    DONATE_CHOICES = [
        ('Before Dead', 'Before Dead'),
        ('After Dead', 'After Dead')
    ]
    donate_type=models.CharField(max_length=12, choices=DONATE_CHOICES)
    beforedeath=models.CharField(max_length=100,null=True,blank=True)
    afterdeath=models.CharField(max_length=100,null=True,blank=True)
    #Step 3
    MEDICAL_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    question1=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question2=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question3=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question4=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question5=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question6=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question7=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question8=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question9=models.CharField(max_length=12, choices=MEDICAL_CHOICES)
    question10=models.CharField(max_length=12, choices=MEDICAL_CHOICES)

    def __str__(self):
        return self.name
class Hospital(models.Model):
    Donor=models.ForeignKey(DonationForm,on_delete=models.CASCADE,null=True,blank=True)
    hospital_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.hospital_name