counts = dict()
names = ['csev', 'zwen', 'ken', 'ten']
for name in names:
  if name not in counts:
     count[name] = 1
  else:
     count[name] = count[name] + 1
print(counts)


// x= counts.get(key, deafult_value)


