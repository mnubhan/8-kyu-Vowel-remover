def shortcut(s):
  vowel=["a","e","i","o","u"]
  return "".join([x for x in list(s) if vowel.count(x) == 0])

ef shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')

def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s
