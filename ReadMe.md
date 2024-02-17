Промежуточная контрольная работа по блоку специализация
Урок 1. Приложение заметки (Python)
Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками. 
Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный репозиторий (Github, gitlub, или Bitbucket). 
Разработку вести в этом репозитории, использовать пул реквесты на изменения. Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.

# Критерии оценки
Приложение должно:
>> 
>> - запускаться без ошибок; 
>> 
>> - уметь сохранять данные в файл; 
>> 
>> - уметь читать данные из файла; 
>> 
>> - делать выборку по дате; 
>> 
>> - выводить на экран выбранную запись; 
>> 
>> - выводить на экран весь список записок; 
>> 
>> - добавлять записку; 
>> 
>> - редактировать ее и удалять.

Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). 
Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные),
можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

# Реализация:

1. Для реализации проекта была сформирована програма 'notepad' на языке Python.
   Данная программа реализована с помошью таких бибилиотек как: easygui, sqlite3, datetime, json, csv

   easygui - для создание простого, удобного интерфейса (Интерфейс студент может выбрать сам);
   sqlite3 - для записи в простую, локальную SQL базу (в условии нет указания точного формата файла в который должна записываться программа);
   datetime - для реализации привязки времени и даты;
   json и csv - для экспорта заметок. (Импорт реализовывать не стал, по причине сложности организации проверки вводимых черех json файлов);

2. Для реализации были использованы следующие функции:

  1. execute - создание простой SQL базы с курсором
  2. create_note - создание записки. Важный аспект, что при создании записки в первый раз, поле "Последняя дата редактирования" - будет заполнено текстом "Не редактировалось ранее";
  3. save_note_to_sqlite - запись в SQL базу
  4. display_notes - вывоз заметок. (т.к. нет чёткого условия, в каком виде выводить заметки, был реализован функционал поиска заметок по их id)
  5. edit_note - редактирование заметок
  6. delete_notе - удаление выбранной заметки
  7. export_notes_to_json - сохранение заметок в JSON;
  8. export_notes_to_csv - сохранение заметок в CVS;

3. Реализация "Пушей" в гитхаб.
   
   Для выполнения условий создания нового репозитория и проведения пушей, была отдельно интегрирована функция "display_all_notes" выводящая список всех записок.

5. Завершение реализации
   
   Далее, в приложение добавлена кнопка Exit - выполняющая команду "Break" 


Задачу выполнял: Козменко Сергей 
Поток 1: Разработчик — Программист. Специализация Группа: 5452
Поток 2: Разработчик — Тестировщик. Специализация Группа: Б/Н (выходного дня)
Поток 3: Разработчик — Проджект-менеджер. Специализация Группа: Б/Н (выходного дня)
