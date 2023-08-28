from programming_language import Language

python = Language("Python", "Dynamic", True, 1991)
ruby = Language("Ruby", "Dynamic", True, 1995)
visual_basic = Language("Visual Basic", "Static", False, 1991)

languages_list = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in languages_list:
    if language.is_dynamic():
        print(language.name)
