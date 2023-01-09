from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .form import Voterage
def index(request):
    if request.method == 'POST':
        age=request.POST['age']
        name=request.POST['name']
        print(request.POST)
        context = {
            "messages": "you can not vote",
            'age':age,
            'name':name
        }
        
        if (int(age)<=17):
            context['messages'] = "You can't vote"
        else:
            context['messages'] = "You can vote"
            
            
        return render(request,'index.html', context=context)
    else:
        return render(request,'index.html')
        
        
def test(request):
    if request.method=='POST':
        name= request.POST['name']
      
   
    context={
     
      'name':name
       
    }
    
    return render(request,'index.html',context=context)
    
    
        # age >= 18 
        # print(age)
        # context={
        #     'age':age
        # }
       
    # elif 
    #     age = request.POST.get('age')
    #     return redirect(request,'/')

      
    
    # return render(request, "index.html")

    #     if age >= 18 :
    #         age=0
    #         print ("You are ready to vote")

    # else:
    #     print ('please vote')
    #     return render(request,'index.html')

# def index(request):

#     if request.method == 'POST':
#         if age <= 17:
#             age=0
#             print(age)
#             age= request.POST["age"]
#         dict = {
#         'age': age,
#         }
         
#         return render(request,"index.html",dict)
        
#     elif age >= 18 :
        
#         print(age)
            
#         render (request,'index.html',age)
            
#     else:
#         return render(request,'index.html',age)
      

       
    
        

    