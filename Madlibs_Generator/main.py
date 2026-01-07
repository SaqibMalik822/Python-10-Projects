# madlibs generator is a project, 
# which replaces placeholders in a story, with user defined characters

def your_story() -> str:
    story:str = input("choose your story, bunny or snakeandman: ").lower().strip()
    try:
        story == "bunny" or "snakeandman"
    except ValueError:
        print("no such story exists")
        return
    if story == "bunny":
        bunny_name:str = input("enter the name for bunny: ")
        with open("stories/bunnystory.txt", "r") as f:
            content = f.read()
        word = "[BUNNY_NAME]"
        content.replace(word, bunny_name)
        f.close()
        return content
    else:
        man_name:str = input("enter the name for the man: ")
        snake_name:str = input("enter the name for the snake: ")
        with open("./stories/snakemanstory.txt", "r") as f:
            content = f.read()
        word = "[MAN_NAME]"
        content.replace(word, man_name)
        content.replace(word, snake_name)
        f.close()
        return content
print(your_story())