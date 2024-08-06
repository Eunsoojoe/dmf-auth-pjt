from .models import User

# 기존 장고의 클래스를 상속받을 예정.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  

# 회원가입
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User    # 우리가 만든 모델로 설정
        # fiedls = '__all__'
        fields = ('username',)

# 로그인 
# user 테이블에서 정보를 가져와 입력 정보가 일치하면 세션을 발급
class CustomAuthenticationForm(AuthenticationForm):
    pass 