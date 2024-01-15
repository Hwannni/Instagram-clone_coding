from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed # Reply
from rest_framework.response import Response
import os
from minstagram.settings import MEDIA_ROOT, MEDIA_URL
from uuid import uuid4

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)
    

# class UploadReply(APIView):
#     def post(self, request):
#         feed_id = request.data.get('feed_id', None)
#         reply_content = request.data.get('reply_content', None)
#         email = request.session.get('email', None)

#         Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

#         return Response(status=200)