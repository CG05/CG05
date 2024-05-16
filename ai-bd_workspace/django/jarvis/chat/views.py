from django.shortcuts import render
from django.http import JsonResponse
import openai
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')

def get_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        # OpenAI API 키 설정
        openai.api_key = 'sk-proj-GVxEkCZtMZLQXy8JOx3xT3BlbkFJt1bi2EkFoaCebITtxGlE'
        
        # OpenAI ChatCompletion 사용하여 응답 생성
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{user_message}. Please send all messages korean except codes with html tags to print pretty."}
            ]
        )
        
        bot_response = response.choices[0].message.content.strip()
        
        # 최신 정보를 웹에서 크롤링
        if "최근" in user_message.lower() or "최신" in user_message.lower() or "오늘" in user_message.lower():
            try:
                search_url = f"https://www.google.com/search?q={user_message}"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                response = requests.get(search_url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                first = soup.find('div', class_='BNeawe');
                first_result = first.text
                print(first);
                bot_response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"{user_message}with{first_result}. Please send all messages korean except codes with html tags to print pretty."}
                    ]
                )
            except Exception as e:
                bot_response += f"\n\n(Note: Additional info could not be retrieved: {e})"

        return JsonResponse({'response': bot_response})
