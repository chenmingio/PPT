import bottle
import jinja2
import pymongo
import uuid

route = bottle.route
run = bottle.run
request = bottle.request
response = bottle.response
template = bottle.template
debug = bottle.debug
redirect = bottle.redirect
view = bottle.jinja2_view

MongoClient = pymongo.MongoClient


# connect to db
client = MongoClient()
db = client.PPT

# list for projectInfo.html generation

projectInfoKeyList = ['project_no', 'project_name', 'production_line', 'fg_no', 'product_cycletime', 'runrate_hella', 'pv_hella', 'sop_hella', 'sop_customer', 't3_date', 't4_date', 'pv_supplier', 'purchasing', 'pjm', 'md', 'sqa_ttm', 'controlling', 'me', 'planner', 'year1_volume', 'year2_volume', 'year3_volume', 'year4_volume', 'year5_volume', 'year6_volume', 'year7_volume', 'year8_volume', 'year9_volume', 'year10_volume', 'part1_pn', 'part1_description', 'part1_usage', 'part1_target_price', 'part1_target_invest', 'part2_pn', 'part2_description', 'part2_usage', 'part2_target_price', 'part2_target_invest', 'part3_pn', 'part3_description', 'part3_usage', 'part3_target_price', 'part3_target_invest', 'part4_pn', 'part4_description', 'part4_usage', 'part4_target_price', 'part4_target_invest', 'part5_pn', 'part5_description', 'part5_usage', 'part5_target_price', 'part5_target_invest']

textDict = {'project_no': 'Project Number', 'project_name': 'Project Name', 'production_line': 'Production Line', 'fg_no': 'FG Number', 'product_cycletime': 'Product Cycletime', 'runrate_hella': 'Run&Rate @Hella', 'pv_hella': 'PV @hella', 'sop_hella': 'SOP @hella', 'sop_customer': 'SOP @Customer', 't3_date': 'T3 Sample Date', 't4_date': 'T4 Sample Date', 'pv_supplier': 'PV Sample', 'purchasing': 'Purchasing', 'pjm': 'PJM', 'md': 'MD', 'sqa_ttm': 'SQA_TtM<', 'controlling': 'Controlling', 'me': 'ME', 'planner': 'Planner', 'year1_volume': 'Year-1 Volume', 'year2_volume': 'Year-2 Volume', 'year3_volume': 'Year-3 Volume', 'year4_volume': 'Year-4 Volume', 'year5_volume': 'Year-5 Volume', 'year6_volume': 'Year-6 Volume', 'year7_volume': 'Year-7 volume', 'year8_volume': 'Year-8 Volume', 'year9_volume': 'Year-9 Volume', 'year10_volume': 'Year-10 Volume', 'part1_pn': 'Part-1 Pn', 'part1_description': 'Part-1 Description', 'part1_usage': 'Part-1 Usage', 'part1_target_price': 'Part-1 Target Price', 'part1_target_invest': 'Part-1 Target Invest', 'part2_pn': 'Part-2 PN', 'part2_description': 'Part-2 Description', 'part2_usage': 'Part-2 Usage', 'part2_target_price': 'Part-2 Target Price', 'part2_target_invest': 'Part-2 Target Invest', 'part3_pn': 'Part-3 PN', 'part3_description': 'Part-3 Description', 'part3_usage': 'Part-3 Usage', 'part3_target_price': 'Part-3 Target Price', 'part3_target_invest': 'Part-3 Target Invest', 'part4_pn': 'Part4 PN', 'part4_description': 'Part-4 Description', 'part4_usage': 'Part-4 Usage', 'part4_target_price': 'Part-4 Target Price', 'part4_target_invest': 'Part-4 Target Invest', 'part5_pn': 'Part-5 PN', 'part5_description': 'Part-5 Description', 'part5_usage': 'Part-5 Usage', 'part5_target_price': 'Part-5 Target Price', 'part5_target_invest': 'Part-5 Target Invest'}

styleDict = {'project_no': 'col-md-4', 'project_name': 'col-md-4', 'production_line': 'col-md-4', 'fg_no': 'col-md-4', 'product_cycletime': 'col-md-4', 'runrate_hella': 'col-md-3', 'pv_hella': 'col-md-3', 'sop_hella': 'col-md-3', 'sop_customer': 'col-md-3', 't3_date': 'col-md-3', 't4_date': 'col-md-3', 'pv_supplier': 'col-md-3', 'purchasing': 'col-md-3', 'pjm': 'col-md-3', 'md': 'col-md-3', 'sqa_ttm': 'col-md-3', 'controlling': 'col-md-3', 'me': 'col-md-3', 'planner': 'col-md-3', 'year1_volume': 'col-md-1', 'year2_volume': 'col-md-1', 'year3_volume': 'col-md-1', 'year4_volume': 'col-md-1', 'year5_volume': 'col-md-1', 'year6_volume': 'col-md-1', 'year7_volume': 'col-md-1', 'year8_volume': 'col-md-1', 'year9_volume': 'col-md-1', 'year10_volume': 'col-md-1', 'part1_pn': 'col-md-2', 'part1_description': 'col-md-2', 'part1_usage': 'col-md-2', 'part1_target_price': 'col-md-2', 'part1_target_invest': 'col-md-2', 'part2_pn': 'col-md-2', 'part2_description': 'col-md-2', 'part2_usage': 'col-md-2', 'part2_target_price': 'col-md-2', 'part2_target_invest': 'col-md-2', 'part3_pn': 'col-md-2', 'part3_description': 'col-md-2', 'part3_usage': 'col-md-2', 'part3_target_price': 'col-md-2', 'part3_target_invest': 'col-md-2', 'part4_pn': 'col-md-2', 'part4_description': 'col-md-2', 'part4_usage': 'col-md-2', 'part4_target_price': 'col-md-2', 'part4_target_invest': 'col-md-2', 'part5_pn': 'col-md-2', 'part5_description': 'col-md-2', 'part5_usage': 'col-md-2', 'part5_target_price': 'col-md-2', 'part5_target_invest': 'col-md-2'}

def insert_document(collection_name, dict):
    '''insert dict into collection_name'''
    collection = getattr(db, collection_name)
    result = collection.insert_one(dict)

def fetch_document(collection_name, key, value):
    '''return the document in a collection according to its key and vaule'''

    collection = getattr(db, collection_name)
    query = {key: value}
    result = collection.find_one(query)
    return result

def add_project(projectInfo):
    """input a project info dictionary-object and save it in project collection"""

    # connect to collection project
    project = db.project

    # add into collection project
    result = project.insert_one(projectInfo)

def create_session(user_name):
    '''create a uuid string as token and go to user_name collection and store the token'''
    token = str(uuid.uuid4())
    user = db.user
    # store the token at certain user document
    query = {'user_name': user_name}
    update = {'$set': {'token': token} }
    results = user.update(query, update, upsert=False, multi=False)
    # add token to response
    response.set_cookie('token', token)

def get_session(request):
    token = request.get_cookie('token')
    userDoc = fetch_document('user', 'token', token)
    return userDoc



@route('/signin', method=['GET', 'POST'])
def signin():

    if request.POST.signin:
        reqUserName = request.forms['user_name']
        reqPassword = request.forms['password']

        userDoc = fetch_document("user", "user_name", reqUserName)
        if userDoc:
            if reqPassword == userDoc['password']:
                results = create_session(reqUserName)
                redirect("/main")
            else:
                return userDoc['password']
        else:
            return 'no such user'
    else:
        return template('tpl/signin')

@route('/')
@route('/main')
def main():
    userDoc = get_session(request)

    if userDoc:
        userGroup = userDoc['user_group']
        userName = userDoc['user_name']

        return template('tpl/main', user_name=userName, user_group=userGroup)
    else:
        redirect("/signin")



@route('/project/<project_id>', method=['GET', 'POST'])
@view('project.html', template_lookup=['templates'])
def overview(project_id):
    '''an overview of certain project. Readonly. No form necessary.'''

    # TODO user authorization

    # fetch basic project Info
    fetchProjectInfo = fetch_document('project', 'project_no', project_id)
    return fetchProjectInfo

@route('/test/project/<project_id>/info/<crud>', method=['GET', 'POST'])
@view('projectInfo.html', template_lookup=['templates'])
def test(project_id, crud):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['PUR', 'PJM']:

        if crud == 'create':
            fetchSuggestion = fetch_document('project', 'project_no', 'project_no')
            projectDeck = [[key, fetchSuggestion[key], textDict[key], styleDict[key]] for key in projectInfoKeyList]
            print(type(projectDeck))
            return projectDeck
        elif crud == 'read' or 'update':
            fetchResult = fetch_document('project', 'project_no', project_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True # 回头把它放在response里面试试
            return fetchResult
        elif crud == 'save':
            projectInfo = request.forms
            addResult = add_project(projectInfo)
            return 'added'
    else:
            "test failed"





@route('/project/<project_id>/info/<crud>', method=['GET', 'POST'])
def project(crud, project_id):
    '''crud: create/read/update/delete + save'''

    # TODO: if the project_id changes, how to solve? if there's a blank in project id... 


    userDoc = get_session(request)

    if userDoc['user_group'] in ['PUR', 'PJM']:

        if crud == 'create':
            # when create a new project, return a standard/instrumental project(projectid == 'projct_no') info as placeholder
            fetchSuggestion = fetch_document('project', 'project_no', 'project_no')
            # fetchSuggestion["crud"] = 'create'
            return template('tpl/project', **fetchSuggestion)
        elif crud == 'save':
            # in this situation, url receive a new form just been send to project/save
            projectInfo = request.forms
            addResult = add_project(projectInfo)
            return "added"
        elif crud == 'read':
            # in this situation, project info is checked with readonly
            fetchResult = fetch_document('project', 'project_no', project_id)
            print(fetchResult.keys)
            fetchResult["is_read"] = 1
            return template('tpl/projectInfo', **fetchResult)
        elif crud == 'update':
            # send back the stored data according to project_id return result
            pass
    else:
        redirect("/main")

@route('/quotation', method=['GET', 'POST'])
def quotation():

    if request.POST.save:
        request_dict = request.forms
        print(str(request_dict))
        return "success"
    else:
        return template('tpl/CBDInjection')

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)

app = bottle.default_app()
