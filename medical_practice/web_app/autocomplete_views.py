from dal import autocomplete
from .models import PatientId

class PatientIdAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = PatientId.objects.all()
        if self.q:
            qs = qs.filter(patient_id__icontains=self.q)
        return qs
