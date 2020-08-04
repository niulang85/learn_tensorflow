# def var():
#     pass
#
# def f2():
#     var = 'Just a String'
#     f1 = globals()['var']
#     print (var)
#     return type(f1)
#
# print ("f2 return: ", f2())

def view():
    var1 = 'Just a String'

    def aaa():
        return 1

    int_var = 12

    print(locals()['var1'])


view()

#
# var = 1
#
# def fun():
#     var = 200
#     print("loc var:", var)
#
# fun()
# print("global var:", var)

#
#
# a = 1
#
#
# def external():
#     global a
#     a = 200
#
#     b = 100
#
#     def internal():
#         nonlocal b
#         print("internal pppp: ", b)
#         b = 200
#         return b
#
#     internal()
#     print("external b:", b)
#
#
# print(external())
#
# print("global a:", a)

# counter
# def counter(start):
#     count = start
#
#     def internal():
#         nonlocal count
#         count += 1
#         return count
#
#     return internal
#
#
# count = counter(0)
# for n in range(10):
#     print(count())
#     # 1,2,3,4,5,6,7,8,9,10
#
# count = counter(0)
# print(count())
# # 1

# counter
# def counter(start):
#     count = [start]
#
#     def internal():
#         print(count[0])
#         # count[0] += 1
#         count[0] = 1
#
#         return count[0]
#
#     return internal
#
#
# count = counter(0)
# for n in range(10):
#     print(count())
#     # 1,2,3,4,5,6,7,8,9,10
#
# count = counter(0)
# print(count())
# # 1
