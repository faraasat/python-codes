def funargs(normal, *args, **kwargs):  # normal argument cannot be passed after *args
    print(type(args))
    print(type(kwargs))

    for item in args:
        print(normal, item)
        normal += 1

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "SkillF", "Hammad", "Shivam", "The Programmer"]
normal = 1
kw = {"Rohan":"Monitor", "Harry":"Fitness Trainer", "The Programmer":"Coordinator"}
funargs(normal, *har, **kw)

