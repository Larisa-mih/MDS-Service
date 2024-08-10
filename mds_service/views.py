from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)
from mds_service.forms import AppointmentAddForm
from mds_service.models import Doctor, Appointment, Service
from users.models import User


class HomeTemplateView(TemplateView):
    """Контроллер отображения главной страницы"""

    template_name = "mds_service/home.html"


class AboutTheClinicTemplateView(TemplateView):
    """Контроллер отображения страницы 'О клинике'"""

    template_name = "mds_service/about_the_clinic.html"


class ContactsTemplateView(TemplateView):
    """Контроллер отображение страницы с контактами клиники"""

    template_name = "mds_service/contacts.html"


class DoctorListView(ListView):
    """Контроллер отображение всех врачей"""

    model = Doctor

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        doctors = Doctor.objects.all()
        context_data["object_list"] = doctors
        return context_data


class ServiceListView(ListView):
    """Контроллер отображение всех услуг, на которые можно записаться"""

    model = Service

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        services = Service.objects.all()
        context_data["object_list"] = services
        return context_data


class AppointmentListView(ListView):
    """Контроллер отображение всех записей на приём/УЗИ/МРТ/Анализы"""

    model = Appointment
    template_name = "mds_service/appointment_list.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context_data["object_list"] = appointments
        return context_data


class AppointmentDetailView(DetailView):
    """Контроллер отображения детального просмотра записи на приём//УЗИ/МРТ/Анализы"""

    model = Appointment
    template_name = "mds_service/appointment_detail.html"
    context_object_name = "objects_list"


class AppointmentCreateView(CreateView):
    """Контроллер создания записи на приём/УЗИ/МРТ/Анализы"""

    model = Appointment
    template_name = "mds_service/appointment_create.html"
    form_class = AppointmentAddForm
    success_url = reverse_lazy("mds_service:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        appointment_form_set = inlineformset_factory(
            User, Appointment, form=AppointmentAddForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = appointment_form_set(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = appointment_form_set(instance=self.object)
        return context_data


class AppointmentUpdateView(UpdateView):
    """Контроллер редактирования записи на приём/УЗИ/МРТ/Анализы"""

    model = Appointment
    template_name = "mds_service/appointment_update_form.html"
    form_class = AppointmentAddForm
    success_url = reverse_lazy("mds_service:home")


class AppointmentDeleteView(DeleteView):
    """Контроллер удаления записи на приём/УЗИ/МРТ/Анализы"""

    model = Appointment
    template_name = "mds_service/appointment_confirm_delete.html"
    success_url = reverse_lazy("mds_service:home")
