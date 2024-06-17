team1_name = 'Code Masters'
team2_name = 'Data Wizards'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Использование %:
print('There are %s players in the %s team!' %(team1_num, team1_name))
print('We have totally %s players challenging - %s in one team and %s in another!' %(team1_num + team2_num, team1_num, team2_num))
# Использование format():
print('The {0} team solved {1} tasks!'.format(team2_name, score_2))
print('{0} spent just {1:.2f} seconds to solve all the tasks!'.format(team2_name, team2_time))
# Использование f-строк:
print(f'There were {score_1} and {score_2} tasks solved by teams!')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'{team1_name} wins!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'{team2_name} wins!'
else:
    result = 'Draw.'
print(f'Challenge result: {result}')
print(f'The were {score_1 + score_2} tasks solved today, \
{(team1_time + team2_time) / (score_1 + score_2):.2f} seconds a task in average!')