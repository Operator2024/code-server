from argon2 import PasswordHasher
import sys
import re


ph = PasswordHasher()
hash = ph.hash(sys.argv[1])
escaped_hash = re.sub('\$', '$$', hash)