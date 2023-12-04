import pandas as pd

def task1(data):
    years = [2015, 2016, 2017, 2018]
    stats = ["H", "avg", "HR", "OBP"]
    data_results = {}
    for stat in stats:
        data_result = data.sort_values(by=stat)
        data_results[stat] = data_result
    
    for year in years:
        print(year)
        for stat in stats:
            data_result = data_results[stat][data_results[stat]['p_year'] == year]
            print(stat)
            print(data_result['batter_name'][:10])

def task2(data):
    data = data[data['p_year'] == 2018]
    data = data.sort_values(by='war')
    positions = ["포수", "1루수", "2루수", "3루수", "유격수", "좌익수", "중견수", "우익수"]
    for position in positions:
        data_result = data[data['cp'] == position]
        print(position)
        print(data_result['batter_name'][:1])

def task3(data):
    stats = ["R", "H", "HR", "RBI", "SB", "war", "avg", "OBP", "SLG"]
    result = -1
    answer = ""
    for stat in stats:
        cur_result = data['salary'].corr(data[stat])
        if cur_result > result:
            result = cur_result
            answer = stat
    
    print(answer)

data = pd.read_csv("2019_kbo_for_kaggle_v2.csv")
task1(data)
task2(data)
task3(data)