from rest_framework import generics

from common.models.contact_us import ContactUs
from common.serializers import ContactUsListSerializers


class ContactUsListApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsListSerializers