from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def login(request):
    return render(request,'loginindex.html')



def login_post(request):
    username = request.POST['name']
    password = request.POST['password']
    lobj = Login.objects.filter(username=username, password=password)
    if lobj.exists():
        log =Login.objects.get(username=username, password=password)
        request.session['lid'] = log.id
        if log.type == 'admin':
            return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')
        elif log.type == 'user':
            return HttpResponse('''<script>alert("success");window.location="/myapp/home_user/"</script>''')
        else:
            return HttpResponse('''<script>alert("success");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("login failed");window.location="/myapp/login/"</script>''')


# ADMIN

def home(request):
    return render(request, 'admin/adminindex.html')


def home_user(request):
    return render(request, 'user/userindex.html')

def addcategory(request):
    return render(request, 'admin/addcategory.html')


def addcategory_post(request):
    # if request.session['lid'] == '':
    category_name = request.POST['category_name']
    photos = request.FILES['pho']
    caobj = Category()

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photos)
    photopath = fs.url(date)

    caobj.category_name = category_name
    caobj.photo = photopath
    caobj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')
def view_category(request):
    obj = Category.objects.all()
    return render(request,'admin/view _category.html', {"data": obj})


def view_category_post(request):
    search = request.POST['search']
    print("search", search)
    obj = Category.objects.filter(category_name__icontains=search)
    return render(request,'admin/view _category.html',{"data": obj})
def edit_category(request, id):
    res = Category.objects.get(id=id)

    return render(request, 'admin/edit_category.html', {'data': res})


def edit_category_post(request):
    id = request.POST['id']
    category_name = request.POST['category_name']


    obj = Category.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        photopath = fs.url(date)
        obj.photo=photopath

    obj.category_name = category_name
    obj.save()
    return HttpResponse('''<script>alert("edited successfuly");window.location="/myapp/view_category/"</script>''')


def delete_category(request,id):
    res=Category.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/view_category/"</script>''')


def add_diamension(request):
    res3=Shapes.objects.all()
    return render(request, 'admin/add_diamension.html', {'data': res3})
def add_diamension_post(request):
    height=request.POST['height']
    width=request.POST['width']
    total_wood_needed=request.POST['totalwood']
    shape=request.POST['shape']
    dobj = Diamension()
    dobj.height= height
    dobj.width=width
    dobj. total_wood_needed= total_wood_needed
    dobj.SHAPES_id=shape
    dobj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')
def view_diamension(request):
    res = Diamension.objects.all()
    return render(request, 'admin/view_diamension.html', {"data": res})
def view_diamension_post(request):
    search = request.POST['search']
    print("search", search)
    res = Diamension.objects.filter(SHAPES__shape__icontains=search)
    return render(request,'admin/view_diamension.html',{'data': res})

def edit_diamension(request, id):
    res = Diamension.objects.get(id=id)
    return render(request,'admin/edit_diamension.html', {'data': res})


def edit_diamension_post(request):
    id = request.POST['id']
    height = request.POST['height']
    width = request.POST['width']
    total_wood_needed = request.POST['total_wood_needed']

    obj = Diamension.objects.get(id=id)


    obj.height = height
    obj.width =width
    obj.total_wood_needed =total_wood_needed
    obj.save()
    return HttpResponse('''<script>alert("edited successfuly");window.location="/myapp/view_diamension/"</script>''')


def delete_diamension(request,id):
    res=Diamension.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/view_diamension/"</script>''')




def add_wood(request):
     res = Category.objects.all()
     return render(request,'admin/add_wood.html',{'data':res})
def add_wood_post(request):
    wood_name=request.POST['wood_name']
    sqft_charge=request.POST['sqftcharge']
    cat=request.POST['cat']
    dobj = Wood()
    dobj. wood_name= wood_name
    dobj. sqft_charge= sqft_charge
    dobj.CATEGORY_id=cat
    dobj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')

def view_wood(request):
    res = Wood.objects.all()
    return render(request, 'admin/view_wood.html', {"data": res})


def view_wood_post(request):
    search = request.POST['search']
    print("search", search)
    res = Wood.objects.filter(CATEGORY__category_name__icontains=search)
    return render(request,'admin/view_wood.html',{'data': res})

def edit_wood(request, id):
    res = Wood.objects.get(id=id)
    return render(request,'admin/edit_wood.html', {'data': res})


def edit_wood_post(request):
    id = request.POST['id']
    wood_name = request.POST['wood_name']
    sqft_charge=request.POST['sqft_charge']
    obj = Wood.objects.get(id=id)


    obj.wood_name = wood_name
    obj.sqft_charge=sqft_charge
    obj.save()
    return HttpResponse('''<script>alert("edited successfuly");window.location="/myapp/view_wood/"</script>''')


def delete_wood(request,id):
    res=Wood.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/view_wood/"</script>''')




def add_shape(request):
    data = Category.objects.all()
    return render(request, 'admin/add_shape.html', {'data': data})

def add_shape_post(request):
    id=request.POST['id']
    shape=request.POST['shapes']
    dobj= Shapes()
    dobj.shape=shape
    dobj.CATEGORY_id =id
    dobj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')



def view_shape(request):
        res = Shapes.objects.all()
        return render(request, 'admin/view_shape.html', {"data": res})

def view_shape_post(request):
        search = request.POST['search']
        print("search", search)
        res = Shapes.objects.filter(CATEGORY__category_name__icontains=search)
        return render(request, 'admin/view_shape.html', {'data': res})
def edit_shape(request, id):
    res = Shapes.objects.get(id=id)
    return render(request,'admin/edit_shape.html', {'data': res})


def edit_shape_post(request):
    id = request.POST['id']
    shape = request.POST['shape']

    obj = Shapes.objects.get(id=id)


    obj.shape = shape

    obj.save()
    return HttpResponse('''<script>alert("edited successfuly");window.location="/myapp/view_shape/"</script>''')


def delete_shape(request,id):
    res=Shapes.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/view_shape/"</script>''')







def add_design(request):
    data = Wood.objects.all()
    return render(request, 'admin/add design.html', {'data': data})


def add_design_post(request):
    id = request.POST['id']
    photo = request.FILES['photo']
    price = request.POST['price']
    shape = request.POST['shapes']
    wood_name = request.POST['wood_name']
    description = request.POST['description']
    # wd=Category.objects.get(id=id).
    dname = request.POST['dd']
    dobj = Design()
    dobj.WOOD_id = Wood.objects.get(CATEGORY_id=id).id
    dobj.photo = photo
    dobj.price = price
    dobj.shape=shape
    dobj.wood_name =wood_name

    dobj.description = description
    dobj.design_name = dname

    dobj.save()

    # if 'photo' in request.FILES:
    #     photo=request.FILES['photo']
    # #image
    date = datetime.now().strftime('%Y%m%d-%H%M%S') +".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    photopath = fs.url(date)
    dobj.photo = photopath
    dobj.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')
def viewdesign(request):
    res = Design.objects.all()
    return render(request, 'admin/viewdesign.html', {"data": res})


def viewdesign_post(request):
    search = request.POST.get('search', '')  # Safely get the search term
    print("search:", search)
    res = Design.objects.filter(WOOD__CATEGORY__category_name__icontains=search)

    return render(request, 'admin/viewdesign.html', {'data': res})


def edit_design(request,id):
    res = Design.objects.get(id=id)
    objs = Category.objects.all()
    return render(request, 'admin/edit_design.html',{'data': res, "cat": objs})


def edit_design_post(request):
    id = request.POST['id']
    price = request.POST['price']
    shape = request.POST['shapes']
    wood_name = request.POST['wood_name']
    description = request.POST['description']

    objs = Design.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        date = datetime.now().strftime('%Y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(date, photo)
        photopath = fs.url(date)
        objs.photo = photopath
        objs.save()

    objs.price = price
    objs.shape = shape
    objs.wood_name = wood_name
    objs.description = description
    objs.save()
    return HttpResponse('''<script>;window.location="/myapp/viewdesign/"</script>''')
def delete_design(request,id):
    res=Design.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/viewdesign/"</script>''')



def add_post(request):
    res = Design.objects.all()
    return render(request, 'admin/add_post.html',{'data': res})


def add_post_post(request):
    id = request.POST['id1']
    post_name = request.POST['post']
    photo_1 = request.FILES['photo_1']
    photo_2 = request.FILES['photo_2']
    photo_3 = request.FILES['photo_3']
    description_1 = request.POST['description_1']
    description_2 = request.POST['description_2']
    description_3 = request.POST['description_3']


    postobj = Post()
    postobj.post_name = post_name
    postobj.DESIGN= Design.objects.get(id=id)
    postobj.photo_1 = photo_1
    postobj.photo_2 = photo_2
    postobj.photo_3 = photo_3
    postobj.description_1 = description_1
    postobj.description_2 = description_2
    postobj.description_3 = description_3

    date = datetime.now().strftime('%Y%m%d-%H%M%S')+"1.jpg"
    fs = FileSystemStorage()
    fs.save(date, photo_1)
    photopath = fs.url(date)
    postobj.photo_1 = photopath

    date1 = datetime.now().strftime('%Y%m%d-%H%M%S')+"2.jpg"
    fs1 = FileSystemStorage()
    fs1.save(date1, photo_2)
    photopath1 = fs1.url(date1)
    postobj.photo_2 = photopath1

    date2 = datetime.now().strftime('%Y%m%d-%H%M%S')+"3.jpg"
    fs2 = FileSystemStorage()
    fs2.save(date2, photo_3)
    photopath2 = fs2.url(date2)
    postobj.photo_3 = photopath2
    postobj.save()

    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("invalid");window.location="/myapp/adminhome/"</script>''')
    return HttpResponse('''<script>alert("success");window.location="/myapp/adminhome/"</script>''')
def view_post(request):
    obj5 = Post.objects.all()
    return render(request, 'admin/view_post.html', {"data": obj5})


def view_post_post(request):
    search = request.POST["search"]
    obj5 = Post.objects.filter(post_name__icontains=search)
    return render(request, 'admin/view_post.html', {"data": obj5})

def edit_post(request,id):
    res = Post.objects.get(id=id)
    objst = Design.objects.all()
    return render(request, 'admin/edit_post.html', {'data': res, "cat": objst})


def delete_post(request,id):
    res=Post.objects.get(id=id).delete()
    return HttpResponse('''<script>;window.location="/myapp/view_post/"</script>''')



def edit_post_post(request):
    post_name = request.POST['post_name']
    design_id = request.POST['design_id']
    description_1 = request.POST['description_1']
    description_2 = request.POST['description_2']
    description_3 = request.POST['description_3']

    id = request.POST['id']
    objst = Post.objects.get(id=id)
    if 'photo_1' in request.FILES:
        photo_1 = request.FILES['photo_1']

        date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"
        fs = FileSystemStorage()
        fs.save(date, photo_1)
        photopath = fs.url(date)
        objst.photo_1 = photopath
        objst.save()

    if 'photo_2' in request.FILES:
        photo_2 = request.FILES['photo_2']

        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + "2.jpg"
        fs1 = FileSystemStorage()
        fs1.save(date1, photo_2)
        photopath2 = fs1.url(date1)
        objst.photo_2 = photopath2
        objst.save()
    if 'photo_3' in request.FILES:
        photo_3 = request.FILES['photo_3']

        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + "3.jpg"
        fs2 = FileSystemStorage()
        fs2.save(date2, photo_3)
        photopath3 = fs2.url(date2)
        objst.photo_3 = photopath3
        objst.save()
    objst.description_1 = description_1
    objst.description_2 = description_2
    objst.description_3 = description_3
    objst.post_name = post_name
    objst.DESIGN_id = Design.objects.get(id=design_id).id
    objst.save()
    return HttpResponse('''<script>;window.location="/myapp/view_post/"</script>''')







def addproduct(request):
    return render(request, 'admin/addproduct.html')




def change_password(request):
    return render(request, 'admin/change_password.html')


def change_password_post(request):
    currentpassword = request.POST['current_password']
    newpassword = request.POST['new_password']
    confirmpassword = request.POST['confirm_password']
    res = Login.objects.filter(id=request.session['lid'], password=currentpassword)
    if res.exists():
        res = Login.objects.get(id=request.session['lid'], password=currentpassword)

        if newpassword == confirmpassword:
            res = Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("password changed");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("password mismatched");window.location="/myapp/change_password/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("check current password");window.location="/myapp/change_password/"</script>''')



















def view_orders(request):
    obj3 = Order.objects.filter(status='pending')
    return render(request, 'admin/view_orders.html', {"data": obj3})


def view_orders_post(request):
    df = request.POST["date1"]
    dt = request.POST["date2"]

    cv = Order.objects.filter(date__range=[df, dt],status='pending')
    return render(request, 'admin/view_orders.html', {'data': cv})

def view_verifiedorders(request):
    obj4=Order.objects.filter(status='verified')
    return render(request, 'admin/view_verifiedorders.html',{"data":obj4})

def view_verifiedorders_post(request):
    df = request.POST["textfield"]
    dt = request.POST["textfield2"]

    cv = Order.objects.filter(date__range=[df, dt], status='verified')

    return render(request, 'admin/view_verifiedorders.html', {'data': cv})



def verifi_orders(request,id):
    Order.objects.filter(id=id).update(status = 'verified')
    return HttpResponse('''<script>;window.location="/myapp/view_orders/"</script>''')


def verifycustomised_orders(request,id):
    Customized_order.objects.filter(id=id).update(status = 'verified')
    return HttpResponse('''<script>;window.location="/myapp/viewcustomised_order/"</script>''')

def viewcustomised_order(request):
    obj7 = Customized_order.objects.filter(status='pending')
    return render(request, 'admin/viewcustomised_order.html', {"data": obj7})


def viewcustomised_order_post(request):
    df = request.POST["textfield"]
    dt = request.POST["textfield2"]
    vc = Customized_order.objects.filter(date__range=[df, dt], status='pending')
    return render(request, 'admin/viewcustomised_order.html', {'data': vc})


def viewverified_customisedorder(request):
    obj9 = Customized_order.objects.filter(status='verified')
    return render(request, 'admin/viewverified_customisedorder.html',{"data":obj9})


def AddAmounttocustomisedproduct(request,id):
    data=Customized_order.objects.get(id=id)
    return render(request,'admin/edit_product.html',{"data":data})


# def AddAmounttocustomisedproduct_post(request):
#     pid=request.POST['pid']
#     price=request.POST['price']
#     data=Customized_order.objects.get(PRODUCT_id=pid)
#     data.status="verified"
#     data.save()
#
#     Product.objects.filter(id=pid).update(price=price)
#
#     return HttpResponse('''<script>alert("price added success");window.location="/myapp/viewverified_customisedorder/"</script>''')
#


def AddAmounttocustomisedproduct_post(request):
    pid = request.POST['pid']
    price = float(request.POST['price'])  # Convert the price from POST data to float
    data = Customized_order.objects.get(PRODUCT_id=pid)

    data.status = "verified"
    data.save()

    product = Product.objects.get(id=pid)

    new_price = product.price + price

    Product.objects.filter(id=pid).update(price=new_price)

    return HttpResponse(
        '''<script>alert("Price added successfully");window.location="/myapp/viewverified_customisedorder/"</script>''')







def raz_payUser(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = Customized_payment()
    obj.CUSTOMIZED_ORDER_id = id
    obj.date = datetime.now().today()
    obj.price = float(amount)
    obj.status = 'paid'
    # obj.CUSTOMER_ID = Customer.objects.get(LOGIN_id=request.session['lid'])
    obj.save()

    Order.objects.filter(id=id).update(status='paid',totalamount=amount)

    return render(request, 'user/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})














def viewverified_customisedorder_post(request):
    df = request.POST["textfield"]
    dt = request.POST["textfield2"]

    vc = Customized_order.objects.filter(date__range=[df, dt], status='verified')
    return render(request, 'admin/viewverified_customisedorder.html',{'data':vc})


def view_users(request):
    obj6 = Customer.objects.all()
    return render(request, 'admin/view_users.html', {"data": obj6})


def view_users_post(request):
    search = request.POST["search"]
    obj6 = Customer.objects.filter(customer_name__icontains=search)
    return render(request, 'admin/view_users.html', {"data": obj6})


def viewrating(request):
    obj8 = review_and_rating.objects.all()
    return render(request, 'admin/viewrating.html', {'data': obj8})


def viewrating_post(request):
    df = request.POST["date1"]
    dt = request.POST["date2"]

    cv = review_and_rating.objects.filter(date__range=[df, dt])
    return render(request, 'admin/viewrating.html', {'data': cv})


# u#user


# def view_product(request):
#     obj1 = Product.objects.all()
#     return render(request, 'admin/view_product.html', {"data": obj1})
#
#
# def view_product_post(request):
#     search = request.POST['search']
#     print("search", search)
#     obj1 = Product.objects.filter(product_name__icontains=search)
#     return render(request, 'admin/view_product.html', {"data": obj1})



def view_profile(request):
    cc=Customer.objects.get(LOGIN=request.session['lid'])
    return render(request, 'user/view_profile.html',{'data':cc})
def edit_profile(request):
    cc = Customer.objects.get(LOGIN=request.session['lid'])
    return render(request, 'user/edit_profile.html',{'data':cc})

def edit_profilepost(request):
    customer_name = request.POST['name']
    email = request.POST['email']
    mobilenumber = request.POST['mobilenumber']
    place = request.POST['place']
    district = request.POST['district']
    post = request.POST['post']
    pin = request.POST['pin']

    re = Customer.objects.get(LOGIN=request.session['lid'])
    re.customer_name = customer_name
    re.email = email
    re.mobilenumber = mobilenumber
    re.place = place
    re.district = district
    re.post = post
    re.pin = pin
    re.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/view_profile/"</script>''')




def choose_category(request):
    obj = Category.objects.all()
    return render(request, 'user/choose_category.html', {"data": obj})




def choose_category_post(request):
    search = request.POST['search']
    print("search", search)
    obj = Category.objects.filter(CATEGORY__category_name__icontains=search)
    return render(request,'user/choose_category.html', {"data": obj})



def register(request):
    return render(request,'admin/index.html')


def register_post(request):
    customer_name=request.POST['name']
    email=request.POST['email']
    mobilenumber=request.POST['mobilenumber']
    place=request.POST['place']
    district=request.POST['district']
    post=request.POST['post']
    pin=request.POST['pin']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']

    if Customer.objects.filter(email=email,mobilenumber=mobilenumber):
        return HttpResponse('''<script>alert("email or phone already exists");window.location="/myapp/login/"</script>''')
    else:
        if password==confirm_password:
            lg=Login()
            lg.username=email
            lg.password=confirm_password
            lg.type='user'
            lg.save()

            re=Customer()
            re.customer_name=customer_name
            re.email=email
            re.mobilenumber=mobilenumber
            re.place=place
            re.district=district
            re.post=post
            re.pin=pin
            re.LOGIN=lg
            re.save()
            return HttpResponse('''<script>alert("success");window.location="/myapp/login/"</script>''')
        else:
             return HttpResponse('''<script>alert("password mismatch");window.location="/myapp/register"</script>''')


def edit_customise_product(request, id):
    res = Customized_order.objects.get(id=id)
    # objsts=Product.objects.all()
    return render(request, 'user/edit_product.html', {'data': res})


def edit_Customised_product_post(request):
    product_name = request.POST['product_name']
    description = request.POST['description']
    material = request.POST['material']
    id = request.POST['id']

    objsts = Product.objects.get(id=id)
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        photopath = fs.url(date)
        objsts.photo = photopath
        objsts.save()
    objsts.description = description
    objsts.material = material
    objsts.product_name = product_name
    objsts.save()

    data=Customized_order.objects.get(PRODUCT_id=id)
    data.date=datetime.now()
    data.status="pending"
    data.save()
    return HttpResponse('''<script>alert('edited succesfully');window.location="/myapp/view_customizedrequeststatus/"</script>''')



def addCustomisedproduct_post(request):
    product = request.POST['textfield']
    des = request.POST['textfield2']
    materials = request.POST['textfield3']
    photo = request.FILES['fileField']
    qnt = request.POST['num']

    fs = FileSystemStorage()
    d = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs.save(d, photo)
    path = fs.url(d)
    # prices = request.POST['textfield4']


    probj = Product()
    probj.product_name = product
    probj.description = des
    probj.material = materials
    probj.photo = path
    probj.price = 0
    probj.Quantity = qnt
    probj.save()

    cs=Customized_order()
    cs.CUSTOMER=Customer.objects.get(LOGIN_id=request.session['lid'])
    cs.PRODUCT=probj
    cs.date=datetime.now()
    cs.status="pending"
    cs.save()
    return HttpResponse('''<script>alert("success");window.location="/myapp/home_user/"</script>''')



def delete_Customised_product(request,id):
    res=Customized_order.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("custamosed product deleted");window.location="/myapp/view_customizedrequeststatus/"</script>''')

def sendcustomized_request(request):
    p = Wood.objects.all()
    d = Diamension.objects.all()

    return render(request,'user/sendcustomized_request.html',{'data':p,'d':d})


def sendcustomized_request_post(request):
    wood = request.POST['wood']
    price = float(request.POST['price'])
    shape = request.POST['shape']
    PRODUCTNAME = request.POST['textfield']
    description = request.POST['textfield2']
    material = request.POST['textfield']
    photo=request.FILES['fileField']
    quantity= request.POST['quantity']
    d=datetime.now()
    fs = FileSystemStorage()
    # d = datetime.now().strftime('%y%m%d-%H%M%S')
    # fs.save(d,photo)
    # path = fs.path(d)
    d = datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs.save(d, photo)
    path = fs.url(d)





    a=Product()
    a.description=description
    a.product_name=PRODUCTNAME
    a.material=material
    a.am=quantity
    a.Quantity=quantity
    a.photo=path
    a.price=price
    a.save()

    o=Customized_order()
    o.PRODUCT=a
    o.CUSTOMER=Customer.objects.get(LOGIN_id=request.session['lid'])
    o.DIMENSION=Diamension.objects.get(id=shape)
    o.WOOD=Wood.objects.get(id=wood)
    o.date=datetime.now().today().date()
    o.status='pending'
    o.save()



    return HttpResponse('''<script>alert("success");window.location="/myapp/home_user/"</script>''')






def view_customizedrequeststatus(request):
    data=Customized_order.objects.filter(CUSTOMER__LOGIN_id=request.session['lid'],status="pending")
    print(data)
    return render(request, 'user/view_customizedrequeststatus.html',{"data":data})


def view_customizedrequeststatus_post(request):
    search = request.POST['textfield']
    search1 = request.POST['textfield2']
    data = Customized_order.objects.filter(date__range=[search,search1],status="pending")
    return render(request, 'user/view_customizedrequeststatus.html',{"data":data})


def viewverifiedCustomiserequest_get(request):
    data=Customized_order.objects.filter(CUSTOMER__LOGIN_id=request.session['lid'],status="Verified")
    return render(request,'user/view_customizedrequeststatus.html',{"data":data})





def send_review(request,id):

    return render(request,'user/sendreviewrating.html',{'id':id})


def send_review_post(request):
    review=request.POST['textarea']
    rating=request.POST['rating']
    did=request.POST['did']
    obj=review_and_rating()
    obj.date=datetime.now().today()
    obj.rating=rating
    obj.review=review
    obj.DESIGN_id=did
    obj.CUSTOMER=Customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return redirect("/myapp/userviewdesign/"+did)

def view_review(request,id):
    res=review_and_rating.objects.filter(DESIGN_id=id)
    return render(request,'user/viewrating.html',{'data':res})

def send_order(request,id):
    return render(request,'user/add_quantity.html',{'id':id})

def send_order_post(request):
    quantity=request.POST['Q']
    did=request.POST['did']
    obj=Order()
    obj.DESIGN_id=did
    obj.CUSTOMER_ID=Customer.objects.get(LOGIN=request.session['lid'])
    obj.date=datetime.now().today()
    obj.status='pending'
    obj.quantity=quantity
    obj.save()

    return HttpResponse('''<script>alert("success");window.location="/myapp/home_user/"</script>''')




def view_orderstatus(request):
    res=Order.objects.filter(CUSTOMER_ID__LOGIN_id=request.session['lid'])
    l=[]
    for i in res:
        p=Design.objects.get(id=i.DESIGN.id).price
        ttl=i.quantity*float(p)
        l.append({
            'id':i.id,
            'dphoto':i.DESIGN.photo,
            'dname':i.DESIGN.design_name,
            # 'category':i.DESIGN.CATEGORY.category_name,
            'date':i.date,
            'status':i.status,
            'quantity':i.quantity,'amount':ttl
        })
    return render(request, 'user/view_orderstatus.html',{"data":l})


def raz_pay(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = Payment()
    obj.ORDER_id = id
    obj.date = datetime.now().today()
    obj.price = float(amount)
    obj.status = 'paid'
    obj.CUSTOMER_ID = Customer.objects.get(LOGIN_id=request.session['lid'])
    obj.save()

    Order.objects.filter(id=id).update(status='paid',totalamount=amount)

    return render(request, 'user/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})




def view_orderstatus_post(request):
    search = request.POST['textfield']
    search1=request.POST['textfield2']

    res = Order.objects.filter(date__range=[search,search1],CUSTOMER_ID__LOGIN_id=request.session['lid'])
    l = []
    for i in res:
        p = Design.objects.get(id=i.DESIGN.id).price
        ttl = i.quantity * float(p)
        l.append({
            'id': i.id,
            'dphoto': i.DESIGN.photo,
            'dname': i.DESIGN.design_name,
            'category': i.DESIGN.WOOD.CATEGORY.category_name,
            'date': i.date,
            'status': i.status,
            'quantity': i.quantity, 'amount': ttl
        })

    return render(request,'user/view_orderstatus.html',{"data":l})


def viewposts_post(request):
    res = Post.objects.all()
    return render(request,'user/viewposts.html',{"data":res})


def viewposts_post_post(request):
    search = request.POST["textfield"]
    res= Post.objects.filter(post_name__icontains=search)
    return render(request, 'user/viewposts.html', {"data": res})


def user_view_product(request):
    return render(request, 'user/view_product.html')


def user_view_product_post(request):
    return render(request, 'user/view_product.html')


def userviewdesign(request,id):
    res = Design.objects.filter(WOOD__CATEGORY_id=id)
    a=Wood.objects.all()
    return render(request, 'user/viewdesign.html', {"data": res,'wood':a})




#
# def userviewdesign_post(request):
#     search = request.POST['search']
#     print("search", search)
#     res = Design.objects.filter(design_name__icontains=search)
#     a=Wood.objects.all()
#
#     return render(request, 'user/viewdesign.html', {'data': res,'wood':a})
# from django.db.models import Q
#
from django.db.models import Q

from django.db.models import Q


def userviewdesign_post(request):
    search_design = request.POST.get('search_design', '')  # Get the design name search query
    search_wood = request.POST.get('search_wood', '')  # Get the wood ID search query

    # Filter by design name and optionally by wood name if selected
    query = Q(design_name__icontains=search_design)
    if search_wood:
        query &= Q(WOOD__id=search_wood)  # Filter by the selected wood ID

    res = Design.objects.filter(query)

    a = Wood.objects.all()  # Get all wood objects for the dropdown

    return render(request, 'user/viewdesign.html', {'data': res, 'wood': a})
