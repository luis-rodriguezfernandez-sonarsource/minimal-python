class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    if self.name <> self.age:
       print('Noncompliant: the operator "<>" is deprecated.')

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

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
