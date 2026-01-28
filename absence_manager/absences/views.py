from rest_framework import generics, permissions
from .models import Absence
from .serializers import AbsenceSerializer

class AbsenceListCreateView(generics.ListCreateAPIView):
    """
    Gestisce la lista delle assenze (GET) e la creazione di una nuova (POST).
    """
    serializer_class = AbsenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtro fondamentale: l'utente vede SOLO le sue assenze.
        # Se è un admin (superuser), potrebbe vederle tutte.
        user = self.request.user
        if user.is_staff:
            return Absence.objects.all()
        return Absence.objects.filter(user=user)

    def perform_create(self, serializer):
        # Iniettiamo l'utente direttamente dal token JWT nel campo 'user' del modello
        serializer.save(user=self.request.user)

class AbsenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Gestisce il dettaglio, la modifica o la cancellazione di una singola assenza.
    """
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Anche qui, un utente non può modificare le assenze degli altri tramite ID
        return Absence.objects.filter(user=self.request.user)