from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginView(APIView):
  def post(self,request):
    response = {}
    response['status'] = 500
    response['message'] = 'Something Went Wrong'
    
    try :
      data = request.data
      
      #checking here for username and password
      if data.get('username') is None:
        response['message'] = "UserName Not Found"
        raise Exception('Username Not Found')
      
      if data.get('password') is None:
        response['messsage'] = 'Password is not Found'
        raise Exception('Password Is Not Found')
      
      #checking here that the particular username is there or not if not then exception raises
      check_user = User.objects.filter(username = data.get('username')).first()
      if check_user is None:
        response['message'] = "Invalid UserName Enter The Correct Username"
        raise Exception('Invalid UserName Enter The Correct Username')
      
      #here i am authenticating by taking its username and password
      user_obj = authenticate(username = data.get('username'), password = data.get('password'))
      if user_obj:
        login(request, user_obj)
        response['status'] = 200
        response['message'] = 'Welcome'
      else:
        response['message'] = "Username Or Password My be Wrong"
        raise Exception('Username Or Password May Br Wrong')
    
    except Exception as e:
      print(e)
      
    return Response(response)
LoginView = LoginView.as_view()
  
class RegisterView(APIView):
  def post(self,request):
    response = {}
    response['status'] = 500
    response['message'] = 'Something Went Wrong'
    
    try :
      data = request.data
      
      #checking here for username and password
      if data.get('username') is None:
        response['message'] = "UserName Not Found"
        raise Exception('Username Not Found')
      
      if data.get('password') is None:
        response['messsage'] = 'Password is not Found'
        raise Exception('Password Is Not Found')
      
      #checking here that the particular username is there or not if not then exception raises
      check_user = User.objects.filter(username = data.get('username')).first()
      if check_user:
        response['message'] = "Username Already Exists/Taken"
        raise Exception('Username Already Exists/Taken')
      
      #here i am authenticating by taking its username and password
      user_obj =User.objects.create(username = data.get('username'))
      user_obj.set_password(data.get('password'))
      user_obj.save()
      response['message'] = "Username Created Successfuly"
      response['status'] = 200
        
    except Exception as e:
      print(e)
      
    return Response(response)
RegisterView = RegisterView.as_view()