#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
def sql_parse(sql):
    #分析用户具体需要哪个功能,交给具体的功能去操作
    parse_func={
        'insert':insert_cmd,
        'delete':delete_cmd,
        'update':update_cmd,
        'select':select_cmd,
    }
    sql_l=sql.split(' ')
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
        return res

#各种不同的功能,定义不同的字典
def insert_cmd(sql_1):
    sql_dic={
        'func':insert,
        'into':[],
        'values':[]
    }
    return handle_parse(sql_1,sql_dic)

def delete_cmd(sql_1):
    sql_dic={
        'func':delete,
        'from':[],
        'where':[]
    }
    return handle_parse(sql_1,sql_dic)

def update_cmd(sql_1):
    sql_dic={
        'func':update,
        'update':[],
        'set':[],
        'where':[]
    }
    return handle_parse(sql_1,sql_dic)

def select_cmd(sql_1):
    sql_dic={
        'func':select,
        'select':[],
        'from':[],
        'where':[],
        'limit':[],
    }
    return handle_parse(sql_1,sql_dic)

def handle_parse(sql_1,sql_dic):
    # 讲用户输入的数据转换成列表后填充到字典中
    tag=False
    for item in sql_1:
        if item in sql_dic:
            tag=True
            key=item
        if tag and item not in sql_dic:
            sql_dic[key].append(item)
    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))
        # print(sql_dic)
    return sql_dic


def where_parse(where_list):
    #function:对where中的条件进行进一步的处理
    where_result = []
    sens_list = ["and","or","not"]
    key_word = ""
    temp = []
    if where_list:
        tag = False
        for item in where_list:
            if item in sens_list:
                tag = True
                key_word = item
                if temp:where_result.append(temp)
                temp = []
            if not tag and  item not in sens_list:
                temp.append(item)
            if tag and item not in sens_list:
                tag = False
                where_result.append(key_word)
                key_word = ""
                temp.append(item)
        else:
            where_result.append(temp)

    return where_result


def sql_action(sql_dic):
    # 执行
    return sql_dic["func"](sql_dic)

def select_parse(sql):
    """
    function:该函数的功能是进行select查询操作
    :param sql: 用户传进来的sql语句
    :return: 返回操作日志
    """
    #定义一个存储结构,以字典的形式进行存储
    sql_list = sql.split()
    #用一个字典结构去存储相应的数据，方便处理数据
    sql_dict = handle_parse_select(sql_list)

    return sql_dict

def handle_parse_select(sql_list):
    """
    function:用字典的形式去存储数据
    :param sql_list: 用户传进来的sql_list列表
    :return: 返回字典形式的数据
    """
    sql_dict = {
        "select":[],
        "from":[],
        "where":[],
        "limit":[]
    }

    # 接下来就是如何将列表中的内容对号入座的放到相应的字典当中，利用到了警报
    tag = False
    key = ""
    for item in sql_list:
        if tag and item in sql_dict:
            tag = False
        if not tag and item in sql_dict:
            tag = True
            key = item
            continue
        if tag:
            sql_dict[key].append(item)
    #此时我们需要对where中的条件进行一步的清洗处理
    #现在的where条件：['id', '>', '10', 'and', 'id', '<', '14', 'or', 'name', 'like', '李']
    #需要处理成的形式:[['id', '>', '10'], 'and', ['id', '<', '14'], 'or', ['name', 'like', '李']]
    #需要处理成的形式:['not', ['id', '>=', '3']]
    if  sql_dict['where']:
        sql_dict['where'] = where_parse(sql_dict['where'])

    return sql_dict

def where_parse(where_list):
    """
    function:该函数的作用是对where中的条件进行进一步的处理
    :param sql_dict: ['id', '>', '10', 'and', 'id', '<', '14', 'or', 'name', 'like', '李']
    :return: ['not', ['id', '>=', '3']]
    """
    sens_list = ['and','or','not']
    where_result = []
    temp = []
    opt = ""

    tag = False
    for item in where_list:
        if item in sens_list:
            tag = True
            #通过if条件来限制not这种情况
            if temp:
                where_result.append(temp)
            temp = []   #注意：此处不能用list.clear(temp)
            opt = item
        if not tag and item not in sens_list:
            temp.append(item)
        if tag and item not in sens_list:
            tag = False
            where_result.append(opt)
            opt = ""
            temp.append(item)
    else:
        where_result.append(temp)

    return where_result

def select(sql_dict):
    """
    function：进一步实现查询功能
    :param sql_dict: 用户传进来的字典形式的数据
    :return: 日志列表
    """
    #1、先通过from获取对应的库名和表名
    # print(sql_dic)
    db_name,table_name = sql_dict["from"][0].split(".")
    fr = open("%s/%s"%(db_name,table_name),"r",encoding="utf-8")
    # print(fr.read())
    #2、我们去解析where语句中的内容
    where_list = where_action(fr,sql_dict["where"])
    #3、获取指定个数的行文本
    limit_list = limit_action(where_list,sql_dict.get("limit"))
    #4、获取指定字段个数的信息
    final_result = search_action(limit_list,sql_dict.get("select"))

    print(final_result)
    # return final_result

def search_action(limit_list,select_list):
    """
    function:本函数的功能是获取指定字段个数的数据
    :param limit_list: list列表
    :param select_list: [id,name]
    :return: 返回一个指定字段的集合
    """
    #final_result用来存放最终的结果集合
    final_result = []
    title = "id,name,age,phone,dept,enroll_data"
    #先考虑*的情况
    if select_list[0] == "*":
        final_result = limit_list
    else:
        fields_list = select_list[0].split(",")
        for line in limit_list:
            user_info = dict(zip(title.split(","),line.split(",")))
            #用一个临时列表去存放中间数据
            r_l = []
            for field in fields_list:
                r_l.append(user_info[field])

            final_result.append(r_l)

    return final_result

def limit_action(where_list,limit_list):
    """
    function:获取指定个数的行文本：
    :param where_list: ['2,李四,25,19230267967,运维,2016-5-27\n', '6,李张明,26,18122677967,测试,2017-5-21\n']
    :param limit_num: 数值
    :return:
    """
    limit_res = []

    if  limit_list:
        where_list  = where_list[0:int(limit_list[0])]
    return where_list

def where_action(fr,where_list):
    """
    function：通过where中的条件对文件中的内容进行过滤
    :param fr: 文件的句柄
    :param where_list: where列表中的内容
    :return: 返回一个列表的内容
    """
    #res_list用于存放结果集
    res_list = []
    #先考虑是否含有where条件
    if  where_list:
        title = "id,name,age,phone,dept,enroll_date"
        for line in fr.readlines():
            user_dict = dict(zip(title.split(","),line.strip().split(",")))
            #用logic_action
            logic_res = logic_action(user_dict,where_list)
            if logic_res:
                res_list.append(line)

    #在考虑无where条件
    else:
        res_list = fr.readlines()

    return res_list

def logic_action(user_dict,where_list):
    """
    function:通过where列表中的条件对文本进行过滤操作
    :param user_dict: 用户的记录字典形式：单行文本
    :param where_list: where条件列表形式[['id', '>', '10'], 'and', ['id', '<', '14'], 'or', ['name', 'like', '李']]
    :return: 返回逻辑值真或假
    """
    logic_result = []
    for item in where_list:
        if (type(item) == list):
            field,label,value = item
            line_value = user_dict[field]
            if label == "=":
                label = "=="
            if value.isdigit():
                value = int(value)
                line_value = int(line_value)
            if label != 'like':
                item = str(eval("%s%s%s" %(line_value,label,value)))
            else:
                if value in line_value:
                    item = 'True'
                else:
                    item = 'False'
        #如果不是列表类型,就是敏感词汇，此时直接加入到logic_result当中
        logic_result.append(item)
    logic_str = ' '.join(logic_result)
    logic_res = eval("%s"%logic_str)

    return logic_res

def insert(sql_list):
    """
    function:该函数的功能是进行文本插入操作
    :param sql: 用户传进来的sql语句
    :return: 无
    """
    db_name,table_name = sql_list['into'][0].split(".")
    #获取最后一行代码的ID
    last_id = ""
    with open("%s/%s"%(db_name,table_name),mode="r",encoding="utf-8") as fr:
        content_list = fr.readlines()
        last_record = content_list[-1]
        last_id = last_record.split(",")[0]

    #拼出最后一行记录,在操作的过程中注意insert的返回值是None
    record_list = sql_list['values'][0].split(",")
    record_list.insert(0,str(int(last_id)+1))
    record_line = ",".join(record_list)

    #向列表中写入记录
    with open("%s/%s"%(db_name, table_name), mode="a", encoding="utf-8") as fw:
        fw.write("\n"+record_line)
        #记住要刷新纪录
        fw.flush()


def delete(sql_dic):
    """
    function:该函数的功能是删除表中指定的行,此处我的where条件就是=号的方式
    :param sql:用户传进来的SQL语句
    :return: 返回值是删除的记录条数和删除是否成功
    """
    db_name, table_name = sql_dic["from"][0].split(".")
    filename = "%s/%s" % (db_name,table_name)
    filename_new = filename + ".swap"
    file = open(filename, 'r', encoding="utf-8")
    where_res = where_action(file, sql_dic["where"])
    file.close()
    if len(where_res) == 0:
        print ("删除记录不存在！")
    else:
        tmp = []
        for line in where_res:
            tmp.append(line.strip())
        with open(filename, 'r', encoding="utf-8") as f, \
                open(filename_new, 'w', encoding="utf-8") as f1:
            id = 0
            for f_line in f:
                if f_line.strip() in tmp:
                    continue
                else:
                    id = 1 + id
                    con = f_line.strip("'").split(",")
                    con = f_line.strip('"').split(",")
                    con[0] = str(id)
                    content = ",".join(con)
                    f1.write(content)
            f1.flush()
        os.rename(filename, filename + "b")
        os.rename(filename_new, filename)
        os.remove(filename + "b")
        print ("共计删除%s条数据" % len(where_res))

def update(sql_dic):
    """
    function:用于进行记录插入操作
    :param sql: 用户传进来的sql语句
    :return: 日志列表
    """
    db_name,table_name = sql_dic['update'][0].split(".")
    #创建备份文件的名字
    back_name = table_name+".swap"

    # print("sql_list is \033[41;1m%s\033[0m"%sql_list)
    change_field = sql_dic['set'][0]
    change_value = sql_dic['set'][2]
    where_field = sql.partition("where")[2].split("=")[0].strip()
    where_value = sql.partition("where")[2].split("=")[1].strip()

    title = "id,name,age,phone,dept,enroll_date"
    update_count = 0
    with open("%s/%s"%(db_name,table_name),"r",encoding="utf-8") as fr, \
        open("%s/%s"%(db_name,back_name),"w",encoding="utf-8") as fw:
        for line in fr.readlines():
            #拼出用户的相关信息
            user_info = dict(zip(title.split(","),line.strip().split(",")))
            if user_info[where_field] == where_value:
                user_info[change_field] = change_value.strip("'")
                #构建插入的记录
                line_list = []
                #下面这一步骤值得学习:先转化成list,在拼接成字符串
                for i in title.split(","):
                    line_list.append(user_info.get(i))
                line_record = ",".join(line_list)
                fw.write(line_record+"\n")
                update_count += 1
            else:
                fw.write(line)
        #所有操作完之后之后再刷新一下缓冲区
        fw.flush()

    os.remove("%s/%s" % (db_name, table_name))
    os.rename("%s/%s" % (db_name, back_name), "%s/%s" % (db_name, table_name))

    print(update_count,"update successful")


if __name__ == '__main__':
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':
            break
        if len(sql) == 0 :
            continue
        sql_dic=sql_parse(sql)
        if len(sql_dic) == 0:
            continue
        res=sql_action(sql_dic)