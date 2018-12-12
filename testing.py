import LoadDataset as LD

load_data = LD.LoadData('/Users/mdabdulkadir/WS1819/ADAI/imagetest')
X, Y = load_data.generate_data()
print('Original data: ', X)
print(Y)
X, y = load_data.shuffle_data(X,Y)

print('Shaffled data: ', X)
print(y)
