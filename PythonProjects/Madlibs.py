verb = []
noun = []


name = (input("enter a name "))
sp = (input("enter a super-power "))
clothes = (input("enter an article of clothing "))
adj = (input("enter an adjective "))

for i in range(0, 6):
    text2 = (input("enter a verb "))
  
    verb.append(text2)

for i in range(0, 2):
    text3 = (input("enter a noun "))
  
    noun.append(text3)

print("Once upon a time, there was a",adj,"superhero named",name,"Every morning,",name,"would wake up early and",verb[0],"to get ready for the day. First,",name,"would put on their",clothes,"and then",verb[1],"to the kitchen to make breakfast. \nAfter breakfast,",name,"would check their",noun[0],"to see if any new crimes had been reported. \nIf there was trouble in the city,",name,"would quickly",verb[2],"to the scene to save the day. Sometimes,",name,"would have to",verb[3],"villains or use their",sp,"to stop them. \nIn the afternoon,",name,"would take a break from crime-fighting to",verb[4],"with their superhero friends. They would talk about their latest adventures and share tips on how to be a better superhero. \nAs the sun started to set,",name,"knew it was time to get back to work. They would patrol the city streets, looking out for any signs of trouble. And when they saw something amiss,",name,"would leap into action and save the day once again. \nFinally, when the night was over,",name,"would return home and",verb[5],"into bed. They would dream of",noun[1],"and hope for a peaceful day tomorrow.")
