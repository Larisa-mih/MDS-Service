from django.urls import path
from mds_service.apps import MdsServiceConfig
from mds_service.views import (
    BaseTemplateView,
    HomeTemplateView,
    AboutTheClinicTemplateView,
    ContactsTemplateView,
    DoctorListView,
    AppointmentListView,
    ServiceListView,
    AppointmentCreateView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentUpdateView,
)

app_name = MdsServiceConfig.name

urlpatterns = [
    path("", BaseTemplateView.as_view(), name="base"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path(
        "about_the_clinic/",
        AboutTheClinicTemplateView.as_view(),
        name="about_the_clinic",
    ),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("doctor/list/", DoctorListView.as_view(), name="doctor_list"),
    path("service/list/", ServiceListView.as_view(), name="service_list"),
    path("appointment/list/", AppointmentListView.as_view(), name="appointment_list"),
    path(
        "appointment/<int:pk>",
        AppointmentDetailView.as_view(),
        name="appointment_detail",
    ),
    path("appointment/new", AppointmentCreateView.as_view(), name="create_appointment"),
    path(
        "appointment/update/<int:pk>",
        AppointmentUpdateView.as_view(),
        name="update_appointment",
    ),
    path(
        "appointment/delete/<int:pk>",
        AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
]
