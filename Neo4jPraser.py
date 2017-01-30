import pandas as pd


headers = ['from','to','value','gas','gasPrice']

#read the file
df = pd.read_csv('./transactions.csv',header=None, names=headers);
#print(df)
df = df[df['from'].notnull()]
df = df[df['to'].notnull()]
df = df[df['from'].str.contains('0x')]
df = df[df['to'].str.contains('0x')]

#grouping the transaction based on the 'from header'
result = df.sort(['from'], ascending=[1])

#print(result)

#for each group operation
count = 0;
label_map = {}
unique_address = result['from'].append(result['to']).unique().tolist();
label = []
prefix = 'ad'
for i in range(0, len(unique_address)):
    label.append(prefix +str(i));
#print(label);

label_map = dict(zip(unique_address,label)) #{ 0x123124: ad1}
print(label_map)


relationships =dict() #{ from_addr#to_addr: [#transaction,#acc_value] }

for index, row in df.iterrows():
    append_addr = row['from']+'#'+row['to']
    if append_addr in relationships.keys():
        relationships[append_addr][0] += 1;
        relationships[append_addr][1] += float(row['value'])/1000000000; #conver to Gweitransactions (2).csv
    else: #base case
        relationships[append_addr] = [0,0];

print(relationships)


# CREATE (ad1: Address { name: "xd123145" }),
# 		(ad2: Address { name: "xd123146" }),
# 		(ad3: Address { name: "xd123147" }),
# 		(ad1)-[:SEND {number:1, acc_value: 15}] -> (ad2),
# 		(ad2)-[:SEND {number:2, acc_value: 20}] -> (ad1),
# 		(ad3)-[:SEND {number:10, acc_value: 5}] -> (ad2)


target = open('neo4j.txt', 'w')
target.write('CREATE')
target.write("\n")
for each in label_map:
    target.write("(" + label_map[each] + ":" +" Address " + "{name: '" +  each + "'}),")
    target.write("\n")





#write the relationship
#relationships =dict() #{ from_addr#to_addr: [#transaction,#acc_value] }
for each in relationships:
    from_node = each[0:42];
    print(from_node);
    to_node = each[43:];
    print(to_node);

    target.write("MATCH(a: Address {name:" + "'" + from_node + "'" + "})")
    target.write("\n")
    target.write("MATCH(b: Address {name:" + "'" + to_node + "'" + "})")
    target.write("\n")
    target.write("MERGE((a)-[:SEND {number:" + str(relationships[each][0]) +", acc_value:" +  str(relationships[each][1]) +"}]->(b))")
    target.write("\n")
    target.write("WITH 1 as dummy")
    target.write("\n")
    target.write("\n")















