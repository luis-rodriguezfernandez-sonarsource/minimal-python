class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    narg=len(sys.argv)
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    if narg == 1:
       print('@Usage: input_filename nelements nintervals')
       break
    a = {}
    try:
        a[5]
    except KeyError:
        raise  # Noncompliant
    pass
    return self

def foo():
    dt = datetime(year=2024, day=66, month=1, hour=16, minute=1) # ValueError: day is out of range for month

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
