def self_number(n):
  generate_set = set()
  number_set = set()
  for i in range(n): #n(여기서는 만개)개 까지의 값
    result = 0
    number_set.add(i)
    for j in str(i): #생성자 만들기
      result +=  int(j)
    result += int(i)
    generate_set.add(result)
    answer = sorted(number_set - generate_set)
  return answer

for _ in self_number(10000):
  print(_)