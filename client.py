import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import requests
import pandas as pd

SERVER_URL = "http://127.0.0.1:5000"


def add_university():
    name = simpledialog.askstring("Добавить университет", "Введите название университета:")
    if name:
        response = requests.post(f"{SERVER_URL}/add_university", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название университета")

def delete_university():
    name = simpledialog.askstring("Удалить университет", "Введите название университета:")
    if name:
        response = requests.post(f"{SERVER_URL}/delete_university", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название университета")

def edit_university():
    old_name = simpledialog.askstring("Редактировать университет", "Введите старое название университета:")
    new_name = simpledialog.askstring("Редактировать университет", "Введите новое название университета:")
    if old_name and new_name:
        response = requests.post(f"{SERVER_URL}/edit_university", json={"old_name": old_name, "new_name": new_name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите названия университета")

def show_universities():
    response = requests.get(f"{SERVER_URL}/show_universities")
    universities = response.json()
    display_data(universities, ["ID", "Название"])

def export_universities():
    response = requests.get(f"{SERVER_URL}/show_universities")
    universities = response.json()
    export_to_excel(universities, "universities.xlsx", ["ID", "Название"])

# Функции для работы с факультетом
def add_faculty():
    name = simpledialog.askstring("Добавить факультет", "Введите название факультета:")
    dean_fio = simpledialog.askstring("Добавить факультет", "Введите ФИО декана:")
    university_id = simpledialog.askinteger("Добавить факультет", "Введите ID университета:")
    if name and dean_fio and university_id:
        response = requests.post(f"{SERVER_URL}/add_faculty", json={"name": name, "dean_fio": dean_fio, "university_id": university_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_faculty():
    name = simpledialog.askstring("Удалить факультет", "Введите название факультета:")
    if name:
        response = requests.post(f"{SERVER_URL}/delete_faculty", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название факультета")

def edit_faculty():
    old_name = simpledialog.askstring("Редактировать факультет", "Введите старое название факультета:")
    new_name = simpledialog.askstring("Редактировать факультет", "Введите новое название факультета:")
    new_dean_fio = simpledialog.askstring("Редактировать факультет", "Введите новое ФИО декана:")
    if old_name and new_name and new_dean_fio:
        response = requests.post(f"{SERVER_URL}/edit_faculty", json={"old_name": old_name, "new_name": new_name, "new_dean_fio": new_dean_fio})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_faculties():
    response = requests.get(f"{SERVER_URL}/show_faculties")
    faculties = response.json()
    display_data(faculties, ["ID", "Название", "Декан", "University ID"])

def export_faculties():
    response = requests.get(f"{SERVER_URL}/show_faculties")
    faculties = response.json()
    export_to_excel(faculties, "faculties.xlsx", ["ID", "Название", "Декан", "University ID"])

# Функции для работы с кафедрой
def add_department():
    name = simpledialog.askstring("Добавить кафедру", "Введите название кафедры:")
    head_fio = simpledialog.askstring("Добавить кафедру", "Введите ФИО заведующего кафедрой:")
    faculty_id = simpledialog.askinteger("Добавить кафедру", "Введите ID факультета:")
    if name and head_fio and faculty_id:
        response = requests.post(f"{SERVER_URL}/add_department", json={"name": name, "head_fio": head_fio, "faculty_id": faculty_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_department():
    name = simpledialog.askstring("Удалить кафедру", "Введите название кафедры:")
    if name:
        response = requests.post(f"{SERVER_URL}/delete_department", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название кафедры")

def edit_department():
    old_name = simpledialog.askstring("Редактировать кафедру", "Введите старое название кафедры:")
    new_name = simpledialog.askstring("Редактировать кафедру", "Введите новое название кафедры:")
    new_head_fio = simpledialog.askstring("Редактировать кафедру", "Введите новое ФИО заведующего кафедрой:")
    if old_name and new_name and new_head_fio:
        response = requests.post(f"{SERVER_URL}/edit_department", json={"old_name": old_name, "new_name": new_name, "new_head_fio": new_head_fio})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_departments():
    response = requests.get(f"{SERVER_URL}/show_departments")
    departments = response.json()
    display_data(departments, ["ID", "Название", "Заведующий", "Faculty ID"])

def export_departments():
    response = requests.get(f"{SERVER_URL}/show_departments")
    departments = response.json()
    export_to_excel(departments, "departments.xlsx", ["ID", "Название", "Заведующий", "Faculty ID"])

# Функции для работы с преподавателем
def add_teacher():
    fio = simpledialog.askstring("Добавить преподавателя", "Введите ФИО преподавателя:")
    department_id = simpledialog.askinteger("Добавить преподавателя", "Введите ID кафедры:")
    if fio and department_id:
        response = requests.post(f"{SERVER_URL}/add_teacher", json={"fio": fio, "department_id": department_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_teacher():
    fio = simpledialog.askstring("Удалить преподавателя", "Введите ФИО преподавателя:")
    if fio:
        response = requests.post(f"{SERVER_URL}/delete_teacher", json={"fio": fio})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите ФИО преподавателя")

def edit_teacher():
    old_fio = simpledialog.askstring("Редактировать преподавателя", "Введите старое ФИО преподавателя:")
    new_fio = simpledialog.askstring("Редактировать преподавателя", "Введите новое ФИО преподавателя:")
    if old_fio and new_fio:
        response = requests.post(f"{SERVER_URL}/edit_teacher", json={"old_fio": old_fio, "new_fio": new_fio})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите ФИО преподавателя")

def show_teachers():
    response = requests.get(f"{SERVER_URL}/show_teachers")
    teachers = response.json()
    display_data(teachers, ["ID", "ФИО", "Department ID"])

def export_teachers():
    response = requests.get(f"{SERVER_URL}/show_teachers")
    teachers = response.json()
    export_to_excel(teachers, "teachers.xlsx", ["ID", "ФИО", "Department ID"])

# Функции для работы с предметом
def add_subject():
    name = simpledialog.askstring("Добавить предмет", "Введите название предмета:")
    teacher_id = simpledialog.askinteger("Добавить предмет", "Введите ID преподавателя:")
    if name and teacher_id:
        response = requests.post(f"{SERVER_URL}/add_subject", json={"name": name, "teacher_id": teacher_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_subject():
    name = simpledialog.askstring("Удалить предмет", "Введите название предмета:")
    if name:
        response = requests.post(f"{SERVER_URL}/delete_subject", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название предмета")

def edit_subject():
    old_name = simpledialog.askstring("Редактировать предмет", "Введите старое название предмета:")
    new_name = simpledialog.askstring("Редактировать предмет", "Введите новое название предмета:")
    if old_name and new_name:
        response = requests.post(f"{SERVER_URL}/edit_subject", json={"old_name": old_name, "new_name": new_name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите названия предмета")

def show_subjects():
    response = requests.get(f"{SERVER_URL}/show_subjects")
    subjects = response.json()
    display_data(subjects, ["ID", "Название", "Teacher ID"])

def export_subjects():
    response = requests.get(f"{SERVER_URL}/show_subjects")
    subjects = response.json()
    export_to_excel(subjects, "subjects.xlsx", ["ID", "Название", "Teacher ID"])

# Функции для работы со специальностью
def add_specialty():
    name = simpledialog.askstring("Добавить специальность", "Введите название специальности:")
    code = simpledialog.askstring("Добавить специальность", "Введите код специальности:")
    qualification = simpledialog.askstring("Добавить специальность", "Введите квалификацию:")
    faculty_id = simpledialog.askinteger("Добавить специальность", "Введите ID факультета:")
    if name and code and qualification and faculty_id:
        response = requests.post(f"{SERVER_URL}/add_specialty", json={"name": name, "code": code, "qualification": qualification, "faculty_id": faculty_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_specialty():
    name = simpledialog.askstring("Удалить специальность", "Введите название специальности:")
    if name:
        response = requests.post(f"{SERVER_URL}/delete_specialty", json={"name": name})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите название специальности")

def edit_specialty():
    old_name = simpledialog.askstring("Редактировать специальность", "Введите старое название специальности:")
    new_name = simpledialog.askstring("Редактировать специальность", "Введите новое название специальности:")
    new_code = simpledialog.askstring("Редактировать специальность", "Введите новый код специальности:")
    new_qualification = simpledialog.askstring("Редактировать специальность", "Введите новую квалификацию:")
    if old_name and new_name and new_code and new_qualification:
        response = requests.post(f"{SERVER_URL}/edit_specialty", json={"old_name": old_name, "new_name": new_name, "new_code": new_code, "new_qualification": new_qualification})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_specialties():
    response = requests.get(f"{SERVER_URL}/show_specialties")
    specialties = response.json()
    display_data(specialties, ["ID", "Название", "Код", "Квалификация", "Faculty ID"])

def export_specialties():
    response = requests.get(f"{SERVER_URL}/show_specialties")
    specialties = response.json()
    export_to_excel(specialties, "specialties.xlsx", ["ID", "Название", "Код", "Квалификация", "Faculty ID"])

# Функции для работы с группой
def add_group():
    code = simpledialog.askstring("Добавить группу", "Введите код группы:")
    year_of_admission = simpledialog.askinteger("Добавить группу", "Введите год поступления:")
    number = simpledialog.askinteger("Добавить группу", "Введите номер группы:")
    specialty_id = simpledialog.askinteger("Добавить группу", "Введите ID специальности:")
    if code and year_of_admission and number and specialty_id:
        response = requests.post(f"{SERVER_URL}/add_group", json={"code": code, "year_of_admission": year_of_admission, "number": number, "specialty_id": specialty_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_group():
    code = simpledialog.askstring("Удалить группу", "Введите код группы:")
    if code:
        response = requests.post(f"{SERVER_URL}/delete_group", json={"code": code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите код группы")

def edit_group():
    old_code = simpledialog.askstring("Редактировать группу", "Введите старый код группы:")
    new_code = simpledialog.askstring("Редактировать группу", "Введите новый код группы:")
    new_year_of_admission = simpledialog.askinteger("Редактировать группу", "Введите новый год поступления:")
    new_number = simpledialog.askinteger("Редактировать группу", "Введите новый номер группы:")
    if old_code and new_code and new_year_of_admission and new_number:
        response = requests.post(f"{SERVER_URL}/edit_group", json={"old_code": old_code, "new_code": new_code, "new_year_of_admission": new_year_of_admission, "new_number": new_number})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_groups():
    response = requests.get(f"{SERVER_URL}/show_groups")
    groups = response.json()
    display_data(groups, ["ID", "Код", "Год поступления", "Номер", "Specialty ID"])

def export_groups():
    response = requests.get(f"{SERVER_URL}/show_groups")
    groups = response.json()
    export_to_excel(groups, "groups.xlsx", ["ID", "Код", "Год поступления", "Номер", "Specialty ID"])

# Функции для работы с самостоятельной работой
def add_independent_work():
    topic = simpledialog.askstring("Добавить самостоятельную работу", "Введите тему самостоятельной работы:")
    time_and_date = simpledialog.askstring("Добавить самостоятельную работу", "Введите время и дату проведения:")
    materials = simpledialog.askstring("Добавить самостоятельную работу", "Введите необходимые материалы:")
    code = simpledialog.askstring("Добавить самостоятельную работу", "Введите код самостоятельной работы:")
    conditions = simpledialog.askstring("Добавить самостоятельную работу", "Введите условия допуска:")
    group_id = simpledialog.askinteger("Добавить самостоятельную работу", "Введите ID группы:")
    if topic and time_and_date and materials and code and conditions and group_id:
        response = requests.post(f"{SERVER_URL}/add_independent_work", json={"topic": topic, "time_and_date": time_and_date, "materials": materials, "code": code, "conditions": conditions, "group_id": group_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_independent_work():
    code = simpledialog.askstring("Удалить самостоятельную работу", "Введите код самостоятельной работы:")
    if code:
        response = requests.post(f"{SERVER_URL}/delete_independent_work", json={"code": code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите код самостоятельной работы")

def edit_independent_work():
    old_code = simpledialog.askstring("Редактировать самостоятельную работу", "Введите старый код самостоятельной работы:")
    new_topic = simpledialog.askstring("Редактировать самостоятельную работу", "Введите новую тему самостоятельной работы:")
    new_time_and_date = simpledialog.askstring("Редактировать самостоятельную работу", "Введите новое время и дату проведения:")
    new_materials = simpledialog.askstring("Редактировать самостоятельную работу", "Введите новые необходимые материалы:")
    new_code = simpledialog.askstring("Редактировать самостоятельную работу", "Введите новый код самостоятельной работы:")
    new_conditions = simpledialog.askstring("Редактировать самостоятельную работу", "Введите новые условия допуска:")
    if old_code and new_topic and new_time_and_date and new_materials and new_code and new_conditions:
        response = requests.post(f"{SERVER_URL}/edit_independent_work", json={"old_code": old_code, "new_topic": new_topic, "new_time_and_date": new_time_and_date, "new_materials": new_materials, "new_code": new_code, "new_conditions": new_conditions})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_independent_works():
    response = requests.get(f"{SERVER_URL}/show_independent_works")
    independent_works = response.json()
    display_data(independent_works, ["ID", "Тема", "Время и дата", "Материалы", "Код", "Условия", "Group ID"])

def export_independent_works():
    response = requests.get(f"{SERVER_URL}/show_independent_works")
    independent_works = response.json()
    export_to_excel(independent_works, "independent_works.xlsx", ["ID", "Тема", "Время и дата", "Материалы", "Код", "Условия", "Group ID"])

# Функции для работы с лекцией
def add_lecture():
    topic = simpledialog.askstring("Добавить лекцию", "Введите тему лекции:")
    time_and_date = simpledialog.askstring("Добавить лекцию", "Введите время и дату проведения:")
    materials = simpledialog.askstring("Добавить лекцию", "Введите необходимые материалы:")
    requirements = simpledialog.askstring("Добавить лекцию", "Введите требования для понимания:")
    literature = simpledialog.askstring("Добавить лекцию", "Введите список литературы:")
    code = simpledialog.askstring("Добавить лекцию", "Введите код лекции:")
    subject_id = simpledialog.askinteger("Добавить лекцию", "Введите ID предмета:")
    if topic and time_and_date and materials and requirements and literature and code and subject_id:
        response = requests.post(f"{SERVER_URL}/add_lecture", json={"topic": topic, "time_and_date": time_and_date, "materials": materials, "requirements": requirements, "literature": literature, "code": code, "subject_id": subject_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_lecture():
    code = simpledialog.askstring("Удалить лекцию", "Введите код лекции:")
    if code:
        response = requests.post(f"{SERVER_URL}/delete_lecture", json={"code": code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите код лекции")

def edit_lecture():
    old_code = simpledialog.askstring("Редактировать лекцию", "Введите старый код лекции:")
    new_topic = simpledialog.askstring("Редактировать лекцию", "Введите новую тему лекции:")
    new_time_and_date = simpledialog.askstring("Редактировать лекцию", "Введите новое время и дату проведения:")
    new_materials = simpledialog.askstring("Редактировать лекцию", "Введите новые необходимые материалы:")
    new_requirements = simpledialog.askstring("Редактировать лекцию", "Введите новые требования для понимания:")
    new_literature = simpledialog.askstring("Редактировать лекцию", "Введите новый список литературы:")
    new_code = simpledialog.askstring("Редактировать лекцию", "Введите новый код лекции:")
    if old_code and new_topic and new_time_and_date and new_materials and new_requirements and new_literature and new_code:
        response = requests.post(f"{SERVER_URL}/edit_lecture", json={"old_code": old_code, "new_topic": new_topic, "new_time_and_date": new_time_and_date, "new_materials": new_materials, "new_requirements": new_requirements, "new_literature": new_literature, "new_code": new_code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_lectures():
    response = requests.get(f"{SERVER_URL}/show_lectures")
    lectures = response.json()
    display_data(lectures, ["ID", "Тема", "Время и дата", "Материалы", "Требования", "Литература", "Код", "Subject ID"])

def export_lectures():
    response = requests.get(f"{SERVER_URL}/show_lectures")
    lectures = response.json()
    export_to_excel(lectures, "lectures.xlsx", ["ID", "Тема", "Время и дата", "Материалы", "Требования", "Литература", "Код", "Subject ID"])

# Функции для работы с практическим занятием
def add_practical():
    topic = simpledialog.askstring("Добавить практическое занятие", "Введите тему практического занятия:")
    time_and_date = simpledialog.askstring("Добавить практическое занятие", "Введите время и дату проведения:")
    materials = simpledialog.askstring("Добавить практическое занятие", "Введите необходимые материалы:")
    code = simpledialog.askstring("Добавить практическое занятие", "Введите код практического занятия:")
    conditions = simpledialog.askstring("Добавить практическое занятие", "Введите условия допуска:")
    subject_id = simpledialog.askinteger("Добавить практическое занятие", "Введите ID предмета:")
    if topic and time_and_date and materials and code and conditions and subject_id:
        response = requests.post(f"{SERVER_URL}/add_practical", json={"topic": topic, "time_and_date": time_and_date, "materials": materials, "code": code, "conditions": conditions, "subject_id": subject_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_practical():
    code = simpledialog.askstring("Удалить практическое занятие", "Введите код практического занятия:")
    if code:
        response = requests.post(f"{SERVER_URL}/delete_practical", json={"code": code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите код практического занятия")

def edit_practical():
    old_code = simpledialog.askstring("Редактировать практическое занятие", "Введите старый код практического занятия:")
    new_topic = simpledialog.askstring("Редактировать практическое занятие", "Введите новую тему практического занятия:")
    new_time_and_date = simpledialog.askstring("Редактировать практическое занятие", "Введите новое время и дату проведения:")
    new_materials = simpledialog.askstring("Редактировать практическое занятие", "Введите новые необходимые материалы:")
    new_code = simpledialog.askstring("Редактировать практическое занятие", "Введите новый код практического занятия:")
    new_conditions = simpledialog.askstring("Редактировать практическое занятие", "Введите новые условия допуска:")
    if old_code and new_topic and new_time_and_date and new_materials and new_code and new_conditions:
        response = requests.post(f"{SERVER_URL}/edit_practical", json={"old_code": old_code, "new_topic": new_topic, "new_time_and_date": new_time_and_date, "new_materials": new_materials, "new_code": new_code, "new_conditions": new_conditions})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_practicals():
    response = requests.get(f"{SERVER_URL}/show_practicals")
    practicals = response.json()
    display_data(practicals, ["ID", "Тема", "Время и дата", "Материалы", "Код", "Условия", "Subject ID"])

def export_practicals():
    response = requests.get(f"{SERVER_URL}/show_practicals")
    practicals = response.json()
    export_to_excel(practicals, "practicals.xlsx", ["ID", "Тема", "Время и дата", "Материалы", "Код", "Условия", "Subject ID"])

# Функции для работы с лабораторной работой
def add_laboratory():
    topic = simpledialog.askstring("Добавить лабораторную работу", "Введите тему лабораторной работы:")
    time_and_date = simpledialog.askstring("Добавить лабораторную работу", "Введите время и дату проведения:")
    code = simpledialog.askstring("Добавить лабораторную работу", "Введите код лабораторной работы:")
    conditions = simpledialog.askstring("Добавить лабораторную работу", "Введите условия допуска:")
    equipment = simpledialog.askstring("Добавить лабораторную работу", "Введите необходимое оборудование:")
    subject_id = simpledialog.askinteger("Добавить лабораторную работу", "Введите ID предмета:")
    if topic and time_and_date and code and conditions and equipment and subject_id:
        response = requests.post(f"{SERVER_URL}/add_laboratory", json={"topic": topic, "time_and_date": time_and_date, "code": code, "conditions": conditions, "equipment": equipment, "subject_id": subject_id})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def delete_laboratory():
    code = simpledialog.askstring("Удалить лабораторную работу", "Введите код лабораторной работы:")
    if code:
        response = requests.post(f"{SERVER_URL}/delete_laboratory", json={"code": code})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите код лабораторной работы")

def edit_laboratory():
    old_code = simpledialog.askstring("Редактировать лабораторную работу", "Введите старый код лабораторной работы:")
    new_topic = simpledialog.askstring("Редактировать лабораторную работу", "Введите новую тему лабораторной работы:")
    new_time_and_date = simpledialog.askstring("Редактировать лабораторную работу", "Введите новое время и дату проведения:")
    new_code = simpledialog.askstring("Редактировать лабораторную работу", "Введите новый код лабораторной работы:")
    new_conditions = simpledialog.askstring("Редактировать лабораторную работу", "Введите новые условия допуска:")
    new_equipment = simpledialog.askstring("Редактировать лабораторную работу", "Введите новое необходимое оборудование:")
    if old_code and new_topic and new_time_and_date and new_code and new_conditions and new_equipment:
        response = requests.post(f"{SERVER_URL}/edit_laboratory", json={"old_code": old_code, "new_topic": new_topic, "new_time_and_date": new_time_and_date, "new_code": new_code, "new_conditions": new_conditions, "new_equipment": new_equipment})
        result = response.json()
        messagebox.showinfo("Успех", result["message"])
    else:
        messagebox.showerror("Ошибка", "Введите все данные")

def show_laboratories():
    response = requests.get(f"{SERVER_URL}/show_laboratories")
    laboratories = response.json()
    display_data(laboratories, ["ID", "Тема", "Время и дата", "Код", "Условия", "Оборудование", "Subject ID"])

def export_laboratories():
    response = requests.get(f"{SERVER_URL}/show_laboratories")
    laboratories = response.json()
    export_to_excel(laboratories, "laboratories.xlsx", ["ID", "Тема", "Время и дата", "Код", "Условия", "Оборудование", "Subject ID"])

# Функция для отображения данных в таблице
def display_data(data, columns):
    for widget in data_frame.winfo_children():
        widget.destroy()

    df = pd.DataFrame(data, columns=columns)
    tree = ttk.Treeview(data_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree.pack()

# Функция для экспорта данных в Excel
def export_to_excel(data, filename, columns):
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(filename, index=False)
    messagebox.showinfo("Успех", f"Данные успешно экспортированы в {filename}")

# Основное окно приложения
root = tk.Tk()
root.title("Университет")

# Меню для выбора таблицы
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

tk.Label(menu_frame, text="Выберите таблицу:").pack()

def show_university_options():
    university_frame.pack()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_faculty_options():
    university_frame.pack_forget()
    faculty_frame.pack()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_department_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_teacher_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_subject_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_specialty_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_group_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_independent_work_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_lecture_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack()
    practical_frame.pack_forget()
    laboratory_frame.pack_forget()

def show_practical_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack()
    laboratory_frame.pack_forget()

def show_laboratory_options():
    university_frame.pack_forget()
    faculty_frame.pack_forget()
    department_frame.pack_forget()
    teacher_frame.pack_forget()
    subject_frame.pack_forget()
    specialty_frame.pack_forget()
    group_frame.pack_forget()
    independent_work_frame.pack_forget()
    lecture_frame.pack_forget()
    practical_frame.pack_forget()
    laboratory_frame.pack()
def export_all_to_pdf():
    response = requests.get(f"{SERVER_URL}/export_all_to_pdf")
    if response.status_code == 200:
        messagebox.showinfo("Успех", "Данные успешно экспортированы в report.pdf")
    else:
        messagebox.showerror("Ошибка", "Ошибка при экспорте данных")
tk.Button(menu_frame, text="Университет", command=show_university_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Факультет", command=show_faculty_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Кафедра", command=show_department_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Преподаватель", command=show_teacher_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Предмет", command=show_subject_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Специальность", command=show_specialty_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Группа", command=show_group_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Самостоятельная работа", command=show_independent_work_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Лекция", command=show_lecture_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Практическое занятие", command=show_practical_options).pack(side=tk.LEFT, padx=5)
tk.Button(menu_frame, text="Лабораторная работа", command=show_laboratory_options).pack(side=tk.LEFT, padx=5)

# Фрейм для университета
university_frame = tk.Frame(root)
university_frame.pack_forget()

tk.Button(university_frame, text="Добавить университет", command=add_university).pack(pady=5)
tk.Button(university_frame, text="Удалить университет", command=delete_university).pack(pady=5)
tk.Button(university_frame, text="Редактировать университет", command=edit_university).pack(pady=5)
tk.Button(university_frame, text="Показать университеты", command=show_universities).pack(pady=5)
tk.Button(university_frame, text="Экспорт в Excel", command=export_universities).pack(pady=5)

# Фрейм для факультета
faculty_frame = tk.Frame(root)
faculty_frame.pack_forget()

tk.Button(faculty_frame, text="Добавить факультет", command=add_faculty).pack(pady=5)
tk.Button(faculty_frame, text="Удалить факультет", command=delete_faculty).pack(pady=5)
tk.Button(faculty_frame, text="Редактировать факультет", command=edit_faculty).pack(pady=5)
tk.Button(faculty_frame, text="Показать факультеты", command=show_faculties).pack(pady=5)
tk.Button(faculty_frame, text="Экспорт в Excel", command=export_faculties).pack(pady=5)

# Фрейм для кафедры
department_frame = tk.Frame(root)
department_frame.pack_forget()

tk.Button(department_frame, text="Добавить кафедру", command=add_department).pack(pady=5)
tk.Button(department_frame, text="Удалить кафедру", command=delete_department).pack(pady=5)
tk.Button(department_frame, text="Редактировать кафедру", command=edit_department).pack(pady=5)
tk.Button(department_frame, text="Показать кафедры", command=show_departments).pack(pady=5)
tk.Button(department_frame, text="Экспорт в Excel", command=export_departments).pack(pady=5)

# Фрейм для преподавателя
teacher_frame = tk.Frame(root)
teacher_frame.pack_forget()

tk.Button(teacher_frame, text="Добавить преподавателя", command=add_teacher).pack(pady=5)
tk.Button(teacher_frame, text="Удалить преподавателя", command=delete_teacher).pack(pady=5)
tk.Button(teacher_frame, text="Редактировать преподавателя", command=edit_teacher).pack(pady=5)
tk.Button(teacher_frame, text="Показать преподавателей", command=show_teachers).pack(pady=5)
tk.Button(teacher_frame, text="Экспорт в Excel", command=export_teachers).pack(pady=5)

# Фрейм для предмета
subject_frame = tk.Frame(root)
subject_frame.pack_forget()

tk.Button(subject_frame, text="Добавить предмет", command=add_subject).pack(pady=5)
tk.Button(subject_frame, text="Удалить предмет", command=delete_subject).pack(pady=5)
tk.Button(subject_frame, text="Редактировать предмет", command=edit_subject).pack(pady=5)
tk.Button(subject_frame, text="Показать предметы", command=show_subjects).pack(pady=5)
tk.Button(subject_frame, text="Экспорт в Excel", command=export_subjects).pack(pady=5)

# Фрейм для специальности
specialty_frame = tk.Frame(root)
specialty_frame.pack_forget()

tk.Button(specialty_frame, text="Добавить специальность", command=add_specialty).pack(pady=5)
tk.Button(specialty_frame, text="Удалить специальность", command=delete_specialty).pack(pady=5)
tk.Button(specialty_frame, text="Редактировать специальность", command=edit_specialty).pack(pady=5)
tk.Button(specialty_frame, text="Показать специальности", command=show_specialties).pack(pady=5)
tk.Button(specialty_frame, text="Экспорт в Excel", command=export_specialties).pack(pady=5)

# Фрейм для группы
group_frame = tk.Frame(root)
group_frame.pack_forget()

tk.Button(group_frame, text="Добавить группу", command=add_group).pack(pady=5)
tk.Button(group_frame, text="Удалить группу", command=delete_group).pack(pady=5)
tk.Button(group_frame, text="Редактировать группу", command=edit_group).pack(pady=5)
tk.Button(group_frame, text="Показать группы", command=show_groups).pack(pady=5)
tk.Button(group_frame, text="Экспорт в Excel", command=export_groups).pack(pady=5)

# Фрейм для самостоятельной работы
independent_work_frame = tk.Frame(root)
independent_work_frame.pack_forget()

tk.Button(independent_work_frame, text="Добавить самостоятельную работу", command=add_independent_work).pack(pady=5)
tk.Button(independent_work_frame, text="Удалить самостоятельную работу", command=delete_independent_work).pack(pady=5)
tk.Button(independent_work_frame, text="Редактировать самостоятельную работу", command=edit_independent_work).pack(pady=5)
tk.Button(independent_work_frame, text="Показать самостоятельные работы", command=show_independent_works).pack(pady=5)
tk.Button(independent_work_frame, text="Экспорт в Excel", command=export_independent_works).pack(pady=5)

# Фрейм для лекции
lecture_frame = tk.Frame(root)
lecture_frame.pack_forget()

tk.Button(lecture_frame, text="Добавить лекцию", command=add_lecture).pack(pady=5)
tk.Button(lecture_frame, text="Удалить лекцию", command=delete_lecture).pack(pady=5)
tk.Button(lecture_frame, text="Редактировать лекцию", command=edit_lecture).pack(pady=5)
tk.Button(lecture_frame, text="Показать лекции", command=show_lectures).pack(pady=5)
tk.Button(lecture_frame, text="Экспорт в Excel", command=export_lectures).pack(pady=5)

# Фрейм для практического занятия
practical_frame = tk.Frame(root)
practical_frame.pack_forget()

tk.Button(practical_frame, text="Добавить практическое занятие", command=add_practical).pack(pady=5)
tk.Button(practical_frame, text="Удалить практическое занятие", command=delete_practical).pack(pady=5)
tk.Button(practical_frame, text="Редактировать практическое занятие", command=edit_practical).pack(pady=5)
tk.Button(practical_frame, text="Показать практические занятия", command=show_practicals).pack(pady=5)
tk.Button(practical_frame, text="Экспорт в Excel", command=export_practicals).pack(pady=5)

# Фрейм для лабораторной работы
laboratory_frame = tk.Frame(root)
laboratory_frame.pack_forget()

tk.Button(laboratory_frame, text="Добавить лабораторную работу", command=add_laboratory).pack(pady=5)
tk.Button(laboratory_frame, text="Удалить лабораторную работу", command=delete_laboratory).pack(pady=5)
tk.Button(laboratory_frame, text="Редактировать лабораторную работу", command=edit_laboratory).pack(pady=5)
tk.Button(laboratory_frame, text="Показать лабораторные работы", command=show_laboratories).pack(pady=5)
tk.Button(laboratory_frame, text="Экспорт в Excel", command=export_laboratories).pack(pady=5)
tk.Button(menu_frame, text="Сформировать отчёты", command=export_all_to_pdf).pack(side=tk.LEFT, padx=5)


# Фрейм для отображения данных
data_frame = tk.Frame(root)
data_frame.pack(pady=10)

root.mainloop()