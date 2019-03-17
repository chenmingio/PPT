from pymongo import MongoClient

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


# new_dict = create_standart_dict(dict_pur)
# print(new_dict)

insert_document('project', suggest_dict)

