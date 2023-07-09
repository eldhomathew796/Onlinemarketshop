from django.shortcuts import render,redirect
from productsapp.models import product,category,customer
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.models import CartItem

# Create your views here.
def index(request):
    if 'username' in request.session:
        pro=product.objects.all()
        return render(request,'index.html',{'pro':pro})
    else:
        return redirect(login_user)

def adminindex(request):
    return render(request,'adminindex.html')  

def store(request):
    return render(request,'addcategory.html')

def addcategory(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
      
        data=category(categoryname=categoryname)
       
        
        data.save()
        return redirect('addcategory')
       
        
       
    return render(request,'addcategory.html')

  




def addpro(request):
    cat=category.objects.all()
     

    if request.method=='POST':
       
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['file'] 
        catgp=request.POST['sel']
        stock=request.POST['stock']
      
        categ=category.objects.get(id=catgp)  
        ctg= product(category=categ,image=image,name=name,description=description,price=price,stock=stock) 
        ctg.save()
        return redirect('addpro')
    return render(request,'addpro.html',{'cat':cat})
    
def showproduct(request):
    pro=product.objects.all()
    return render(request,'showproduct.html',{'pro':pro})

def editdetails(request,pk):
    pro=product.objects.get(id=pk)
    cat=category.objects.all()
    context={'pro':pro,'cat':cat}
    if request.method=='POST':
        pro.name=request.POST['name']
        pro.price=request.POST['price']
        pro.description=request.POST['description']
        pro.stock=request.POST['stock']
        if request.FILES.get('file'):
            pro.image=request.FILES.get('file')
        c=request.POST['sel']
        pro.category=category.objects.get(id=c)
        pro.save()
        return redirect('showproduct')
    return render(request,'edit.html',context)
def deletedetails(request,pk):
    std=product.objects.get(id=pk)
    std.delete()
    return redirect('showproduct')

def log_out(request):
    # if 'username' in request.session:
    #     request.session.flush()
    auth.logout(request) 
    pro=product.objects.all()
    return render(request,'index.html',{'pro':pro})

def loginpage(request):
    return render(request,'login.html') 

def register(request):
    return render(request,'register.html')

def signup(request):
    
    if 'username'in request.session:
        return redirect(index)
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name'] 
        username=request.POST['username']  
        email=request.POST['email']
        address=request.POST['address']
        contact=request.POST['contact']
        password= request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
               messages.info(request,'this user is already exists!!!')
               return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                    )
                details=customer.objects.create(
                    user=user,
                    address=address,
                    phone=contact,
                )
            user.save()    
            details.save()    
            
            return render(request,'login.html')
        else:
            messages.info(request,'password doesnot match')
            return redirect('signup')
        return redirect('loginpage')
    else:
          return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        pro=product.objects.all()
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
         # request.session["uid"]=user.id
        if user is not None:
            request.session["username"]=username
            # return redirect('index')
            if user.is_staff:
                auth.login(request,user)
                return render(request,'adminindex.html') 
            else:
                 # login(request,user)
                auth.login(request,user)
                # messages.info(request,f'Welcome {username}')
                return render(request,'index.html',{'pro':pro, 'user':user})
                # return redirect('userhomepage')
        else:
            messages.info(request,"invalid username or password")
            return redirect('loginpage') 
    else:
        return redirect(loginpage)



def details(request,pk,k):
    if 'username'in request.session:
        # return redirect(index)
        pro=product.objects.get(id=pk)
    
        return render(request,'details.html',{'product':pro, 'u':k})
    else:
       return redirect(login_user)
    
   

def profile(request,pk):
    if 'username'in request.session:
    #     return redirect(index)
        # std=User.objects.get(id=pk)
        det=customer.objects.get(user=request.user)
    
        return render(request,'profile.html',{'det':det})
    else:
       return redirect(login_user)


def showuser(request):
        # std=User.objects.filter(is_staff=0)
        det=customer.objects.all()
        return render(request,'showuser.html',{'det':det})

def deleteuser(request,pk):
    std=User.objects.get(id=pk)
    std.delete()
    return redirect('showuser')

def items(request):
    item=CartItem.objects.all()
    return render(request,'item.html',{'item':item})

def deleteitem(request,pk):
    item=CartItem.objects.get(id=pk)
    item.delete()
    return redirect('items')            


             
                    



                   












