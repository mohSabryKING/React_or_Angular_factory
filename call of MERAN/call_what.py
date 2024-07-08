import os,shutil

node_v=os.system("node -v")

while True:
     
 get_tec=input("select a techenology React(r) or Angular(a)....exite(x):")

 if get_tec == 'r':
      print("you called React.js")
      #npx create-next-app@latest
      call_now=os.system("npx create-next-app@latest")
 elif get_tec == 'a':
      print("you called Angular.js")
      add_ang=input("make a name to your angular app:")

      call_now=os.system("ng new "+add_ang)
      call_now=os.system("ng serve")
 elif get_tec == 'x':exit()
 else:print("try agin")