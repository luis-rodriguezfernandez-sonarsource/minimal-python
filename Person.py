class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    narg=len(sys.argv)
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    a = {}
    try:
        a[5]
    except KeyError:
        raise  # Noncompliant
    return self

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
