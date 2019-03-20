import bottle
import jinja2
import uuid
import pymongo

route = bottle.route
run = bottle.run
request = bottle.request
response = bottle.response
debug = bottle.debug
redirect = bottle.redirect
view = bottle.jinja2_view
static_file = bottle.static_file

MongoClient = pymongo.MongoClient


# connect to db
client = MongoClient()
db = client.PPT


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

def remove_document(collection_name, key, value):
    ''' pass '''

    collection = getattr(db, collection_name)
    query = {key: value}
    collection.remove(query)

def find_info(collection_name, queryDict, fieldList):
    collection = getattr(db, collection_name)
    query = queryDict
    fields = {item : True for item in fieldList}
    cursor = collection.find(query, fields)
    return cursor



def save_project(projectInfo):
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


@route('/login', method=['GET', 'POST'])
@view('login.html', template_lookup=['templates'])
def login():

    if request.POST.login:
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
        return {'title': "Hello World"}

@route('/')
@route('/main')
@view('main.html', template_lookup=['templates'])
def main():
    userDoc = get_session(request)

    if userDoc:
        userGroup = userDoc['user_group']
        userName = userDoc['user_name']

        # extract all project names according to userName
        query = {userGroup : userName}
        fields = ['project_no', 'project_name', 't3_date', 't4_date']
        findInfoResult = find_info('project', query, fields)
        resultDict = {}
        n = 1
        for dict in findInfoResult:
            print(dict)
            for field in fields:
                key = str(field) + str(n)
                value = dict[field]
                resultDict[key] = value
            n = n + 1

        print(resultDict)

        return resultDict
    else:
        redirect("/login")



@route('/project/<project_id>', method=['GET', 'POST'])
@view('project.html', template_lookup=['templates'])
def overview(project_id):
    '''an overview of certain project. Readonly. No form necessary.'''

    # TODO user authorization

    # fetch basic project Info
    fetchProjectInfo = fetch_document('project', 'project_no', project_id)
    return fetchProjectInfo

@route('/project/<project_id>/info/<crud>', method=['GET', 'POST'])
@view('projectInfo.html', template_lookup=['templates'])
def test(project_id, crud):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['PUR', 'PJM']:

        if crud == 'create':
            fetchResult = fetch_document('project', 'project_no', 'project_no')
            is_crud = f'is_{crud}'
            print(is_crud)
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'read':
            print(crud)
            fetchResult = fetch_document('project', 'project_no', project_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'update':
            # update is same as read. But use 'read' or 'update' just doesn't work!
            print(crud)
            fetchResult = fetch_document('project', 'project_no', project_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'save':
            requestForm = request.forms
            remove_document('project', 'project_no', requestForm['project_no'])
            saveResult = save_project(requestForm)
            redirect ("/main")
    else:
            "test failed"


@route('/quotation', method=['GET', 'POST'])
@view('quotation.html', template_lookup=['templates'])
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

# TODO forbid the user to change default/templete
# TODO mongodb has uuid support
# TODO: if the project_id changes, how to solve? if there's a blank in project id... 
