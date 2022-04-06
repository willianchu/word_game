import random

database = {
              "stories": [
                {"story": "And the three little pigs run out into the element1 and lock the door with element2.",
                "element1": "place",
                "element2": "object"},
                {"story": "And the prince came at the element1 and gave a wake up kiss in element2",
                "element1": "place",
                "element2": "person"},
                {"story": "With element1 Dark Vader cuts element3's right hand and said - element3 I'm your element2",
                "element1": "object",
                "element2": "degree of kinship",
                "element3": "person"}
              ]
            }

def whichArticle(word): # Defines whe is use "a" or "an"
  firstCharacter = word[:1].lower() 
  if firstCharacter in "aeiou":
    return "an "
  else:
    return "a "

def tellTheStory(story, storyHeader):
  phrase = story["story"]
  for element in storyHeader:
    if element != "story":
      phrase = phrase.replace(element,story[element])
  return phrase

def askQuestions(story, storyHeader):
  for element in storyHeader:
    if element != "story":
      answer = input("Type " + whichArticle(story[element]) + story[element] + " :")
      if story[element] == "object":
        story[element] = whichArticle(answer) + answer
      else:
        story[element] = answer
  return story

def wordGame(database):
  dataHeader = list(database.keys())[0]
  data = database[dataHeader] # retrieves the array of objects
  story = data[random.randrange(0,len(data))]
  storyHeader = list(story.keys())
  story = askQuestions(story,storyHeader)
  return tellTheStory(story,storyHeader)
  

print(wordGame(database))

