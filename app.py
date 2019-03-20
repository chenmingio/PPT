import bottle
import jinja2
import uuid
import pymongo

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
            remove_document('project', 'project_no', requestForm['project_no'] )
            saveResult = save_project(requestForm)
            redirect ("/main")
    else:
            "test failed"





@route('/project/<project_id>/info/<crud>', method=['GET', 'POST'])
def project(crud, project_id):
    '''crud: create/read/update/delete + save'''



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
            addResult = save_project(projectInfo)
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

# TODO forbid the user to change default/templete
# TODO mongodb has uuid support
# TODO: if the project_id changes, how to solve? if there's a blank in project id... 
