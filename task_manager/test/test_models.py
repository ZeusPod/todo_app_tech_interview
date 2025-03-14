from django.test import TestCase
from task_manager.models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        """Prueba que se pueda crear una tarea con datos válidos."""
        task = Task.objects.create(
            title="Comprar leche",
            description="Ir al supermercado",
            due_date="2025-03-20",
            completed=False,
            city="Caracas"
        )
        self.assertEqual(task.title, "Comprar leche")
        self.assertEqual(task.city, "Caracas")