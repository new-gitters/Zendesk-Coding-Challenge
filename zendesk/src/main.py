from flask import Flask,render_template,request,redirect
import json
from request import get_list_tickets,get_single_ticket,authenticate
app = Flask(__name__,template_folder='./app/templates')
curr_page=1

@app.route("/",methods = ['GET'])
def home():
    return render_template("index.html")


@app.route("/login",methods = ['POST'])
def login():
    account=request.form.get("account")
    token=request.form.get("token")
    status,reason=authenticate(account,token)
    if status==200:
        return redirect("/table")
    else:
        return render_template("error.html",status=status,reason=reason)

@app.route("/table",methods = ['POST', 'GET'])
def table():
    global curr_page
    if request.method == "GET":
        
        curr_page=1
        context=get_list_tickets(curr_page)
        if context['status_code']==200:
            return render_template("base.html",data=context)
        else:
            return render_template("error.html",status=context['status_code'],reason=context['reason'])
    
    elif request.method == "POST":
        if request.form.get("prev"):
            context=get_list_tickets(curr_page)
            if context['prev_page']!=None:
                curr_page-=1
                new_context=get_list_tickets(curr_page)
                return render_template("base.html",data=new_context)
            else:
                return render_template("base.html",data=context)
            #print(new_data)
            
        elif request.form.get("next"):
            context=get_list_tickets(curr_page)
            if context['next_page']!=None:
                curr_page+=1
                new_context=get_list_tickets(curr_page)
                return render_template("base.html",data=new_context)
            else:
                return render_template("base.html",data=context)

        elif request.form.get("home"):
            context=get_list_tickets(curr_page)
            return render_template("base.html",data=context)



@app.route('/getTicketById',methods=['POST'])
def getTicketById():
    dict_=request.form.to_dict()
    #id=list(dict_.keys())[0]#request.form.to_dict().keys()[0]
    url=list(dict_.values())[0]#request.form.to_dict().values()[0]
    context=get_single_ticket(url)
    if context['status_code']==200:
        return render_template("single.html",ticket=context['ticket'])
    else:
        return render_template("error.html",status=context['status_code'],reason=context['reason'])


if __name__ == '__main__':
    app.run(debug = True)