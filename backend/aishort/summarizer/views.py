from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
import openai   
from django.conf import settings


class SummarizeView(APIView):
    def post(self, request):
        url = request.data.get('url')
        dummy_text = "This is a dummy text for summarization."  # Placeholder for actual text extraction logic
      

        try:
            openai.api_key = settings.OPENAI_API_KEY
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Please summarize the following text: {dummy_text}"}
                ]
            )
            summary = completion.choices[0].message['content']
            return Response({'summary': summary}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)