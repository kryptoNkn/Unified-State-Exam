s = '2'*2+'1'*2024+'2'*2
while '2111' in s or '1112' in s:
    s = s.replace('111','1',1)
    if '21' in s:
        s = s.replace('21','12',1)
    else:
        s = s.replace('12','1',1)
print(s)
