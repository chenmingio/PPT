from pymongo import MongoClient

# connect to db
client = MongoClient()
db = client.PPT

# connect to collection project
project = db.project


# create userone dict
dict_userone = {
    "user_name" : "chenmingio",
    "password" : "666",
    "user_group" : "PUR",
    "token" : "ssss"
}

dict_project = {
    "_id" : ObjectId("5c8920f2f4a2c0c79c52e661"),
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


def insert_user(dict):
    '''insert user. Input a dict-object of user'''

    user = db.user
    user.insert_one(dict)
    print('success')

def insert_demo_project(dict):
    '''insert a demo project into mongodb'''

    project =db.project
    project.insert_one(dict)

insert_user(dict_userone)
insert_demo_project(dict_project)
