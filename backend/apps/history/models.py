from django.db import models
from apps.doctor.models import Doctor
from apps.register.models import Register
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class History(models.Model):
    history_id = models.BigAutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    register = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)

    consultation_reason = models.TextField(null=True)
    current_illness = models.TextField(null=True)

    # System check
    head_system = models.TextField(default="Sin alteraciones", blank=True)
    eyes_system = models.TextField(default="Sin alteraciones", blank=True)
    otolaryngology_system = models.TextField(default="Sin alteraciones", blank=True)
    neck_system = models.TextField(default="Sin alteraciones", blank=True)
    chest_system = models.TextField(default="Sin alteraciones", blank=True)
    cardiac_system = models.TextField(default="Sin alteraciones", blank=True)
    pulmonary_system = models.TextField(default="Sin alteraciones", blank=True)
    digestive_system = models.TextField(default="Sin alteraciones", blank=True)
    genitourinary_system = models.TextField(default="Sin alteraciones", blank=True)
    central_nervous_system = models.TextField(default="Sin alteraciones", blank=True)
    skin_system = models.TextField(default="Sin alteraciones", blank=True)
    extremities_system = models.TextField(default="Sin alteraciones", blank=True)
    other_system = models.TextField(default="Sin alteraciones", blank=True)

    # Vital signs
    temperature = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    systolic_pressure = models.PositiveIntegerField(null=True, blank=True)
    diastolic_pressure = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True,
        validators=[
            MinValueValidator(20),
            MaxValueValidator(220)
        ]
    )
    respiratory_rate = models.IntegerField(null=True,
        validators=[
            MinValueValidator(12),
            MaxValueValidator(25)
        ]
    )
    weight = models.FloatField(null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )
    height = models.FloatField(null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3)
        ]
    )
    imc = models.FloatField(null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )
    abdominal_perimeter = models.FloatField(null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )
    head_perimeter = models.FloatField(null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )

    # Physical Exam
    consciousness_status = models.TextField(default="Sin alteraciones", blank=True)
    respiratory_status = models.TextField(default="Sin alteraciones", blank=True)
    hydration_status = models.TextField(default="Sin alteraciones", blank=True)
    general_status = models.TextField(default="Sin alteraciones", blank=True)
    physical_examination = models.TextField(default="Sin alteraciones", blank=True)

    #Key Findings
    head_findings = models.TextField(default="Sin alteraciones", blank=True)
    eyes_findings = models.TextField(default="Sin alteraciones", blank=True)
    otolaryngology_findings = models.TextField(default="Sin alteraciones", blank=True)
    mouth_findings =  models.TextField(default="Sin alteraciones", blank=True)
    neck_findings =  models.TextField(default="Sin alteraciones", blank=True)
    chest_findings = models.TextField(default="Sin alteraciones", blank=True)
    abdominal_findings = models.TextField(default="Sin alteraciones", blank=True)
    genitourinary_findings = models.TextField(default="Sin alteraciones", blank=True)
    central_nervous_findings = models.TextField(default="Sin alteraciones", blank=True)
    skin_findings = models.TextField(default="Sin alteraciones", blank=True)
    extremities_findings = models.TextField(default="Sin alteraciones", blank=True)
    mental_findings = models.TextField(default="Sin alteraciones", blank=True)
    other_findings = models.TextField(default="Sin alteraciones", blank=True)

    #Analysis and conduct
    analysis = models.TextField(default="Sin alteraciones", blank=True)
    diagnosis = models.TextField(default="Sin alteraciones", blank=True)
    follow_up_plan = models.TextField(blank=True)
    clinical_orders = models.TextField(default="Sin alteraciones", blank=True)
    family_history = models.TextField(default="Sin alteraciones", blank=True)
    personal_history = models.TextField(default="Sin alteraciones", blank=True)
    patient_progress = models.TextField(default="Sin alteraciones", blank=True)

    #General info
    issue_date = models.DateTimeField(auto_now=True)

    """
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    weight = models.FloatField(
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(200)
        ]
    )
    height = models.FloatField(
        validators=[
            MinValueValidator(0.5),
            MaxValueValidator(3)
        ]
    )
    heart_rate = models.IntegerField(
        validators=[
            MinValueValidator(20),
            MaxValueValidator(220)
        ]
    )
    respiratory_rate = models.IntegerField(
        validators=[
            MinValueValidator(12),
            MaxValueValidator(25)
        ]
    )
    key_findings = models.TextField(null=True)
    main_diagnostic = models.TextField(null=True)
    differential_diagnostic = models.TextField(null=True)
    requested_exams = models.TextField(null=True)
    programmed_procedures = models.TextField(null=True)
    interconsultation = models.TextField(null=True)
    follow_up_recommendations = models.TextField(null=True)
    disability = models.TextField(null=True)
    follow_up_plan = models.TextField(null=True)
    prescription_details = models.TextField(null=True)
    send_email = models.BooleanField(default=False)
    cause_consultation = models.CharField(max_length=2, null=True)
    main_diagnostic_code = models.CharField(max_length=25, null=True)
    secondary_diagnostic_code = models.CharField(max_length=25, null=True)
    third_diagnostic_code = models.CharField(max_length=25, null=True)
    fourth_diagnostic_code = models.CharField(max_length=25, null=True)
    service_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    income_concept = models.CharField(max_length=2, null=True)
    payment_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    fev_number = models.CharField(max_length=2, null=True)
    previous_diseases = models.TextField(null=True)
    previous_surgeries = models.TextField(null=True)
    hospitalization = models.TextField(null=True)
    allergies = models.TextField(null=True)
    medicines = models.TextField(null=True)
    immunization = models.TextField(null=True)
    gynecologic_conditions = models.TextField(null=True)
    obstetric_conditions = models.TextField(null=True)
    psychiatric_conditions = models.TextField(null=True)
    genetic_diseases = models.TextField(null=True)
    vascular_diseases = models.TextField(null=True)
    """

    class Meta:
        db_table = 'history'

    def __str__(self):
        return f"History {self.history_id}"
