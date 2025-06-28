from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# 로깅 설정
logger = logging.getLogger(__name__)

# 환경 변수 로드
load_dotenv()

# Gemini API 키 설정
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key or gemini_api_key == 'your_gemini_api_key_here':
    logger.warning("Gemini API 키가 설정되지 않았습니다. .env 파일에 올바른 API 키를 설정해주세요.")

# Gemini 클라이언트 설정
if gemini_api_key and gemini_api_key != 'your_gemini_api_key_here':
    genai.configure(api_key=gemini_api_key)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')
else:
    gemini_model = None

def home(request):
    """챗봇 홈페이지 뷰"""
    return render(request, 'chatbot/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """챗봇 API 엔드포인트"""
    try:
        if not gemini_api_key or gemini_api_key == 'your_gemini_api_key_here':
            return JsonResponse({
                'error': 'Gemini API 키가 설정되지 않았습니다. .env 파일에 올바른 API 키를 설정해주세요.',
                'status': 'error'
            }, status=400)
        
        if not gemini_model:
            return JsonResponse({
                'error': 'Gemini 모델이 초기화되지 않았습니다.',
                'status': 'error'
            }, status=500)
        
        data = json.loads(request.body)
        user_message = data.get('message', '')
        if not user_message:
            return JsonResponse({
                'error': '메시지가 비어있습니다.',
                'status': 'error'
            }, status=400)
        
        logger.info(f"사용자 메시지 수신: {user_message[:50]}...")
        
        # Gemini API 호출
        system_prompt = "당신은 친근하고 도움이 되는 AI 어시스턴트입니다. 한국어로 답변해주세요."
        full_prompt = f"{system_prompt}\n\n사용자: {user_message}\n어시스턴트:"
        
        response = gemini_model.generate_content(full_prompt)
        bot_response = response.text
        
        logger.info(f"AI 응답 생성 완료: {bot_response[:50]}...")
        return JsonResponse({
            'response': bot_response,
            'status': 'success'
        })
    except Exception as e:
        logger.error(f"Gemini API 오류: {str(e)}")
        return JsonResponse({
            'error': f'Gemini API 오류가 발생했습니다: {str(e)}',
            'status': 'error'
        }, status=500)
    except json.JSONDecodeError:
        logger.error("JSON 파싱 오류")
        return JsonResponse({
            'error': '잘못된 요청 형식입니다.',
            'status': 'error'
        }, status=400)
    except Exception as e:
        logger.error(f"예상치 못한 오류: {str(e)}")
        return JsonResponse({
            'error': f'서버 오류가 발생했습니다: {str(e)}',
            'status': 'error'
        }, status=500)

def health_check(request):
    """헬스 체크 엔드포인트"""
    api_key_status = "설정됨" if gemini_api_key and gemini_api_key != 'your_gemini_api_key_here' else "설정되지 않음"
    return JsonResponse({
        'status': 'healthy',
        'api_key_status': api_key_status
    })
