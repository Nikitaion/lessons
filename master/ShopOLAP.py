def ShopOLAP(N, items):
  result = []
  st_items = {}

  for i in range(len(items)):
    item = items[i].split()
    if st_items.get(item[0]) == None:
      st_items[item[0]] = int(item[1])
    else:
      st_items[item[0]] += int(item[1])

  sr_item = sorted(st_items.items())
  sr_item.sort(key=lambda numb: numb[1], reverse=True)

  for i in sr_item:
    result.append(i[0] + ' ' + str(i[1]))

  return result