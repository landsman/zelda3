import util, sys

kTextAlphabet_US = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
  "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
  "-", ".", ",", 

  # 64 - 79
  "[...]", ">", "(", ")",
  "[Ankh]", "[Waves]", "[Snake]", "[LinkL]", "[LinkR]",
  "\"", "[Up]", "[Down]", "[Left]",

  # 80 - 95
  "[Right]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
  "[4HeartL]", "[4HeartR]", " ", "<", "[A]", "[B]", "[X]", "[Y]",
]

kTextAlphabet_EU = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", # 0 - 15
  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", # 16 - 31
  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", # 32 - 47
  "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", # 48 - 63
  

  # 64 - 79
  "-", ".", ",",  "[...]", ">", "(", ")",
  "[Ankh]", "[Waves]", "[Snake]", "[LinkL]", "[LinkR]",
  "\"", "[UpL]", "[UpR]", "[LeftL]",


  # 80 - 95
  "[LeftR]", "'", "[1HeartL]", "[1HeartR]", "[2HeartL]", "[3HeartL]", "[3HeartR]",
  "[4HeartL]", "[4HeartR]", " ", "ö", "[A]", "[B]", "[X]", "[Y]", "ü",

  # 96-111
  "ß", ":", "[DownL]", "[DownR]", "[RightL]", "[RightR]", "è", "é", "ê", "à", "ù", "ç", "Ä", "Ö", "Ü", "ä"
  
  # 112-
]

kText_CommandLengths_US = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, ]
kText_CommandNames_US = [
  "NextPic", "Choose", "Item", "Name", "Window", "Number",
  "Position","ScrollSpd", "Selchg", "Unused_Crash", "Choose3",
  "Choose2", "Scroll", "1", "2", "3", "Color",
  "Wait", "Sound", "Speed", "Unused_Mark", "Unused_Mark2", "Unused_Clear",
  "Waitkey"
]

kTextDictionary_US = [
'    ', '   ', '  ', "'s ", 'and ', 
'are ', 'all ', 'ain', 'and', 'at ', 
'ast', 'an', 'at', 'ble', 'ba', 
'be', 'bo', 'can ', 'che', 'com', 
'ck', 'des', 'di', 'do', 'en ', 
'er ', 'ear', 'ent', 'ed ', 'en', 
'er', 'ev', 'for', 'fro', 'give ', 
'get', 'go', 'have', 'has', 'her', 
'hi', 'ha', 'ight ', 'ing ', 'in', 
'is', 'it', 'just', 'know', 'ly ', 
'la', 'lo', 'man', 'ma', 'me', 
'mu', "n't ", 'non', 'not', 'open', 
'ound', 'out ', 'of', 'on', 'or', 
'per', 'ple', 'pow', 'pro', 're ', 
're', 'some', 'se', 'sh', 'so', 
'st', 'ter ', 'thin', 'ter', 'tha', 
'the', 'thi', 'to', 'tr', 'up', 
'ver', 'with', 'wa', 'we', 'wh', 
'wi', 'you', 'Her', 'Tha', 'The', 
'Thi', 'You', 
]


kText_CommandLengths_EU = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
kText_CommandNames_EU = [
  "Selchg", "Choose3", "Choose2", "Scroll", "1", "2", "3",
  "Color", "Wait", "Sound", "Speed", "Mark", "Mark2",
  "Clear", "Waitkey", "EndMessage", "NextPic", "Choose",
  "Item", "Name", "Window", "Number", "Position", "ScrollSpd",
]

kTextDictionary_DE = [
'    ', '   ', '                                          ', '-Knopf', ' ich ', 
' Sch', ' Ver', ' zu ', ' es ', 'aber', 
'alle', 'auch', 'ang', 'aus', 'auf', 
'an', 'bist', 'bin', 'bei', 'der ', 
'die ', 'das ', 'den ', 'dem ', 'daß', 
'der', 'die', 'das', 'den', 'da', 
'etwas', 'ein ', 'ein', 'en ', 'er ', 
'es ', 'en', 'er', 'es', 'ei', 
'für', 'fe', 'habe', 'hier', 'hast', 
'her', 'ich ', 'icht', 'ich', 'ist', 
'ie ', 'im', 'ie', 'kannst ', 'kannst', 
'kommen', 'kann ', 'll', 'mich', 'mein', 
'mit', 'mal', 'mir', 'nicht ', 'nicht', 
'nen', 'nn', 'och ', 'och', 'or', 
'schon', 'sich', 'sein', 'sch', 'sie', 
'st', 'tte', 'te ', 'te', 'und ', 
'und', 'ung', 'um', 'von', 'ver', 
'vor', 'wird', 'zu ', 'Amulett', 'Aber', 
'Deine', 'Dich ', 'Dir ', 'Dir', 'Der', 
'Die', 'Das', 'Du ', 'Du', 'Da', 
'Ein', 'Hyrule', 'Hier', 'Ich ', 'Master-Schwert', 
'Mach', 'Rubine', 'Sch', 'Sie', 'Ver', 
'Weisen', 'Zelda', 
]

class LangUS:
  alphabet = kTextAlphabet_US
  dictionary = kTextDictionary_US
  command_lengths = kText_CommandLengths_US
  command_names = kText_CommandNames_US
  rom_addrs = [0x9c8000, 0x8edf40]
  COMMAND_START = 0x67
  SWITCH_BANK = 0x80
  FINISH = 0xff
  DICT_BASE_ENC, DICT_BASE_DEC = 0x88, 0x88
  def encode_command(self, cmd_index, param):
    name = self.command_names[cmd_index]
    if param == None:
      return [cmd_index + self.COMMAND_START]
    return [cmd_index + self.COMMAND_START, int(param)]

class LangDE:
  alphabet = kTextAlphabet_EU
  dictionary = kTextDictionary_DE
  command_lengths = kText_CommandLengths_EU
  command_names = kText_CommandNames_EU
  rom_addrs = [0x9c8000, 0x8CEB00]
  COMMAND_START = 0x70
  SWITCH_BANK = 0x88
  FINISH = 0x8f
  DICT_BASE_ENC, DICT_BASE_DEC = 0x88, 0x90
  US = False

  kCmdInfo = {
    "Scroll" : (0x80, ),
    "Waitkey" : (0x81, ),
    "1" : (0x82, ),
    "2" : (0x83, ),
    "3" : (0x84, ),
    "Name" : (0x85, ),
    "Wait" : (0x87, {i:i+0x00 for i in range(16)}),
    "Color" : (0x87, {i:i+0x10 for i in range(16)}),
    "Number" : (0x87, {i:i+0x20 for i in range(16)}),
    "Speed" : (0x87, {i:i+0x30 for i in range(16)}),
    "Sound" : (0x87, {45 : 0x40}),
    "Choose" : (0x87, 0x80),
    "Choose2" : (0x87, 0x81),
    "Choose3" : (0x87, 0x82),
    "Selchg" : (0x87, 0x83),
    "Item" : (0x87, 0x84),
    "NextPic" : (0x87, 0x85),
    "Window" : (0x87, {0 : None, 2 : 0x86}),
    "Position" : (0x87, {0: 0x87, 1: 0x88}),
    "ScrollSpd" : (0, {0 : None}),
  }

  def encode_command(self, cmd_index, param):
    info = self.kCmdInfo[self.command_names[cmd_index]]
    if len(info) <= 1 or isinstance(info[1], int):
      assert param == None
      return info
    else:
      assert param != None
      r = info[1][param]
      return (info[0], r) if r != None else ()

kLanguages = {
  'us' : LangUS(),
  'de' : LangDE(),
}

kDialogueFilenames = {
  'us' : 'dialogue.txt',
  'de' : 'dialogue_de.txt',
}

dict_expansion = []

def decode_strings_generic(get_byte, lang):
  info = kLanguages[lang]
  p, rom_idx = info.rom_addrs[0], 1
  result = []
  while True:
    s, srcdata = '', []
    while True:
      c = get_byte(p)
      srcdata.append(c)
      l = info.command_lengths[c - info.COMMAND_START] if c >= info.COMMAND_START and c < info.SWITCH_BANK else 1

      p += l
      if c == 0x7f: # EndMessage
        break
      if c < info.COMMAND_START:
        s += info.alphabet[c]
      elif c < info.SWITCH_BANK:
        if l == 2:
          srcdata.append(get_byte(p - 1))
          s += '[%s %.2d]' % (info.command_names[c - info.COMMAND_START], get_byte(p - 1))
        else:
          s += '[%s]' % info.command_names[c - info.COMMAND_START]
      elif c == info.FINISH:
        return result # done
      elif c == info.SWITCH_BANK:
        p = info.rom_addrs[rom_idx]; rom_idx += 1
        s, srcdata = '', []
      elif c < info.SWITCH_BANK + 8:
        assert 0
      else:
        s += info.dictionary[c - info.DICT_BASE_DEC]
        dict_expansion.append(len(info.dictionary[c - info.DICT_BASE_DEC]))

    result.append((s, srcdata))

  
def print_strings(rom, file = None):
  texts = decode_strings_generic(rom.get_byte, rom.language)
  if len(texts) == 396:
    extra_str = "[Speed 00]0- [Number 00]. 1- [Number 01][2]2- [Number 02]. 3- [Number 03]"
    texts = texts[:4] + [(extra_str, None)] + texts[4:]

  for i, s in enumerate(texts):
    print('%s: %s' % (i + 1, s[0]), file = file)


def encode_greedy_from_dict(s, i, rev, a2i, info):
  a = s[i:]
  if r := rev.get(a[0]):
    for k, v in r.items():
      if a.startswith(k):
        return [v + info.DICT_BASE_ENC], len(k)

  if a[0] == '[':
    cmd, param = a[1:a.index(']')], None
    cmdlen = len(cmd)
    if r := a2i.get(a[:cmdlen+2]):
      return [r], cmdlen+2
    if ' ' in cmd:
      cmd, param = cmd.split(' ', 1)
      param = int(param)
    if cmd not in info.command_names:
      raise Exception(f'Invalid cmd {cmd}')
    i = info.command_names.index(cmd)
    if info.command_lengths[i] != (1 if param == None else 2):
      raise Exception(f'Invalid cmd params {cmd} {param}')
    return info.encode_command(i, param), cmdlen + 2
  else:
    return [a2i[a[0]]], 1

  print('substr %s not found' % a)
  assert 0

def compress_strings(xs, lang = 'us'):
  info = kLanguages[lang]
  rev = {}
  for a,b in enumerate(info.dictionary):
    rev.setdefault(b[0], {})[b] = a
  #rev = {b:a for a,b in enumerate(info.dictionary)}
  a2i = {e:i for i,e in enumerate(info.alphabet)}
  def compress_string(s):
    i = 0
    r = bytearray()
    while i < len(s):
      what, num = encode_greedy_from_dict(s, i, rev, a2i, info)
      r.extend(what)
      i += num
    return r
  return [compress_string(x) for x in xs]
  
def verify(get_byte):
  for i, (decoded, original) in enumerate(decode_strings_generic(get_byte, 'us')):
    c = compress_strings([decoded])[0]
    if c != original:
      print('String %s not match: %s, %s' % (decoded, c, original))
      break
    else:
      pass

def encode_dictionary(lang = 'us'):
  info = kLanguages[lang]
  rev = {b:a for a,b in enumerate(info.alphabet)}
  return [bytearray(rev[c] for c in line) for line in info.dictionary]

if __name__ == "__main__":
  ROM = util.load_rom(sys.argv[1] if len(sys.argv) >= 2 else None, True)

  decoded = decode_strings_generic(ROM.get_byte, 'de')
  print('Total bytes: %d' % sum(len(a[1]) for a in decoded))

  print('Dict tokens: %d' % len(dict_expansion))
  print('Dict save: %d' % (sum(dict_expansion) - len(dict_expansion)))

  print('US size ', len(kTextDictionary_US))
  print('DE size ', len(kTextDictionary_DE))

  texts = [a[0] for a in decoded]


  # Pal seems to have one string too little
  if len(texts) == 396:
    extra_str = "[Speed 00]0- [Number 00]. 1- [Number 01][2]2- [Number 02]. 3- [Number 03]"
    texts = texts[:4] + [extra_str] + texts[4:]

  #for i, s in enumerate(texts):
  #  print('%s: %s' % (i + 1, s), file = None)


  #encode_dictionary()
  compr = compress_strings(texts, 'de')
  print(f'Compressed size (excl eof): {sum(len(a) for a in compr)}')


