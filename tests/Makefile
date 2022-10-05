MAKE=make
RM=rm
FILE=exploit_me

# Build rules
all: $(FILE)

$(FILE):
	gcc exploit_me.c -o $(FILE)

# Rebuild this project
rebuild: cleanall all

# Clean this project
clean:
	$(RM) -f $(FILE)

# Clean this project and all dependencies
cleanall: clean
