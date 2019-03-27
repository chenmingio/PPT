import bottle
import jinja2
import uuid
import pymongo
import time
import bson
import collections

route = bottle.route
run = bottle.run
request = bottle.request
response = bottle.response
debug = bottle.debug
redirect = bottle.redirect
view = bottle.jinja2_view
static_file = bottle.static_file

ObjectId = bson.ObjectId

MongoClient = pymongo.MongoClient


# connect to db
client = MongoClient()
db = client.PPT

def six_digit_id_generator():
    uuidString = str(uuid.uuid4())
    return uuidString[:7]


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

def save_document(collection_name, dict):
    '''insert dict into collection_name'''
    collection = getattr(db, collection_name)
    result = collection.insert_one(dict)



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

        if userGroup == 'supplier':
            # query =  { '$or': [{ f'supplier_{n}': userName } for n in range(1,6)] }
            query =  { '$or': [{ 'supplier_1': userName }, { 'supplier_2': userName }, { 'supplier_3': userName }, { 'supplier_4': userName }, { 'supplier_5': userName } ] }
            cursor = db.part.find(query)
            resultDict = {'userName': userName} # transfer username and then put project info inside
            cursorList = list(cursor)
            for n in range(len(cursorList)):
                resultDict[f'project_name{n + 1}'] = cursorList[n]["project_name"]
                resultDict[f'project_no{n + 1}'] = cursorList[n]["project_no"]
                resultDict[f'sourcing_date{n + 1}'] = cursorList[n]["sourcing_date"]

            resultDict['is_supplier'] = True
            return resultDict
        else:
            # extract all project names according to current userGroup and userName
            query = {userGroup : userName}
            fields = ['project_no', 'project_name', 't3_date', 't4_date']
            findInfoResult = find_info('project', query, fields)

            # put a no after every attribute like: project_name1, t3_date2, t4_date3 ... # TODO later use project1.attr to transfer. Then use for loop to expand
            resultDict = {'userName': userName} # transfer username and then put project info inside
            n = 1
            for dict in findInfoResult:
                for field in fields:
                    key = str(field) + str(n)
                    value = dict[field]
                    resultDict[key] = value
                n = n + 1

            return resultDict
    else:
        redirect("/login")



@route('/project/<project_id>', method=['GET', 'POST'])
@view('project.html', template_lookup=['templates'])
def overview(project_id):
    '''an overview of certain project. Readonly. No form necessary.'''

    userDoc = get_session(request)
    userGroup = userDoc['user_group']

    if userGroup in ['purchasing', 'supplier', 'pjm']: # may remove if

        # TODO add a guard to make sure project purchasing name = userName

        # fetch basic project Info
        fetchProjectInfo = fetch_document('project', 'project_no', project_id)

        fetchProjectInfo[f"is_{userGroup}"] = True
        return fetchProjectInfo
    else:
        return 'Purchasing ONLY'





@route('/project/<project_id>/info/<crud>', method=['GET', 'POST'])
@view('projectInfo.html', template_lookup=['templates'])
def projectinfo(project_id, crud):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['purchasing', 'pjm']:

        if crud == 'create':
            fetchResult = fetch_document('project', 'project_no', 'suggestion')
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            idDict = {f'part{n}_id': six_digit_id_generator() for n in range(1,6)}
            fetchResult.update(idDict)
            return fetchResult
        elif crud == 'read':
            fetchResult = fetch_document('project', 'project_no', project_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'update':
            # update is same as read. But use 'read' or 'update' just doesn't work!
            fetchResult = fetch_document('project', 'project_no', project_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'save':
            requestForm = request.forms
            remove_document('project', 'project_no', requestForm['project_no'])
            saveResult = save_project(requestForm) # why not use insertdocument
            redirect ("/main")
    else:
            "test failed"

@route('/part/<part_id>/<crud>', method=['GET', 'POST'])
@view('part.html', template_lookup=['templates'])
def part(part_id, crud):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['purchasing', 'supplier']:

        if crud == 'create':
            # need to find the project with partn_id equals part_id here? Have to be like this?
            query =  { '$or': [ { 'part1_id': part_id }, { 'part2_id': part_id }, { 'part3_id': part_id }, { 'part4_id': part_id }, { 'part5_id': part_id }, ] }
            fetchResult = db.project.find_one(query)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            fetchResult['part_id'] = part_id # because only partn_id will be return

            # get lifetime volume for PVO calculation
            total_volume = 0
            lifetime = 0
            for year in range(1,11):
                if fetchResult[f'year{year}_volume'] != '0':
                    total_volume += int(fetchResult[f'year{year}_volume'])
                    lifetime += 1

            average_volume = total_volume / lifetime

            # check which part is this part and return its current_pn
            for n in range(1,6):
                if fetchResult[f'part{n}_id'] == part_id:
                    fetchResult['current_pn'] = fetchResult[f'part{n}_pn']
                    fetchResult['yearly_pvo'] = average_volume * float(fetchResult[f'part{n}_target_price'])

            return fetchResult

        elif crud == 'read':
            fetchResult = fetch_document('part', 'part_id', part_id)

            # if not exist yet, redirect to create
            if fetchResult:
                is_crud = f'is_{crud}'
                fetchResult[is_crud] = True
                return fetchResult
            else:
                redirect(f"/part/{part_id}/create")
        elif crud == 'update':
            # update is same as read. But use 'read' or 'update' just doesn't work!
            fetchResult = fetch_document('part', 'part_id', part_id)
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'save':
            requestForm = request.forms
            remove_document('part', 'part_id', part_id)
            saveResult = insert_document('part', requestForm)
            redirect ("/main")
    else:
            "test failed"

@route('/quotation/<part_id>/<crud>', method=['GET', 'POST'])
@view('quotation.html', template_lookup=['templates'])
def quotation(part_id, crud):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['purchasing', 'supplier']:
        userName = userDoc['user_name']

        if crud == 'create':
            uuidString = str(uuid.uuid4())
            fetchResult = fetch_document('quotation', 'author', 'suggestion')
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            fetchResult['part_id'] = part_id
            fetchResult['quotation_id'] = uuidString[:7]
            return fetchResult
        elif crud == 'update':
            # find document in quotaiton where partid is partid and author is username
            query =  { '$and': [ { 'part_id': part_id }, { 'author': userName}] }
            fetchResult = list(db.quotation.find(query))[-1]
            uuidString = str(uuid.uuid4())
            newQuotationId = uuidString[:7]
            fetchResult['quotation_id'] = newQuotationId
            is_crud = f'is_{crud}'
            fetchResult[is_crud] = True
            return fetchResult
        elif crud == 'read':
            # find document in quotaiton where partid is partid and author is username
            query =  { '$and': [ { 'part_id': part_id }, { 'author': userName}] }
            fetchResults = list(db.quotation.find(query))
            # if not exist yet, redicret to create
            if fetchResults:
                fetchResult = fetchResults[-1]
                is_crud = f'is_{crud}'
                fetchResult[is_crud] = True
                quotationDate = str(fetchResult['_id'].generation_time)
                fetchResult['quotation_date']
                return fetchResult
            else:
                redirect(f"/quotation/{part_id}/create")
        elif crud == 'save':
            requestForm = request.forms
            requestForm['author'] = userName
            insert_document('quotation', requestForm)
            redirect ("/main")
    else:
        return "only for purchaing and supplier"

@route('/compare/<part_id>')
@view('compare.html', template_lookup=['templates'])
def compare(part_id):

    userDoc = get_session(request)

    if userDoc['user_group'] in ['purchasing']:

        # get supplier names from part/strategy page:
        result = fetch_document('part', 'part_id', part_id)
        compareList = {}
        for n in range(1, 6):
            supplierName = result[f'supplier_{n}']
            query =  { '$and': [ { 'part_id': part_id }, { 'author': supplierName}] }
            quotation = list(db.quotation.find(query).sort('_id', pymongo.DESCENDING))
            if quotation:
                quotation[0]['supplier_name'] = supplierName
                compareList[f'supplier_{n}'] = quotation[0]
            else:
                compareList[f'supplier_{n}'] = {"supplier_name" : supplierName}
        return compareList
    else:
        return 'only for purchasing'









if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)

app = bottle.default_app()

# TODO forbid the user to change default/templete
# TODO mongodb has uuid support
# TODO: if the project_id changes, how to solve? if there's a blank in project id... 
# TODO: thinking about use class to contain data (Class Quotation/Project...)
# TODO: minimize the return fields
