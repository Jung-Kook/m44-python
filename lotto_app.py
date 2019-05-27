# 아래에 코드를 작성하세요.
# 1-45의 숫자 중 중복되지 않는 랜덤 6개 숫자를 뽑아서 출력하는 앱을 만들어 보세요!

import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)

print(sorted(lotto))
print(f'행운의 숫자는 {sorted(lotto)[0]}, {sorted(lotto)[1]},'
      f' {sorted(lotto)[2]}, {sorted(lotto)[3]}, '
      f'{sorted(lotto)[4]}, {sorted(lotto)[5]} 입니다!')
