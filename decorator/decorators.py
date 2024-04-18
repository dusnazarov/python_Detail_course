# ////////////////////////////////
# class User:

#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

# user = User('simple_user', 'user')
# admin = User('root', 'admin')

# current_user = admin

# # print(current_user.name)
# # print(current_user.role)

# def do_admin_work():
#     if current_user.role != "admin":
#         raise Exception('Access do not allow')
#     return 'Do anything for admin'

# print(do_admin_work())

# # ////////////////////////////////
# class User:

#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

# user = User('simple_user', 'user')
# admin = User('root', 'admin')

# current_user = admin


# def do_admin_work2():
#     return 'Do anything for admin'

# def check_access(funcs):
#     if current_user.role != "admin":
#         raise Exception('Access do not allow')
#     return funcs()

# print(check_access(do_admin_work2))


# # # ////////////////////////////////
# class User:

#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

# user = User('simple_user', 'user')
# admin = User('root', 'admin')

# current_user = admin


# def do_admin_work2():
#     return 'Do anything for admin'

# def check_access2(funcs):
#     def wrapper():
#         if current_user.role != "admin":
#             raise Exception('Access do not allow')
#         return funcs()
#     return wrapper

# print(do_admin_work2.__name__)

# do_admin_work2 = check_access2(do_admin_work2)
# print(do_admin_work2.__name__)


