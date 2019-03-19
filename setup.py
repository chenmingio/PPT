from pymongo import MongoClient
import collections

# connect to local Mongodb
client = MongoClient()

# connect to Mongo Atlas Remote
# client = MongoClient("mongodb+srv://chenming123:chenming123@cmcluster-s42od.mongodb.net/test?retryWrites=true")



# connect to db-PPT
db = client.PPT


# connect to collection project
# project = db.project


# create user dict for pur
dict_pur = {
    "user_name" : "pur",
    "password" : "666",
    "user_group" : "PUR",
    "token" : "ssss"
}

# create user dict for supplier
dict_supplier = {
    "user_name" : "supplier",
    "password" : "111",
    "user_group" : "Supplier",
    "token" : "ssss"
}

# create user dict for pjm
dict_pjm = {
    "user_name" : "pjm",
    "password" : "111",
    "user_group" : "PJM",
    "token" : "ssss"
}

suggest_dict = {'project_no': 'same_as_key', 'project_name': 'project_name', 'production_line': 'production_line', 'fg_no': 'fg_no', 'product_cycletime': 'product_cycletime', 'runrate_hella': 'runrate_hella', 'pv_hella': 'pv_hella', 'sop_hella': 'sop_hella', 'sop_customer': 'sop_customer', 't3_date': 't3_date', 't4_date': 't4_date', 'pv_supplier': 'pv_supplier', 'purchasing': 'purchasing', 'pjm': 'pjm', 'md': 'md', 'sqa_ttm': 'sqa_ttm', 'controlling': 'controlling', 'me': 'me', 'planner': 'planner', 'year1_volume': 'year1_volume', 'year2_volume': 'year2_volume', 'year3_volume': 'year3_volume', 'year4_volume': 'year4_volume', 'year5_volume': 'year5_volume', 'year6_volume': 'year6_volume', 'year7_volume': 'year7_volume', 'year8_volume': 'year8_volume', 'year9_volume': 'year9_volume', 'year10_volume': 'year10_volume', 'part1_pn': 'part1_pn', 'part1_description': 'part1_description', 'part1_usage': 'part1_usage', 'part1_target_price': 'part1_target_price', 'part1_target_invest': 'part1_target_invest', 'part2_pn': 'part2_pn', 'part2_description': 'part2_description', 'part2_usage': 'part2_usage', 'part2_target_price': 'part2_target_price', 'part2_target_invest': 'part2_target_invest', 'part3_pn': 'part3_pn', 'part3_description': 'part3_description', 'part3_usage': 'part3_usage', 'part3_target_price': 'part3_target_price', 'part3_target_invest': 'part3_target_invest', 'part4_pn': 'part4_pn', 'part4_description': 'part4_description', 'part4_usage': 'part4_usage', 'part4_target_price': 'part4_target_price', 'part4_target_invest': 'part4_target_invest', 'part5_pn': 'part5_pn', 'part5_description': 'part5_description', 'part5_usage': 'part5_usage', 'part5_target_price': 'part5_target_price', 'part5_target_invest': 'part5_target_invest', 'save': 'save'}

def insert_document(collection_name, dict):
    '''insert dict into collection_name as a document'''

    collection = getattr(db, collection_name)
    result = collection.insert_one(dict)
    print(result)


def create_standart_dict(dict):
    '''create a dict with project key with value=key'''

    for itemstring in iter(dict):
        dict[itemstring] = str(itemstring)

        return dict

def fetch_document(collection_name, key, value):
    '''return the document in a collection according to its key and vaule'''

    collection = getattr(db, collection_name)
    query = {key: value}
    result = collection.find_one(query)
    return result

# new_dict = create_standart_dict(dict_pur)
# print(new_dict)
# insert_document('project', suggest_dict)

resultDict = fetch_document('project', 'project_no', 'project_no')


projectInfoKeyList = ['project_no', 'project_name', 'production_line', 'fg_no', 'product_cycletime', 'runrate_hella', 'pv_hella', 'sop_hella', 'sop_customer', 't3_date', 't4_date', 'pv_supplier', 'purchasing', 'pjm', 'md', 'sqa_ttm', 'controlling', 'me', 'planner', 'year1_volume', 'year2_volume', 'year3_volume', 'year4_volume', 'year5_volume', 'year6_volume', 'year7_volume', 'year8_volume', 'year9_volume', 'year10_volume', 'part1_pn', 'part1_description', 'part1_usage', 'part1_target_price', 'part1_target_invest', 'part2_pn', 'part2_description', 'part2_usage', 'part2_target_price', 'part2_target_invest', 'part3_pn', 'part3_description', 'part3_usage', 'part3_target_price', 'part3_target_invest', 'part4_pn', 'part4_description', 'part4_usage', 'part4_target_price', 'part4_target_invest', 'part5_pn', 'part5_description', 'part5_usage', 'part5_target_price', 'part5_target_invest']

textDict = {'project_no': 'Project Number', 'project_name': 'Project Name', 'production_line': 'Production Line', 'fg_no': 'FG Number', 'product_cycletime': 'Product Cycletime', 'runrate_hella': 'Run&Rate @Hella', 'pv_hella': 'PV @hella', 'sop_hella': 'SOP @hella', 'sop_customer': 'SOP @Customer', 't3_date': 'T3 Sample Date', 't4_date': 'T4 Sample Date', 'pv_supplier': 'PV Sample', 'purchasing': 'Purchasing', 'pjm': 'PJM', 'md': 'MD', 'sqa_ttm': 'SQA_TtM<', 'controlling': 'Controlling', 'me': 'ME', 'planner': 'Planner', 'year1_volume': 'Year-1 Volume', 'year2_volume': 'Year-2 Volume', 'year3_volume': 'Year-3 Volume', 'year4_volume': 'Year-4 Volume', 'year5_volume': 'Year-5 Volume', 'year6_volume': 'Year-6 Volume', 'year7_volume': 'Year-7 volume', 'year8_volume': 'Year-8 Volume', 'year9_volume': 'Year-9 Volume', 'year10_volume': 'Year-10 Volume', 'part1_pn': 'Part-1 Pn', 'part1_description': 'Part-1 Description', 'part1_usage': 'Part-1 Usage', 'part1_target_price': 'Part-1 Target Price', 'part1_target_invest': 'Part-1 Target Invest', 'part2_pn': 'Part-2 PN', 'part2_description': 'Part-2 Description', 'part2_usage': 'Part-2 Usage', 'part2_target_price': 'Part-2 Target Price', 'part2_target_invest': 'Part-2 Target Invest', 'part3_pn': 'Part-3 PN', 'part3_description': 'Part-3 Description', 'part3_usage': 'Part-3 Usage', 'part3_target_price': 'Part-3 Target Price', 'part3_target_invest': 'Part-3 Target Invest', 'part4_pn': 'Part4 PN', 'part4_description': 'Part-4 Description', 'part4_usage': 'Part-4 Usage', 'part4_target_price': 'Part-4 Target Price', 'part4_target_invest': 'Part-4 Target Invest', 'part5_pn': 'Part-5 PN', 'part5_description': 'Part-5 Description', 'part5_usage': 'Part-5 Usage', 'part5_target_price': 'Part-5 Target Price', 'part5_target_invest': 'Part-5 Target Invest'}

styleDict = {'project_no': 'col-md-4', 'project_name': 'col-md-4', 'production_line': 'col-md-4', 'fg_no': 'col-md-4', 'product_cycletime': 'col-md-4', 'runrate_hella': 'col-md-3', 'pv_hella': 'col-md-3', 'sop_hella': 'col-md-3', 'sop_customer': 'col-md-3', 't3_date': 'col-md-3', 't4_date': 'col-md-3', 'pv_supplier': 'col-md-3', 'purchasing': 'col-md-3', 'pjm': 'col-md-3', 'md': 'col-md-3', 'sqa_ttm': 'col-md-3', 'controlling': 'col-md-3', 'me': 'col-md-3', 'planner': 'col-md-3', 'year1_volume': 'col-md-1', 'year2_volume': 'col-md-1', 'year3_volume': 'col-md-1', 'year4_volume': 'col-md-1', 'year5_volume': 'col-md-1', 'year6_volume': 'col-md-1', 'year7_volume': 'col-md-1', 'year8_volume': 'col-md-1', 'year9_volume': 'col-md-1', 'year10_volume': 'col-md-1', 'part1_pn': 'col-md-2', 'part1_description': 'col-md-2', 'part1_usage': 'col-md-2', 'part1_target_price': 'col-md-2', 'part1_target_invest': 'col-md-2', 'part2_pn': 'col-md-2', 'part2_description': 'col-md-2', 'part2_usage': 'col-md-2', 'part2_target_price': 'col-md-2', 'part2_target_invest': 'col-md-2', 'part3_pn': 'col-md-2', 'part3_description': 'col-md-2', 'part3_usage': 'col-md-2', 'part3_target_price': 'col-md-2', 'part3_target_invest': 'col-md-2', 'part4_pn': 'col-md-2', 'part4_description': 'col-md-2', 'part4_usage': 'col-md-2', 'part4_target_price': 'col-md-2', 'part4_target_invest': 'col-md-2', 'part5_pn': 'col-md-2', 'part5_description': 'col-md-2', 'part5_usage': 'col-md-2', 'part5_target_price': 'col-md-2', 'part5_target_invest': 'col-md-2'}

ProjectItem = collections.namedtuple('ProjectItem', ['key', 'value', 'text', 'style'])


foo = [ProjectItem(key, resultDict[key], textDict[key], styleDict[key]) for key in projectInfoKeyList]

print(foo)
