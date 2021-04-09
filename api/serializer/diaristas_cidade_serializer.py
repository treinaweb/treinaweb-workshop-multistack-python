from rest_framework import serializers
from web.models import Diarista


class DiaristaCidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diarista
        fields = ('nome_completo', 'foto_usuario', 'cidade')