from .base_serializer import BasePageSerializer
from . import AboutPage


class AboutPageSerializer(BasePageSerializer):
    class Meta:
        model = AboutPage
        fields = BasePageSerializer.Meta.fields

