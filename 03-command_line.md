# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

Command | Action
------- | ------
`pwd` | show current working directory path
`cd otherdir` | change current working directory path
`mkdir newdir | creating a directory
`rmdir olddir` OR `rm -rf olddir` | deleting a directory
`touch newfile` | creating a file using `touch` command
`rm oldfile` | deleting a file
`mv oldfile newfile` | renaming a file
`ls -a` | listing hidden files
`cp onedir/file otherdir` | copying a file from one directory to another
`cat fileone filetwo > filethree` | concatenating files
`head file` | print the first few lines of a file
`tail file` | print the last few lines of a file


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

Command | Action
------- | ------
`ls`  | List files in current or specified directory
`ls -a`  | Include hidden files
`ls -l`  | Include several attributes about the files
`ls -lh`  | Change the format of the file sizes reported
`ls -lah`  | Combine the last three remarks
`ls -t`  | Sort files listed by time (newest first)
`ls -Glp`  | Add an indicator to directories and remove group info

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

Sigh... sign of the times.  You point folk to a website?  Instead of man?

-A is very useful when scripting.

-F is more robust than -p.

-R is helpful when you want to see a whole directory structure

-r helps with -t.  I often do `ls -lart` to confirm what the last changes were.

-Q helps for scripting since all filenames are quoted, not just those with spaces.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs takes stdin (or a specified file) and arguments to xargs to call (repeatedly if necessary) the
command specified in the argument to xargs (along with arguments passed to that command) with the fields
from the lines from stdin as further arguments to the command.  In essence, it's a more direct way to
flatten and use the data from a list in a particular way.  Depending on what you're doing this could be
done with a while read loop.  But xargs lets you do it in one line.

```bash
$ find dsp | xargs sum
```

That let's you get sumchecks of all the files in the directory, recursively.


 

