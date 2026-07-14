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
    <h1 className="title red-300">this is the app ROOT</h1>
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

function Comp_number_{str(num)} (){ {function_content} }"""



def Page_default_content(num):
    page_content=f"""
 return (
    <div>
      <h1>Page {str(num)}</h1>
      <p>Welcome to the page {str(num)}</p>
    </div>
  );
"""
    print("adding PAGE defualt content")
    return f"""
import React from 'react';

const page_{str(num)} = () => {{page_content}};

export default page_{str(num)};
"""


def config_tailwind():
    print("configuring tailwind into tailwind.config.js")
    return""" 
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
"""

def Adding_Tailwind_Directives_into_index_stylesheet():
    print("Adding Tailwind Directives into index.css")
    return"""
@tailwind base;
@tailwind components;
@tailwind utilities;
 """

def backend_page_content(page_name):
   print(f"writing the backend {page_name} PAGE content")
   return f""" 
export const metatags={'{'}title:{page_name},description:'none'{'}'}

export default function PAGE_{page_name}(){'{'}

return(
<section className="bg-green w-full m-5">
<h1 >{page_name} PAGE</h1>
<section>)


{'}'}

"""



def backend_MODEL_page_content(model_name):
   print("writing the backend PAGE content")
   return""" 

"""


def backend_layout_content():
   print("writing the backend LAYOUT content")
   return f""" 
export const metatags={'{'}title:'layout',description:'none'{'}'}

export default function PAGE_layout(){'{'}

return(
<section className="bg-green w-full m-5">
<h1 >LAYOUT MODEL</h1>
<section>)


{'}'}

"""






def Rearranging_BACKEND_files(dir_name):
    print("Rearranging BACKEND files")
    change_path(dir_name+"/app")
    #createing pages directory and moving into it
    create_path("PAGES")
    change_path("PAGES")
    
    while True:
      making_an_obj_model=input("Add an object name(or x to Exit):")
      
      #if making_an_obj_model == 'x':break;
      print("Creating an object name of "+making_an_obj_model)
      create_path(making_an_obj_model)
      create_path(making_an_obj_model+"/[code]")
      os.system("nul>"+making_an_obj_model+"/[code]/page.js")
      os.system("nul>"+making_an_obj_model+"/[code]/layout.js")
      os.system("nul>"+making_an_obj_model+"/page.js")
      os.system("nul>"+making_an_obj_model+"/layout.js")

         


      page_write=open(making_an_obj_model+"/page.js",'w+')
      page_write.write(backend_MODEL_page_content(making_an_obj_model))
      page_write.close()

      page_write=open(making_an_obj_model+"/[code]/page.js",'w+')
      page_write.write(backend_MODEL_page_content(making_an_obj_model))
      page_write.close()


      page_write=open(making_an_obj_model+"/layout.js",'w+')
      page_write.write(backend_layout_content())
      page_write.close()
         
         
      page_write=open(making_an_obj_model+"/[code]/layout.js",'w+')
      page_write.write(backend_layout_content())
      page_write.close()


         
      

    change_path("..")
    

    create_path("COMPONENTS")

    change_path("../..")
    
    





while True:
    project_frontend_tech_type=input("select the project type (R:react)(A:angular)......(x:exit):")
    project_name=input("wrtie the project name:")
    project_comps=int(input("add amount of compounents:")) 
    project_pages=int(input("add amount of Pages:")) 
    write_command("node -v")
    if project_frontend_tech_type =="r" or project_frontend_tech_type =="R" :
      create_path(project_name)
      change_path(project_name)
      write_command(f"npx create-react-app frontend")
      write_command("npm install -D tailwindcss postcss autoprefixer")
      write_command("npx tailwindcss init")
      change_path('frontend')
      
      comp_model=open(f"src/App.js",'w')
      comp_model.write(src_defult_content())
      comp_model.close()

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

          page_model=open(f"src/tailwind.config.js",'w')
          page_model.write(config_tailwind())
          page_model.close()

          page_model=open(f"src/index.css",'w')
          page_model.write(Adding_Tailwind_Directives_into_index_stylesheet())
          page_model.close()
          #change_path("..")
      #write_command("npm start")

      change_path("..")
      
    
    

    elif project_frontend_tech_type =="a" or project_frontend_tech_type =="A" :
      print("create an Angular project.....")
      write_command("ng new frontend")
      write_command("npm install -D tailwindcss postcss autoprefixer")
      
    else:break
    project_backend_tech_type=input("select the project backend type (nex:next.js)(nes:nest.js)......(x:exit):")
    if project_backend_tech_type =="nex" or project_backend_tech_type =="NEX" :
      print("creating an next.js project.....")
      write_command("npx create-next-app@latest backend")
      Rearranging_BACKEND_files("backend")
    elif project_backend_tech_type =="nes" or project_backend_tech_type =="NES" :
      print("creating an nest.js project.....")
      write_command("nest new backend")
    else:break
      






node_command=os.path.exists("node")

if node_command :
    print("found")
else:
    print("no its not")
