from django.test import TestCase
from django.urls import reverse
from task_manager.models import Task

class TaskDetailViewTest(TestCase):
    def setUp(self):
        """Configura una tarea de prueba antes de cada test."""
        self.task = Task.objects.create(
            title="Revisar correo",
            description="Leer emails pendientes",
            due_date="2025-03-21",
            completed=False,
            city="Bogota"
        )

    def test_task_detail_view(self):
        """Prueba que la vista de detalle cargue correctamente."""
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Revisar correo")
