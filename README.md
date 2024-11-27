# Here I started learning Python program
1. We can run Python in multiple platforms: 
   a) command line interface
	 b) Git Bash
	 c) IDLE shell
	 d) notepad++
	 e) Visual studio
2. Today I have written one simple hello world program and pushed it into git repo
   Process:
•	Clone the repo into the local
   	git clone https://github.com/singithamdhana/Python-for-DevOps.git
•	Create a new branch develop/feature
	git checkout -b develop
•	validate branch name
	git branch
•	create new file with extension .py (first.py)
•	then write simple print statement
•	save the file and open terminal
•	go to the file path and run the file
	python first.py
•	It will print the output
•	Now, Push code from local to git by using following commands
	git status   (it will show added/modified file list)
	git add first.py  (add the file)
	git commit -m "writting first program" (add comment)
	git push --set-upstream origin develop (for first commit)
	note: next commit onwards just run 
	git push
•	Go to the git repo refresh the page and check it in develop branch



