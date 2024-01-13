'''

Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
Знайти студента із найвищим середнім балом з певного предмета.
Знайти середній бал у групах з певного предмета.
Знайти середній бал на потоці (по всій таблиці оцінок).
Знайти які курси читає певний викладач.
Знайти список студентів у певній групі.
Знайти оцінки студентів у окремій групі з певного предмета.
Знайти середній бал, який ставить певний викладач зі своїх предметів.
Знайти список курсів, які відвідує певний студент.
Список курсів, які певному студенту читає певний викладач.
Для запитів оформити окремий файл my_select.py, де будуть 
10 функцій від select_1 до select_10. Виконання функцій 
повинно повертати результат аналогічний попередньої 
домашньої роботи. При запитах використовуємо механізм 
сесій SQLAlchemy.

Підказки та рекомендації
Це завдання перевірить вашу здатність користуватися документацією 
SQLAlchemy. Але основні підказки та напрямки рішення ми вам дамо одразу. 
Нехай у нас є наступний запит.

Знайти 5 студентів з найбільшим середнім балом з усіх предметів.
Спробуймо його перевести в запит ORM SQLAlchemy. Нехай у нас є 
сесія у змінній session. Є описані моделі Student та Grade для 
відповідних таблиць. Вважаємо, що база даних вже заповнена даними. 
Функції агрегації SQLAlchemy зберігає в
 обєкті func. Його треба спеціально 
 імпортувати from sqlalchemy import func і тоді ми зможемо 
 використати методи func.round та func.avg. Отже перший 
 рядок SQL запиту має виглядати 
 так session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')). Тут ми використали ще label('avg_grade') так ORM виконує найменування поля, із середнім балом, за допомогою оператора AS.

Далі FROM grades g замінюється методом select_from(Grade). Заміна оператора JOIN - тут все просто це функція join(Student), все інше на себе бере ORM. Групування по полю виконуємо функцією group_by(Student.id).

За сортування відповідає функція order_by, яка, за замовчуванням, сортує як ASC, а нам явно треба режим зростання DESC та ще й по полю avg_grade, яке ми самі створили у запиті. Імпортуємо from sqlalchemy import func, desc та остаточний вигляд — order_by(desc('avg_grade')). Ліміт у п'ять значень це функція з такою самою назвою limit(5). Ось і все, наш запит готовий.

Остаточний варіант запиту для ORM SQLAlchemy.
Інші запити ви повинні побудувати аналогічно викладеному вище прикладу. І остання підказка, якщо ви вирішите зробити вкладені запити, тоді використовуйте scalar-selects

Додаткове завдання
Перша частина
Для додаткового завдання зробіть такі запити підвищеної складності:

Середній бал, який певний викладач ставить певному студентові.
Оцінки студентів у певній групі з певного предмета на останньому занятті.
Друга частина
Замість скрипту seed.py подумайте та реалізуйте повноцінну CLI програму для CRUD операцій із базою даних. Використовуйте для цього модуль argparse .

Використовуйте команду --action або скорочений варіант -a для CRUD операцій. Та команду --model (-m) для вказівки над якою моделлю проводитися операція.

Приклад:

--action create -m Teacher --name 'Boris Jonson' створення вчителя
--action list -m Teacher показати всіх вчителів
--action update -m Teacher --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
--action remove -m Teacher --id 3 видалити вчителя з id=3
Реалізуйте ці операції для кожної моделі.

INFO
Приклади виконання команд у терміналі.

Створити вчителя

 py main.py -a create -m Teacher -n 'Boris Jonson'

Створити групу

 py main.py -a create -m Group -n 'AD-101'  
 '''



from db import session  
from models import Student, Teacher, Grade, Group, Discipline
from sqlalchemy import select, func, desc
from pprint import pprint


def select_1():
   result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade') )\
      .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')) .limit(5).all()
   return result



def select_2(discipline_id):
   res = session.query(
      Discipline.name,
      Student.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Student).join(Discipline)\
         .filter(Discipline.id == discipline_id)\
         .group_by(Student.name, Discipline.name)\
         .order_by(desc("avg_grade"))\
         .limit(1).all()
   return res




def select_3(discipline_id):
   res = session.query(
      Group.name,
      Discipline.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Student)\
         .join(Discipline)\
         .join(Group)\
         .filter(Discipline.id == discipline_id)\
         .group_by(Group.name, Discipline.name)\
         .order_by(desc("avg_grade"))\
         .all()
   return res




def select_4():
   res = session.query(
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .all()
   return res




def select_5(teacher_id):
   res = session.query(
      Teacher.name,
      Discipline.name ) \
         .select_from(Grade)\
         .join(Student)\
         .join(Discipline)\
         .join(Group)\
         .join(Teacher)\
         .filter(Teacher.id == teacher_id)\
         .group_by(Teacher.name, Discipline.name)\
         .all()
   return res




def select_6(group_id):
   res = session.query(
      Student.name,
      Group.name ) \
         .select_from(Student)\
         .join(Group)\
         .filter(Group.id == group_id)\
         .all()
   return res




def select_7():
   ...




def select_8():
   ...




def select_9():
   ...




def select_10():
   ...


def select_11(discipline_id, group_id):
   subquery =session.query(Grade.date_off)  (select(func.max(Grade.date_off)).join(Student).join(Group).where(
      (Grade.discipline_id == discipline_id) and (Group.group_id == group_id) 
      ).order_by(desc(Grade.date_off)).limit(1).scalar_subquery() )
   return subquery


def select_12(discipline_id, group_id):
   subquery = ( select(func.max(Grade.date_off)).join(Student).join(Group).where(
      (Grade.discipline_id == discipline_id) and (Group.group_id == group_id) 
      ).order_by(desc(Grade.date_off)).limit(1).scalar_subquery() )

   res = session.query(
      Discipline.name,
      Group.name,
      Student.name,
      Grade.grade,
      Grade.date_off ) \
         .select_from(Grade)\
         .join(Student).join(Discipline).join(Group)\
         .filter(( (Discipline.id == discipline_id) and (Group.id == group_id) and (Grade.date_off == subquery)))\
         .order_by(Grade.date_off)\
         .all()
          

   return res



if __name__ == '__main__':

   # pprint(select_1())
   # pprint(select_2(1))
   # pprint(select_3(3))
   # pprint(select_4())
   # pprint(select_5(1))
   pprint(select_6(3))
   # pprint(select_7(3))
   # pprint(select_8(3))
   # pprint(select_9(3))
   # pprint(select_10(3))
   # pprint(select_11(3))
   # pprint(select_12(3))
