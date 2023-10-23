import click
@click.group 
def mycommands ():
    pass

@click.command
@click.option("--name", prompt = "Enter your name :", help="the name of the user")
def hello (name):
    click.echo(f"hello {name} !")



PRIORITIES ={ 
    "o": "Optional",
    "l": "low" ,
    "m": "medium",
    "h": "high",
    "c": "crucial"

}
@click.command()
@click.argument("priority", type = click.Choice(PRIORITIES.keys()), default ="m")
@click.argument("todofile", type = click.Path(exists=False))
@click.option("-n","--name", prompt ="Enter the todoname", help ="The name of todo item")
@click.option("-d","--desc", prompt ="Describe the todo", help ="The description of the todo item")
def add_todo(name , desc , todofile):
    filename = todofile if todofile is not None else "mytodo.txt"
    with open (filename ,"a+") as f :
        f.write(f"{name}: {desc} [Priority : {PRIORITIES : [priority]}]")



@click.command
@click.argument("idx", type = int )
def delete_todo(idx):
    with open("mytodo.txt", "r") as f :
        todo_list = f.read().splitlines
        todo_list.pop(idx)
    with open ("mytodo.txt","m") as f :
        f.write("\n".join(todo_list))
        f.write("\n")   



@click.command
@click.option("-p","--priority", type = click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type = click.Path(exists=True))
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodo.txt"
    with open(filename , "r")as f :
        todo_list= f.read().splitlines()
    if priority is None :
        for idx , todo in enumerate(todo_list):
            print (f"({idx})- {todo}")   
    else:
        for idx , todo in  enumerate(todo_list):
            if f"[Priority :{PRIORITIES[priority]}]" in todo :
                 print (f"({idx})- {todo}")  





mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)


if  __name__ == "__main__":
    mycommands()






































































