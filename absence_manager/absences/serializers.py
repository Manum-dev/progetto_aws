# absences/serializers.py
from rest_framework import serializers
from .models import Absence

class AbsenceSerializer(serializers.ModelSerializer):
    # Mostriamo lo username dell'utente invece dell'ID numerico
    # Lo impostiamo come ReadOnly perché lo prenderemo dal Token JWT nella View
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Absence
        fields = ['id', 'user', 'start_date', 'end_date', 'reason', 'status', 'created_at']
        
        # IMPORTANTE: Impediamo all'utente di manomettere lo stato o la data di creazione
        read_only_fields = ['status', 'created_at']

    def validate(self, data):
        """
        Validazione personalizzata: controlla che la data di fine non sia prima dell'inizio.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({
                "end_date": "La data di fine non può essere precedente alla data di inizio."
            })
        return data