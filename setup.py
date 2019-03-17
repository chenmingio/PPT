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

# create user dict for supplier
dict_pjm = {
    "user_name" : "pjm",
    "password" : "111",
    "user_group" : "PJM",
    "token" : "ssss"
}

dict_project = {
    "project_no" : "qwert",
    "project_name" : "h",
    "production_line" : "h",
    "fg_no" : "lkh",
    "product_cycletime" : "lk",
    "runrate_hella" : "hlk",
    "pv_hella" : "hjk",
    "sop_hella" : "l",
    "sop_customer" : "j;l",
    "t3_date" : "j",
    "t4_date" : "lkj",
    "pv_supplier" : "l;k",
    "purchasing" : "jl",
    "pjm" : "jk",
    "md" : "j",
    "sqa_ttm" : "kg",
    "controlling" : "kjf",
    "me" : "jhgf",
    "planner" : "h",
    "year1_volume" : "gk",
    "year2_volume" : "hl",
    "year3_volume" : "g",
    "year4_volume" : "kjg",
    "year5_volume" : "lh",
    "year6_volume" : "kj",
    "year7_volume" : "hk",
    "year8_volume" : "hlk",
    "year9_volume" : "g",
    "year10_volume" : "g",
    "part1_pn" : "jg",
    "part1_description" : "j",
    "part1_usage" : "g",
    "part1_target_price" : "kh",
    "part1_target_invest" : "h",
    "part2_pn" : "lk",
    "part2_description" : "h",
    "part2_usage" : "g",
    "part2_target_price" : "jgh",
    "part2_target_invest" : "kh",
    "part3_pn" : "",
    "part3_description" : "hlk",
    "part3_usage" : "h",
    "part3_target_price" : "lkjh",
    "part3_target_invest" : "",
    "part4_pn" : "",
    "part4_description" : "",
    "part4_usage" : "",
    "part4_target_price" : "",
    "part4_target_invest" : "",
    "part5_pn" : "",
    "part5_description" : "",
    "part5_usage" : "",
    "part5_target_price" : "",
    "part5_target_invest" : "",
    "save" : "Save"
}


def insert_document(collection_name, dict):
    '''insert dict into collection_name'''

    collection = getattr(db, collection_name)
    result = collection.insert_one(dict)
    print(result)


for dict in (dict_supplier, dict_pjm, dict_pur):
    insert_document('user', dict)
