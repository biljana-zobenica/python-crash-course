from admin import User, Admin, Privileges

my_admin = Admin('Jack', 'Spark', 'jack123', 'jack123@email.com', 'Seattle')
my_admin.greet_user()
my_admin.privileges.list_privileges()

print("Adding privileges...")

my_admin_priveleges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
my_admin.privileges.privileges = my_admin_priveleges
my_admin.privileges.list_privileges()