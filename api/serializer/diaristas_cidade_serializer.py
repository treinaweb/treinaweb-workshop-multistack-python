from rest_framework import serializers
from web.models import Diarista
import random


class DiaristaCidadeSerializer(serializers.ModelSerializer):
    reputacao = serializers.SerializerMethodField()

    class Meta:
        model = Diarista
        fields = ('nome_completo', 'foto_usuario', 'cidade', 'reputacao')

    def get_reputacao(self, obj):
        return random.randint(0, 5)