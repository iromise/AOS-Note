import frida
session = frida.attach('cat')
#print session.enumerate_modules()[:10]
#print([x.name for x in session.enumerate_modules()[:10]])
print session.enumerate_ranges('r-x')[:10]
