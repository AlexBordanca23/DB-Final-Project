# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(blank=False, null=True, max_length=255)
    last_name = models.CharField(blank=False, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'doctors'


class PatientContact(models.Model):
    patient_id = models.AutoField(primary_key=True, blank=False, null=False)
    email = models.CharField(blank=False, null=True, max_length=255)
    street_address = models.CharField(blank=False, null=True, max_length=255)
    city = models.CharField(blank=False, null=True, max_length=255)
    state = models.CharField(blank=False, null=True, max_length=255)
    zip = models.IntegerField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'patient_contact'


class PatientDoctors(models.Model):
    patient_id = models.AutoField(primary_key=True, blank=False, null=False)
    doctor = models.CharField(blank=False, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_doctors'


class PatientFinance(models.Model):
    patient = models.OneToOneField('PatientId', models.DO_NOTHING, db_column='Patient_ID', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    amount_due = models.DecimalField(db_column='Amount_due', max_digits=10, decimal_places=5, blank=False, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    ins_co = models.CharField(db_column='Ins_co', blank=False, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_finance'


class PatientHealth(models.Model):
    patient = models.OneToOneField('PatientId', models.DO_NOTHING, db_column='Patient_ID', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    current_smoker = models.BooleanField(db_column='Current_smoker', blank=False, null=True)  # Field name made lowercase.
    condition_1 = models.CharField(db_column='Condition_1', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_2 = models.CharField(db_column='Condition_2', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_3 = models.CharField(db_column='Condition_3', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_4 = models.CharField(db_column='Condition_4', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_5 = models.CharField(db_column='Condition_5', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_6 = models.CharField(db_column='Condition_6', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_7 = models.CharField(db_column='Condition_7', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_8 = models.CharField(db_column='Condition_8', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_9 = models.CharField(db_column='Condition_9', blank=False, null=True, max_length=255)  # Field name made lowercase.
    condition_10 = models.CharField(db_column='Condition_10', blank=False, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_health'


class PatientId(models.Model):
    patient_id = models.AutoField(db_column='Patient_ID', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', blank=False, null=True, max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', blank=False, null=True, max_length=255)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=False, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=False, null=True, max_length=255)  # Field name made lowercase.
    biol_sex = models.CharField(db_column='Biol_sex', blank=False, null=True, max_length=255)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='Ethnicity', blank=False, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_id'


class PatientVitals(models.Model):
    patient = models.OneToOneField(PatientId, models.DO_NOTHING, db_column='Patient_ID', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    last_height = models.DecimalField(db_column='Last_height', max_digits=10, decimal_places=5, blank=False, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    last_weight = models.DecimalField(db_column='Last_weight', max_digits=10, decimal_places=5, blank=False, null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    last_heartrate = models.IntegerField(db_column='Last_heartrate', blank=False, null=True)  # Field name made lowercase.
    last_systolic_bp = models.IntegerField(db_column='Last_systolic_BP', blank=False, null=True)  # Field name made lowercase.
    last_diastolic_bp = models.IntegerField(db_column='Last_diastolic_BP', blank=False, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_vitals'
