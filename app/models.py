from django.db import models


class TodoApp(models.Model):
	todo_text = models.TextField(default=None, blank=True, null=True)
	schedule_date = models.DateTimeField(default=None, null=True)
	is_completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-pk']
