from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import redis
# Create your views here.

#sadd answers "It is certain" "It is decidedly so" "Without a doubt" "Yes definitely" "You may rely on it" "As I see it, yes" "Most likely" "Outlook good" "Yes" "Signs point to yes" "Reply hazy try again" "Ask again later" "Better not tell you now" "Cannot predict now" "Concentrate and ask again" "Don't count on it" "My reply is no" "My sources say no" "Outlook not so good" "Very doubtful"
r = redis.StrictRedis(host='localhost', port=6379, db = 0);

def index(request):
    return render(request,'index.html');

@csrf_exempt
def start(request):
    question = request.POST.get('question','');
    if r.get(question) != None:
        answer = r.get(question);
    else:
        if(r.scard("answers")>=1):
            answer = r.spop("answers");
        else:
            r.sadd("answers","It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful")
            answer = r.spop("answers");
        r.set(question,answer);

    return render(request,'answer.html',{'answer':answer});
