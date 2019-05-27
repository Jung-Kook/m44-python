# lunch_menu.py

import random

# menu 리스트를 만들어주세요.
menu = ["떡볶이","초밥","바스버거","할스","백수산","감자탕"]
phonebook = {"떡볶이": '123-456'
             , "초밥": '987-654'
             , "바스버거": '1004-1004'
             , "할스": '456-789'
             , "백수산": '321-654'
             , "감자탕": '159-357'}
choice = random.choice(menu)
print(f"오늘의 점심은 {choice} 입니다.")
print(f"전화번호는 {phonebook[choice]} 입니다.")