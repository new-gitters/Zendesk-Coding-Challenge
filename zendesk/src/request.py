
import requests

header={"Authorization":"Bearer 98d75e177bfc788af652d53886bd388ab2847e6cea5add00441490ff311ae8d5"} 
def get_list_tickets(page=1):
    page="https://zccadmin.zendesk.com/api/v2/tickets.json?per_page=25&page={}".format(page)
    res=requests.get(url=page,headers=header)
    context={}
    if res.status_code==200:
        data=res.json()
        context['status_code']=res.status_code
        context['reason']=res.reason
        context['total_count']=data["count"]
        context['next_page']=data["next_page"]
        context['prev_page']=data["previous_page"]
        context['count']=data["count"]
        tickets=data["tickets"]
        rows=[]
        headers=['id','subject','requester_id','status','priority']
        context['header']=headers
        context['first']=tickets[0]['id']
        context['last']=tickets[-1]['id']
        for x in tickets:
            entry={}
            entry['id']=x['id']
            entry['url']=x['url']
            entry['subject']=x['subject']
            entry['requester_id']=x['requester_id']
            entry['status']=x['status']
            entry['priority']=x['priority']
            entry['url']=x['url']
            rows.append(entry)
        context['rows']=rows
        return context
    else:
        context['status_code']=res.status_code
        context['reason']=res.reason
        return context

def get_single_ticket(url):
    res=requests.get(url=url,headers=header)
    context={}
    if res.status_code==200:
        context['status_code']=res.status_code
        context['reason']=res.reason
        context['ticket']=res.json()['ticket']
    else:
        context['status_code']=res.status_code
        context['reason']=res.reason
    return context


def authenticate(account,token):
    url = 'https://{}.zendesk.com/api/v2/tickets.json'.format(account)
    auth={}
    auth["Authorization"]="Bearer {}".format(token)
    res=requests.get(url=url,headers=auth)
    return res.status_code,res.reason










