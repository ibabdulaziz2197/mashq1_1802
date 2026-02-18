# # 13
# mahsulot = {"nomi": "Telefon",
#             "brend": "Samsung",
#             "narx": 3500000,
#             "rang": "qora"
# }
# print(mahsulot)
# mahsulot.pop()
# print(mahsulot)

# # 14
# sozlamalar = {"til": "uz",
#               "rang_rejim": "tungi",
#               "shrift": "14px",
#               "ovoz": True
# }
# print(sozlamalar)
# sozlamalar.clear()
# print(sozlamalar)

# # 15
# asl_dict = {"a": 1,
#             "b": 2,
#             "c": 3,
#             "d": 4
# }
# print(asl_dict)
# asl_dict.copy()
# print(asl_dict)


# # 16
# maktab = {
#     "10-A": {"o'quvchilar": 25,
#              "sinf_rahbar": "Olimova N."
#     },
#     "10-B": {"o'quvchilar": 28,
#              "sinf_rahbar": "Karimov S."
#     },
#     "11-A": {"o'quvchilar": 22,
#              "sinf_rahbar": "Rahimova D."
#     }
# }
# print(maktab)

# # 17
# maktab = {
#     "10-A": {"o'quvchilar": 25,
#              "sinf_rahbar": "Olimova N."},
#     "10-B": {"o'quvchilar": 28,
#              "sinf_rahbar": "Karimov S."}
# }
# print(maktab)
# print(maktab['10-A'])
# print(maktab)

# # 18
# dict1 = {"a": 1,
#          "b": 2,
#          "c": 3
# }
# print(dict1)
# dict2 = {"c": 10,
#          "d": 4,
#          "e": 5
# }
# print(dict2)
# dict1.update(dict2)
# print(dict1)

# # 19
# atlar = {"UZ": "O'zbekiston",
#              "RU": "Rossiya",
#              "US": "Amerika",
#              "TR": "Turkiya"
# }
# print(atlar)
# for kalit in atlar:
#     print(kalit)


# # 20
# baholar = {"Matematika": 5,
#            "Fizika": 4,
#            "Kimyo": 5,
#            "Biologiya": 4, "Tarix": 5}
# print(baholar)
# for kalit, qiymat in baholar.items():
#     p
#     rint(kalit, ":", qiymat)

# # 21
# shaxs = {"ism": "Jamshid",
#          "yosh": 21,
#          "shahar": "Xorazm"
# }
# print(shaxs)
# shaxs.setdefault()
# print(shaxs)


# # 22
# dict1 = {"a": 1,
#          "b": 2
# }
# print(dict1)
# dict2 = {"c": 3,
#          "d": 4
# }
# print(dict2)
# dict3 = {"e": 5,
#          "f": 6
# }
# print(dict3)
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)
#
# # 24
# narxlar = {
#     "Non": 3000,
#     "Sut": 9000,
#     "Tuxum": 18000,
#     "Go'sht": 85000,
#     "Yog'": 45000,
#     "Sabzi": 7000
# }
# print(narxlar)
# eng_qimmat = max(narxlar, key=narxlar.get)
#
# print("Eng qimmat mahsulot:", eng_qimmat)

# # 25
# matn = "salom dunyo salom python python python dunyo"
# 
# sozlar = matn.split()
# natija = {}
# 
# for soz in sozlar:
#     if soz in natija:
#         natija[soz] += 1
#     else:
#         natija[soz] = 1
# 
# print(natija)
