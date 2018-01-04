import json
account_file='db'
account_data={'egon':{'password':'123','salary':'15000'}}
# with open(account_file, 'w') as f:
#     acc_data = json.dump(account_data,f)



with open(account_file) as f:
    acc_data = json.load(f)
print(acc_data['egon']['password'])
