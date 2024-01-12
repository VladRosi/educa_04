from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden


@login_required
def course_chat_room(request, course_id):
  try:
    # * retrieve course with given id, to which
    # * joined current user
    course = request.user.courses_joined.get(id=course_id)
  except:
    # * the user is not student of the course or the course does not exist
    return HttpResponseForbidden()
  return render(request, 'chat/room.html', {'course': course})
