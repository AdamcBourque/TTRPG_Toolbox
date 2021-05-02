## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere


class Spell:

  name = ""
  lvl = 0
  school = ""
  action = ""
  components = (0,0,"")
  duration = ""
  spell_range = ""
  ritual = 0
  description = ""
  
  
  def __init__(self, spell):
    self.name = spell[0]
    self.lvl = spell[1]
    self.school = spell[2]
    self.action = spell[3]
   # self.components = spell[4] + 
    self.duration = spell[7]
    self.spell_range = spell[8]
    self.ritual = spell[9]
    self.description = spell[10]


  def display(self):
    output = ''
    output += self.name + '\n'
    output += "Level " + str(self.lvl) + " "
    output += self.school + " Spell" + '\n'
    output += "Casting Time: " + self.action + '\n'
    output += "Duration: " + self.duration + '\n'
    output += "Range: " + self.spell_range + '\n'
    if (self.ritual == 1):
      output += "Ritual" + '\n'

    def split(word):
      return [char for char in word]
    
    words = split(self.description)
    count = 0
    output += '\n' + '\n'
    for i in words:
      count = count % 70 + 1
      if (i == '\n'):
        count = 0
      output += i
      if (count == 70):
        output += '-' + '\n'

    return output
