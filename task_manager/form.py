from django import forms
from .models import Task
from django.utils.timezone import now

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'city']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.strip():
            raise forms.ValidationError("El título no puede estar vacío.")
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        
        created_at = self.instance.created_at.date() if self.instance.pk else now().date() 

        if due_date and due_date < created_at:
            raise forms.ValidationError("La fecha de vencimiento debe ser mayor o igual a la fecha de creación.")

        return due_date
