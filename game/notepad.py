import easygui
import sqlite3
import json
import csv
import datetime

# Подключение к базе данных 
conn = sqlite3.connect('notes_db.sqlite')

# Создание таблицы для хранения заметок
conn.execute('''CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             create_date TEXT NOT NULL,
             last_edit_date TEXT,
             title TEXT NOT NULL,
             body TEXT NOT NULL);''')

# Функция для создания заметки
def create_note():
    title = easygui.enterbox("Заголовок заметки:")
    body = easygui.enterbox("Текст заметки:")
    create_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_edit_date = "Не редактировалось ранее"
    note = {
        'title': title,
        'body': body,
        'create_date': create_date,
        'last_edit_date': last_edit_date
    }
    return note

# Функция для сохранения заметки в базу данных 
def save_note_to_sqlite(note):
    conn.execute("INSERT INTO notes (create_date, last_edit_date, title, body) VALUES (?, ?, ?, ?)",
                 (note['create_date'], note['last_edit_date'], note['title'], note['body']))
    conn.commit()

# Функция для отображения списка заметок
def display_notes(sort_by):
    cursor = conn.execute(f"SELECT * FROM notes ORDER BY {sort_by}")
    for row in cursor.fetchall():
        easygui.msgbox(f"ID: {row[0]}\nTitle: {row[3]}\nBody: {row[4]}\nCreate Date: {row[1]}\nLast Edit Date: {row[2]}")

# Функция для редактирования заметки
def edit_note():
    note_id = easygui.enterbox("Введите ID заметки для редактирования:")
    new_title = easygui.enterbox("Введите новый заголовок:")
    new_body = easygui.enterbox("Введите новый текст:")
    last_edit_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute("UPDATE notes SET title=?, body=?, last_edit_date=? WHERE id=?",
                 (new_title, new_body, last_edit_date, note_id))
    conn.commit()

# Функция для удаления заметки
def delete_note():
    note_id = easygui.enterbox("Введите ID заметки для удаления:")
    conn.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()

# Функция для выгрузки заметок в JSON
def export_notes_to_json(file_name):
    cursor = conn.execute("SELECT * FROM notes")
    notes = []
    for row in cursor.fetchall():
        note = {'id': row[0], 'create_date' : row[1], 'last_edit_date' : row[2], 'title': row[3], 'body': row[4]}
        notes.append(note)
    with open(file_name, 'w') as file:
        json.dump(notes, file)

# Функция для выгрузки заметок в CSV
def export_notes_to_csv(file_name):
    cursor = conn.execute("SELECT * FROM notes")
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['id', 'create_date', 'last_edit_date', 'title', 'body'])
        for row in cursor.fetchall():
            writer.writerow(row)

#Главный цикл программы
while True:
    choices = ["Create Note", "Display Notes (ID)", "Display Notes (Date)", "Edit Note", "Delete Note", "Export to JSON", "Export to CSV", "Exit"]
    choice = easygui.buttonbox("Select an action:", choices=choices)

    if choice == "Create Note":
        note = create_note()
        save_note_to_sqlite(note)
    elif choice == "Display Notes (ID)":
        display_notes("id")
    elif choice == "Display Notes (Date)":
        display_notes("create_date")
    elif choice == "Edit Note":
        edit_note()
    elif choice == "Delete Note":
        delete_note()
    elif choice == "Export to JSON":
        file_name = easygui.filesavebox("Export to JSON. Choose a file:")
        export_notes_to_json(file_name)
    elif choice == "Export to CSV":
        file_name = easygui.filesavebox("Export to CSV. Choose a file:")
        export_notes_to_csv(file_name)
    elif choice == "Exit":
        conn
        break
        