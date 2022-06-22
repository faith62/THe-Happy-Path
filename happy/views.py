from rest_framework.viewsets import ModelViewSet
from .models import Contact
from .serializers import ContactSerializer

#modelviewset already has mixins for CRUD
class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()