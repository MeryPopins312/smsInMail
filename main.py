import smtplib
import os

my_login = os.environ['LOGIN']
my_password = os.environ['PASSWORD']

mail = 'https://dvmn.org/referrals/dKtkrWYmHIpDm3tqImpmcu1F84Shh2keFSaO10p4/'
friend_name = 'Малика'
my_name = 'Мэри'
letter = """From: il.os1pov@yandex.ru
To: merypopins312@yandex.ru
Subject: Приглашение !
Content-Type: text/plain; charset="UTF-8";"""

text = """{a}
Привет, {f}! {m} приглашает тебя на сайт {w}!

{w} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {w}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {w}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(w = mail , f = friend_name , m = my_name , a = letter)
text = text.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(my_login ,my_password)
server.sendmail('il.os1pov@yandex.ru','merypopins312@yandex.ru', text)
server.quit()

print(text)


