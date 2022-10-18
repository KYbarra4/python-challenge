import os
import csv

election_csv = os.path.join('..','Resources','election_data.csv')

#votes = []
#candidates = []
#total_votes=0

with open(election_csv) as csvfile:
    csvreader = csv.reader(election_csv, delimiter=',')

    next(csvreader)
    pypoll=list(csvreader)
    row_s = len(pypoll)
    can_list=list()
    can_count=list()

    for i in range(0,row_s):
        candidates = pypoll[i][2]
        can_count.append(candidates)

        if candidates not in can_list:
            can_list.append(candidates)

    poll_count=len(can_list)

    percent= list()
    votes= list()

    for j in range (0,poll_count):
      name=can_list[j]
      votes.append(can_count.count(name))
      vote_p=votes[j]/row_s
      percent.append(vote_p)

    can_win=votes.index(max(votes))

print('Election Results')
print('-------------------------')
print(f'Total Votes:{row_s:,}')
print('-------------------------')
for m in range (0,poll_count):
    print(f'{poll_count[m]} : {percent[m]} ({votes[m]:,})')
print('-------------------------')
print(f'Winner: {poll_count[can_win]}')
print('-------------------------')

