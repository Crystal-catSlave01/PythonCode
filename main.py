def Hi(name, age):
  return "Hi, name age years old"

hello = Hi("someone", "100")
print(hello)

def Hi_1(name, age):
  return f"Hi, {name} {age} years old"
# "(스트링)" 앞에 f(format) 붙이고 {로} 감싸기
# return "Hi, " + name + " " + age " years old"

hello1 = Hi_1("someone", "100")
#Hi("age = 100, name = someone")
print(hello1)