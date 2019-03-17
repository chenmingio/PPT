import bottle
import uuid
import pymongo

route = bottle.route
run = bottle.run
request = bottle.request
response = bottle.response
template = bottle.template
debug = bottle.debug
redirect = bottle.redirect

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


def fetch_user(key, value):
    '''fetch document in user collection with key and value. return the first one matches in dict-object'''

    # connect to collection user
    user = db.user
    # build query and get result
    query = {key: value}
    result = user.find_one(query)
    return result

def fetch_project(key, value):
    '''fetch document in project collection with key and value. return the first one matches in dict-object'''

    # connect to collection project
    project = db.project

    # build query and get result
    query = {key: value}
    result = project.find_one(query)
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

def FormsDict2PythonDict(FormsDict):
    pyDict = {}
    for item in FormsDict:
        pass




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


@route('/overview')
def overview():
    userDoc = get_session(request)
    return 'building...'


@route('/project/<project_id>', method=['GET', 'POST'])
def project(project_id):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['PUR', 'PJM']:
        if project_id == 'new':
            fetchSuggestion= fetch_document('project', 'project_no', 'qwert')
            fetchSuggestion["toggle"] = 'NA'
            return template('tpl/project', **fetchSuggestion)
        elif project_id == 'save':
            projectInfo = request.forms
            addResult = add_project(projectInfo)
            return "added"
        else:
            fetchResult = fetch_document('project', 'project_no', project_id)
            fetchResult["toggle"] = "readonly"
            return template('tpl/project', **fetchResult)
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
