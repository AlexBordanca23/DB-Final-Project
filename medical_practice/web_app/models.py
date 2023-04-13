from django.db import models

class PatientId(models.Model):
    patient_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    biol_sex = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=255)
    dob = models.DateField()

    class Meta:
        managed = True
        db_table = 'patient_id'

class Doctors(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'doctors'

class PatientContact(models.Model):
    patient = models.OneToOneField(PatientId, primary_key=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'patient_contact'

class PatientDoctors(models.Model):
    patient = models.ForeignKey(PatientId, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'patient_doctors'

class PatientFinance(models.Model):
    patient = models.OneToOneField(PatientId, primary_key=True, on_delete=models.CASCADE)
    ins_co = models.CharField(max_length=255)
    amount_due = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = True
        db_table = 'patient_finance'

class PatientHealth(models.Model):
    patient = models.ForeignKey(PatientId, on_delete=models.CASCADE)
    currrent_smoker = models.BooleanField()
    condition_1 = models.CharField(max_length=255)
    condition_2 = models.CharField(max_length=255)
    condition_3 = models.CharField(max_length=255)
    condition_4 = models.CharField(max_length=255)
    condition_5 = models.CharField(max_length=255)
    condition_6 = models.CharField(max_length=255)
    condition_7 = models.CharField(max_length=255)
    condition_8 = models.CharField(max_length=255)
    condition_9 = models.CharField(max_length=255)
    condition_10 = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'patient_health'

class PatientVitals(models.Model):
    patient = models.ForeignKey(PatientId, on_delete=models.CASCADE)
    height_in = models.DecimalField(max_digits=5, decimal_places=2)
    weight_lb = models.DecimalField(max_digits=5, decimal_places=2)
    bp_systolic = models.IntegerField()
    bp_diastolic = models.IntegerField()
    heart_rate = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'patient_vitals'
