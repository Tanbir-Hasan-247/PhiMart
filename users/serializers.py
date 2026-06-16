from djoser.serializers import UserCreateSerializer as UCS
from djoser.serializers import UserSerializer as US

class UserCreateSerializer(UCS):
    class Meta(UCS.Meta):
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'address', 'phone']
        
        
        
class UserSerializer(US):
    class Meta(US.Meta):
        ref_name = 'CustomUserSerializer'
        fields = ['id', 'email', 'first_name', 'last_name', 'address', 'phone']