from django.forms import ModelForm

from mds_service.models import Doctor, Appointment


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "current_version":
                field.widget.attrs["class"] = "form-control"


class DoctorForm(StyleMixin, ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class AppointmentAddForm(ModelForm):

    class Meta:
        model = Appointment
        fields = "__all__"
