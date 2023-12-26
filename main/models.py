from django.db import models
import uuid

# Create your models here.
class MENU(models.Model):
    ID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    class Meta:
        db_table="menu"

class ROOM(models.Model):
    RoomNo = models.IntegerField(primary_key=True)
    Area = models.CharField(max_length=50, null=False)
    class Meta:
        db_table="room"

class PROGRAM(models.Model):
    ProgramID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    Name = models.CharField(max_length=20, null=False)
    AgeMin = models.IntegerField(null=False)
    AgeMax = models.IntegerField(null=False)
    class Meta:
        db_table="program"

class EXTRACURRICULAR(models.Model):
    ExtracurricularID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=30, null=False)
    Day = models.CharField(max_length=15, null=False)
    Hour = models.IntegerField(null=False)
    class Meta:
        db_table="extra_curricular"

class USERS(models.Model):
    UserID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Password = models.CharField(max_length=20, null=False)
    PhoneNumber = models.CharField(max_length=15, null=False)
    FirstName = models.CharField(max_length=20, null=False)
    LastName = models.CharField(max_length=20, null=False)
    Gender = models.CharField(max_length=10, null=False)
    Birthdate = models.DateField(null=False)
    Address = models.TextField(null=False)
    class Meta:
        db_table="users"

class CHILD(models.Model):
    UserID = models.OneToOneField(USERS, on_delete=models.CASCADE, primary_key=True)
    DadName = models.CharField(max_length=50)
    MomName = models.CharField(max_length=50)
    DadJob = models.CharField(max_length=20)
    MomJob = models.CharField(max_length=20)
    class Meta:
        db_table="child"

class STAFF(models.Model):
    UserID = models.OneToOneField(USERS, on_delete=models.CASCADE, primary_key=True)
    NIK = models.CharField(max_length=50)
    NPWP = models.CharField(max_length=50)
    BankAccount = models.CharField(max_length=50)
    BankName = models.CharField(max_length=50)
    class Meta:
        db_table="staff"

class CAREGIVER(models.Model):
    UserID = models.OneToOneField(STAFF, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        db_table="caregiver"

class CAREGIVER_CERTIFICATE(models.Model):
    UserID = models.ForeignKey(USERS, on_delete=models.CASCADE)
    CertificateNumber = models.CharField(max_length=20, null=True)
    CertificateName = models.CharField(max_length=20, null=True)
    CertificateYear = models.CharField(max_length=4, null=True)
    CertificateOrganizer = models.CharField(max_length=20, null=True)
    class Meta:
        unique_together = ('UserID', 'CertificateNumber', 'CertificateName', 'CertificateYear', 'CertificateOrganizer')
        db_table="caregiver_certificate"

