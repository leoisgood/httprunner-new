# 定义管理员类，管理员有属性(name,password)，可以创建学校、创建课程、创建老师

# 定义老师类，老师有属性(name,password)，可以添加课程、给学生打分,但发现学生没有购买课程时，不能打分，并给出提示

# 定义学生类，学生有属性(name,password)，可以获取当前学校、选择学校、选择课程，但学校没有该课程时，需要提示，并且不能选择该课程

# 定义学校类，学校有属性(name,addr)，可以添加课程

# 定义课程类，课程有属性(name)，可以添加学生

# 然后对上面的类进行测试并且自己编写日志写入到log文件中

# 定义管理员类，管理员有属性(name,password)，可以创建学校、创建课程、创建老师

'''
编写思路：
（1）面向客户，输入角色做判断
（2）管理员，判断是否有学校，课程，老师；没有，则创建；有则显示
（3）选择老师，添加课程，给学生打分，...
（4）学生类，获取学校，如果不存在给出提示

'''
class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password   # define private attribute

    def create_schoool(self, name, addr):
        school_dict = {}
        school_dict.setdefault(name, addr)
        print()

    def create_school_course(self, name):
        school_course_list = []
        school_course_list.append(name)

    def create_school_teacher(self, name):
        course_list = []
        course_list.append(name)


# 定义老师类，老师有属性(name,password)，可以添加课程、给学生打分,但发现学生没有购买课程时，不能打分，并给出提示
class Teacher:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_course(self, course_name):
        course_list = []
        course_list.append(course_name)

    def add_score(self, studennt_name):
        print('{} is scored as 100'.format(studennt_name))


# 定义学生类，学生有属性(name,password)，可以获取当前学校、选择学校、选择课程，但学校没有该课程时，需要提示，并且不能选择该课程
class Student:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def student_info(self):
        pass

    def get_school_name(self, student_name):
        pass

    def choose_school(self, student_name):
        print('{} is scored as 100'.format(student_name))

    def choose_course(self, course_name):
        print('choose_course')


# 定义学校类，学校有属性(name,addr)，可以添加课程
class School:
    def __init__(self, name, addr):
            self.name = name
            self.addr = addr

    def add_school_course(self, course):
            school_course_list = []
            school_course_list.append(course)


# 定义课程类，课程有属性(name)，可以添加学生
class Course:
    def __init__(self, name):
        self.name = name

    def add_student(self, student_name):
        course_student_list = []
        course_student_list.append(student_name)


if __name__ == '__main__':
    while True:
        role = input('Please choose your role using number,1:adminstrator,2:teacher,3:student')
        if role == '1':
            pass
        elif role == '2':
            pass
        elif role == '3':
            pass
        else:
            print('The role number is wrong')