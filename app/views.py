from django.shortcuts import render
from rest_framework.views import APIView
from .models import TodoApp
from rest_framework.response import Response


class TodoAppView(APIView):


	def get(self, request):
		
		list_data = []

		todo_data = TodoApp.objects.all()

		for todo in todo_data:
			if todo.schedule_date:
				list_data.append({"id":todo.id, "todo_text":todo.todo_text, "is_completed":todo.is_completed, "schedule_date":todo.schedule_date.replace(tzinfo=None)})
			else:
				list_data.append({"id":todo.id, "todo_text":todo.todo_text, "is_completed":todo.is_completed, "schedule_date":""})

		return Response({"data": list_data, "status":True, "message": "success"}, status=200)


	def post(self, request):

		todo_text = request.data.get("todo_text", "")
		schedule_date = request.data.get("schedule_date", "")

		if not schedule_date:
			schedule_date = None

		obj = TodoApp.objects.create(todo_text=todo_text, schedule_date=schedule_date)
		obj.save()

		return Response({"data":{"id":obj.id, "todo_text":obj.todo_text, "schedule_date":schedule_date}, "status":True, "message":"success"}, status=200)


	def delete(self, request):

		todo_id = request.query_params.get("id", "")

		obj = TodoApp.objects.get(id=todo_id)
		obj.delete()

		return Response({"data":{}, "status":True, "message":"success"}, status=200)


	def put(self, request):

		todo_id = request.data.get("todo_id", "")
		todo_text = request.data.get("todo_text", "")
		schedule_date = request.data.get("schedule_date", "")

		if not schedule_date:
			schedule_date = None

		obj = TodoApp.objects.get(id=todo_id)
		obj.todo_text = todo_text
		obj.schedule_date = schedule_date
		obj.save()

		return Response({"data":{"id":obj.id, "todo_text":obj.todo_text}, "status":True, "message":"success"}, status=200)


class TodoCompletedView(APIView):

	def post(self, request):

		todo_id = request.data.get("todo_id", "")

		obj = TodoApp.objects.get(id=todo_id)
		obj.is_completed = True
		obj.save()

		return Response({"data":{"id":obj.id, "todo_text":obj.todo_text}, "status":True, "message":"success"}, status=200)
