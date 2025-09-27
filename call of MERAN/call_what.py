import os

def write_command(com):
    return os.system(com)

def change_path(dir):
    return os.chdir(dir)

def create_path(dir):
    return os.mkdir(dir)



def src_defult_content():
    print("changeing the src content")
    return"""
import logo from './logo.svg';
import './App.css';

function App() {
  return (
   <main>
    <h1 className="title">this is an app model</h1>
   </main>
  );
}

export default App;


"""

def comp_obj_default_content(num):
    function_content=f"""
 return (
    <div className="comp_model">
      <h1>comp number {str(num)}</h1>
      <p>This is a functional component.</p>
    </div>
  );
"""
    print("adding COMPUNENT defualt content")
    return f"""
import React from 'react';

function Comp_number_{str(num)} () {function_content}
"""



def Page_default_content(num):
    page_content="{"+f"""
 return (
    <div>
      <h1>Page {str(num)}</h1>
      <p>Welcome to the page {str(num)}</p>
    </div>
  );
"""+"}"
    print("adding PAGE defualt content")
    return "{"+f"""
import React from 'react';

const page_{str(num)} = () => {
 page_content
};

export default page_{str(num)};
"""+"}"



while True:
    project_tech_type=input("select the project type (R:react)(A:angular)......(x:exit):")
    project_name=input("wrtie the project name:")
    project_comps=int(input("add amount of compounents:")) 
    project_pages=int(input("add amount of Pages:")) 
    write_command("node --v")
    if project_tech_type =="r" or project_tech_type =="R" :
      write_command(f"npx create-react-app {project_name}")
      change_path(project_name)
      for c in range(project_comps):
          create_path(f"src/comp_{str(c)}")
          write_command(f"nul>src/comp_{str(c)}/comp_obj.js")
          write_command(f"nul>src/comp_{str(c)}/style.css")
          comp_model=open(f"src/comp_{str(c)}/comp_obj.js",'w')
          comp_model.write(comp_obj_default_content(c))
          comp_model.close()
          #change_path("..")
      for p in range(project_pages):
          create_path(f"src/page_{str(p)}")
          write_command(f"nul>src/page_{str(p)}/page_obj.js")
          write_command(f"nul>src/page_{str(p)}/style.css")
          page_model=open(f"src/page_{str(p)}/page_obj.js",'w')
          page_model.write(Page_default_content(p))
          page_model.close()
          #change_path("..")
      write_command("npm start")

      change_path("..")

    elif project_tech_type =="a" or project_tech_type =="A" :
      print("not avilable")
    else:break






node_command=os.path.exists("node")

if node_command :
    print("found")
else:
    print("no its not")
