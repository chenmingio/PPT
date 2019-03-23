from pymongo import MongoClient
import collections

# connect to local Mongodb
client = MongoClient()

# connect to Mongo Atlas Remote
# client = MongoClient("mongodb+srv://chenming123:chenming123@cmcluster-s42od.mongodb.net/test?retryWrites=true")



# connect to db-PPT
db = client.PPT


suggest_projectInfo = {'project_no': 'suggestion', 'project_name': 'project_name', 'production_line': 'production_line', 'fg_no': 'fg_no', 'product_cycletime': 'product_cycletime', 'runrate_hella': 'runrate_hella', 'pv_hella': 'pv_hella', 'sop_hella': 'sop_hella', 'sop_customer': 'sop_customer', 't3_date': 't3_date', 't4_date': 't4_date', 'pv_supplier': 'pv_supplier', 'purchasing': 'purchasing', 'pjm': 'pjm', 'md': 'md', 'sqa_ttm': 'sqa_ttm', 'controlling': 'controlling', 'me': 'me', 'planner': 'planner', 'year1_volume': 'year1_volume', 'year2_volume': 'year2_volume', 'year3_volume': 'year3_volume', 'year4_volume': 'year4_volume', 'year5_volume': 'year5_volume', 'year6_volume': 'year6_volume', 'year7_volume': 'year7_volume', 'year8_volume': 'year8_volume', 'year9_volume': 'year9_volume', 'year10_volume': 'year10_volume', 'part1_pn': 'part1_pn', 'part1_description': 'part1_description', 'part1_usage': 'part1_usage', 'part1_target_price': 'part1_target_price', 'part1_target_invest': 'part1_target_invest', 'part2_pn': 'part2_pn', 'part2_description': 'part2_description', 'part2_usage': 'part2_usage', 'part2_target_price': 'part2_target_price', 'part2_target_invest': 'part2_target_invest', 'part3_pn': 'part3_pn', 'part3_description': 'part3_description', 'part3_usage': 'part3_usage', 'part3_target_price': 'part3_target_price', 'part3_target_invest': 'part3_target_invest', 'part4_pn': 'part4_pn', 'part4_description': 'part4_description', 'part4_usage': 'part4_usage', 'part4_target_price': 'part4_target_price', 'part4_target_invest': 'part4_target_invest', 'part5_pn': 'part5_pn', 'part5_description': 'part5_description', 'part5_usage': 'part5_usage', 'part5_target_price': 'part5_target_price', 'part5_target_invest': 'part5_target_invest', 'save': 'save'}

suggest_quotation = {'part_id': 'part_id', 'part_weight': 'part_weight', 'runner_weight': 'runner_weight', 'wastage': 'wastage', 'resin_moq': 'resin_moq', 'resin_price': 'resin_price', 'cavity': 'cavity', 'machine_tonnage': 'machine_tonnage', 'machine_rate': 'machine_rate', 'cycle_time': 'cycle_time', 'reject_allow': 'reject_allow', 'secpro_mtl': 'secpro_mtl', 'secpro_mtl_cost': 'secpro_mtl_cost', 'secpro_process_name': 'secpro_procss_name', 'secpro_process_cost': 'secpro_process_cost', 'part_moq': 'part_moq', 'packaging_concept': 'packaging_concept', 'packaging_cost': 'packaging_cost', 'profit': 'profit', 'overhead': 'overhead', 'tooling_lifetime': 'tooling_lifetime', 'injection_tooling_cost': 'injection_tooling_cost', 'measuring_cost': 'measuring_cost', 'copy_tooling_cost': 'copy_tooling_cost', 'extra_tooling_name': 'extra_tooling_name', 'extra_tooling_cost': 'extra_tooling_cost', 'extra_invest_name': 'extra_invest_name', 'extra_invest_cost': 'extra_invest_cost', 'year1_price': 'year1_price', 'year2_price': 'year2_price', 'year3_price': 'year3_price', 'year4_price': 'year4_price', 'year5_price': 'year5_price', 'year6_price': 'year6_price', 'year7_price': 'year7_price', 'year8_price': 'year8_price', 'year9_price': 'year9_price', 'year10_price': 'year10_price', 'first_qc_amount': 'first_qc_amount', 'first_qc_date': 'first_qc_date', 'second_qc_amount': 'second_qc_amount', 'second_qc_date': 'second_qc_date', 'submit': 'submit', 'author': 'suggestion'}

suggest_partInfo = {'current_pn': '1', 'part_id': '1', 'description': '1', 'mtl_group': '1', 'rfq_date': '1', 'fs_date': '1', 'log_date': '1', 'sourcing_date': '1', 'risk_analysis': '1', 'yearly_pvo': '1', 'sourcing_level': '1', 'supplier_1': '1', 'supplier_2': '1', 'supplier_3': '1', 'supplier_4': '1', 'supplier_5': '1'}

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


def suggestionBuilder(dict):
    for key in dict:
        quotationDict[key] = key
    print(quotationDict)


def insert_user_groups():
    '''insert 10x3 users into user collection'''

    userList = [{"user_name" : f"{user_group}{n}", "password" : "666", "user_group" : user_group} for n in range(21,31) for user_group in ['purchasing', 'pjm', 'supplier']]

    for dict in userList:
        insert_document('user', dict)


def insert_projectInfoSuggestion():
    '''please maintain suggestion at first'''
    insert_document('project', suggest_projectInfo)


def insert_quotationSuggestion():
    '''please maintain suggestion at first'''
    insert_document('quotation', suggest_quotation)

def insert_partSuggestion():
    '''please maintain suggestion at first'''
    insert_document('part', suggest_partInfo)

# insert_user_groups()
# insert_projectInfoSuggestion()
insert_quotationSuggestion()
# insert_partSuggestion()



