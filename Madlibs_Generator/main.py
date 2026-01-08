# madlibs generator is a project, 
# which replaces placeholders in a story, with user defined characters

def your_story() -> str:
    story:str = input("choose your story, bunny or snakeandman: ").lower().strip()
    if(story not in ("bunny","snakeandman")):
        return f"{story} no such story exists"
    if story == "bunny":
        bunny_name:str = input("enter the name for bunny: ")
        with open("stories/bunnystory.txt", "r") as f:
            content = f.read()
            word = "[BUNNY_NAME]"
            content = content.replace(word, bunny_name)
            f.close()
        return content
    else:
        man_name:str = input("enter the name for the man: ")
        snake_name:str = input("enter the name for the snake: ")
        with open("./stories/snakemanstory.txt", "r") as f:
            content = f.read()
            word = "[MAN_NAME]"
            word2 = "[SNAKE_NAME]"
            content = content.replace(word, man_name)
            content = content.replace(word2, snake_name)
            f.close()
        return content
print(your_story())