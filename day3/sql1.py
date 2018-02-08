#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio

import os
#分发功能
def sql_parse(sql):
    #找到用户想要使用哪种功能
    parse_func={
        'insert':insert_cmd,
        'delete':delete_cmd,
        'update':update_cmd,
        'select':select_cmd,
    }
    sql_l=sql.split()
    #提取命令的功能
    func=sql_l[0]
    res=''
    #判断用户的命令是否合法
    if func in parse_func:
        res=parse_func[func](sql_l)
    #不合法直接返回空
    return res

#各种不同的功能,定义不同的字典
def insert_cmd(sql_l):
    sql_dic={
        'func':insert,
        'into':[],
        'values':[]
    }
    return handle_parse(sql_l,sql_dic)

def delete_cmd(sql_l):
    sql_dic={
        'func':delete,
        'from':[],
        'where':[]
    }
    return handle_parse(sql_l,sql_dic)

def update_cmd(sql_l):
    sql_dic={
        'func':update,
        'update':[],
        'set':[],
        'where':[]
    }
    return handle_parse(sql_l,sql_dic)

def select_cmd(sql_l):
    sql_dic={
        'func':select,
        'select':[],
        'from':[],
        'where':[],
        'limit':[]
    }
    return handle_parse(sql_l,sql_dic)

#输入数据字典格式化
def handle_parse(sql_l,sql_dic):
    tag=False
    for item in sql_l:
        if tag and item in sql_dic:
            tag = False
        if not tag and item in sql_dic:
            tag = True
            #将关键字作为key
            key = item
            continue
        if tag:
            sql_dic[key].append(item)
    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))
    return sql_dic

#对用户输入的where子句后的条件格式化,每个子条件都改成列表形式
def where_parse(where_l):
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if len(i) == 0:continue
        if i in key:
            if len(char) != 0:
                # 将每一个小的过滤条件如,name>=1转换成['name','>=','1']
                char=three_parse(char)
                res.append(char)
            res.append(i)
            char=''
        else:
          char+=i
    else:
        char=three_parse(char)
        res.append(char)
    return res

#将每一个小的过滤条件如,name>=1转换成['name','>=','1']
def three_parse(exp_str):
    key=['>','=','<']
    res=[]
    char=''
    opt=''
    tag=False
    for i in exp_str:
        if i in key:
            tag=True
            if len(char) !=0:
                res.append(char)
                char=''
            opt+=i
        if not tag:
            char+=i
        if tag and i not in key:
            tag=False
            res.append(opt)
            opt=''
            char+=i
    else:
        res.append(char)
    # print('res is %s ' %res)
    #新增like功能
    if len(res) == 1:#['namelike_ale5']
        res=res[0].split('like')
        res.insert(1,'like')
    return res


#功能处理
def insert(sql_dic):
    db_name,table_name = sql_dic['into'][0].split(".")
    #获取最后一行代码的ID
    last_id = ""
    with open("%s/%s"%(db_name,table_name),mode="r",encoding="utf-8") as fr:
        content_list = fr.readlines()
        last_record = content_list[-1]
        last_id = last_record.split(",")[0]

    #拼出最后一行记录,在操作的过程中注意insert的返回值是None
    record_list = sql_dic['values'][0].split(",")
    record_list.insert(0,str(int(last_id)+1))
    record_line = ",".join(record_list)

    #向列表中写入记录
    with open("%s/%s"%(db_name, table_name), mode="a", encoding="utf-8") as fw:
        fw.write("\n"+record_line)
        #记住要刷新纪录
        fw.flush()
    return [['insert successful']]

def delete(sql_dic):
    db, table = sql_dic["from"][0].split(".")
    bak_file = table + ".swap"
    fr = open("%s/%s" % (db, table), "r", encoding="utf-8")
    where_res = where_action(fr, sql_dic["where"])
    fr.close()
    if len(where_res) == 0:
        return [["Delete records do not exist!"]]
    else:
        with open("%s/%s" % (db, table), 'r', encoding='utf-8') as r_file, \
                open('%s/%s' % (db,bak_file), 'w', encoding='utf-8') as w_file:
            del_count = 0
            for line in r_file:
                title = "id,name,age,phone,dept,enroll_date"
                dic = dict(zip(title.split(','), line.split(',')))
                filter_res = logic_action(dic, sql_dic.get('where'))
                if not filter_res:
                    w_file.write(line)
                else:
                    del_count += 1
            w_file.flush()
        os.remove("%s/%s" % (db, table))
        os.rename("%s/%s" % (db, bak_file), "%s/%s" % (db, table))
        return [["Total deletion of %s data" % len(where_res)]]

def update(sql_dic):
    #update db1.emp set id='sb' where name like alex
    db,table=sql_dic.get('update')[0].split('.')
    set=sql_dic.get('set')[0].split(',')
    set_l=[]
    for i in set:
        set_l.append(i.split('='))
    bak_file=table+".swap"
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        #更新计数
        update_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if filter_res:
                for i in set_l:
                    k=i[0]
                    v=i[-1].strip("'")
                    dic[k]=v
                line=[]
                for i in title.split(','):
                    line.append(dic[i])
                update_count+=1
                line=','.join(line)
            w_file.write(line)
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [['update successful,In total update %s' %update_count]]

def select(sql_dic):
    # print(sql_dic)
    #通过from获取对应的库名和表名
    db_name,table_name = sql_dic["from"][0].split(".")
    fr = open("%s/%s"%(db_name,table_name),"r",encoding="utf-8")
    # print(fr.read())
    #解析where语句中的内容
    where_list = where_action(fr,sql_dic["where"])
    #获取指定个数的行文本
    limit_list = limit_action(where_list,sql_dic.get("limit"))
    #获取指定字段个数的信息
    final_result = search_action(limit_list,sql_dic.get("select"))
    return final_result

def sql_action(sql_dic):
    # 执行sql的统一接口,用户输入什么功能调用什么模块
    return sql_dic.get('func')(sql_dic)

def where_action(fh,where_l):
    res=[]
    logic_l=['and','or','not']
    title="id,name,age,phone,dept,enroll_date"
    if len(where_l) !=0:
        for line in fh:
            dic=dict(zip(title.split(','),line.split(',')))
            logic_res=logic_action(dic,where_l)
            if logic_res:
                res.append(line.split(','))
    else:
        res=fh.readlines()
    return res

#where子判断
def logic_action(dic,where_l):
    res=[]
    # print('==\033[45;1m%s\033[0m==\033[48;1m%s\033[0m' %(dic,where_l))
    for exp in where_l:
        if type(exp) is list:
            exp_k,opt,exp_v=exp
            if exp[1] == '=':
                opt='%s=' %exp[1]
            if dic[exp_k].isdigit():
                dic_v=int(dic[exp_k])
                exp_v=int(exp_v)
            else:
                dic_v="'%s'" %dic[exp_k]
            if opt != 'like':
                exp=str(eval("%s%s%s" %(dic_v,opt,exp_v)))
            else:
                if exp_v in dic_v:
                    exp='True'
                else:
                    exp='False'
        res.append(exp)
    res=eval(' '.join(res))
    # print('==\033[45;1m%s\033[0m' %(res))
    return res

#limit条件
def limit_action(filter_res,limit_l):
    res=[]
    if len(limit_l) !=0:
        index=int(limit_l[0])
        res=filter_res[0:index]
    else:
        res=filter_res

    return res

def search_action(limit_res,select_l):
    res=[]
    fileds_l=[]
    title="id,name,age,phone,dept,enroll_date"
    if select_l[0] == '*':
        res=limit_res
        fileds_l=title.split(',')
    else:

        for record in limit_res:
            dic=dict(zip(title.split(','),record))
            # print("dic is %s " %dic)
            fileds_l=select_l[0].split(',')
            r_l=[]
            for i in fileds_l:
                r_l.append(dic[i].strip())
            res.append(r_l)

    return [fileds_l,res]

#人类可读
def hm(res):
    for i in res[-1]:
        print(i)

if __name__ == '__main__':#如果此程序为主入口程序
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit' or sql == 'q':
            break
        if len(sql) == 0 :
            continue
        #格式化输入语句
        sql_dic=sql_parse(sql)
        print(sql_dic)
        #如果为空则不合法.
        if len(sql_dic) == 0:
            continue
        #将格式化后的数据执行
        res=sql_action(sql_dic)
        hm(res)