from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)  # added
    due_date = models.DateField(null=True, blank=True)  # added
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @staticmethod
    def create_todo(params):
        """
        Create a new Todo item
        """
        todo = Todo.objects.create(
            title=params.get('title'),
            description=params.get('description', ''),
            is_completed=params.get('is_completed', False),
            due_date=params.get('due_date', None)
        )
        return todo

    def update_todo(self, params):
        """
        Update an existing Todo item
        """
        self.title = params.get('title', self.title)
        self.description = params.get('description', self.description)
        self.is_completed = params.get('is_completed', self.is_completed)
        self.due_date = params.get('due_date', self.due_date)
        self.save()
        return self
