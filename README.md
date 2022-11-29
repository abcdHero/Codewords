
# Codewords

A question & answer game for everyone to enjoy.


## Features

- Question Customisation
- Readablity
- Cross platform


## Authors

- [@abcdHero](https://www.github.com/abcdHero)


## Documentation

[- Official Documentation](https://linktodocumentation)


## Feedback

If you have any feedback, please reach out to us at abcdHero@abcdHero.com


## Running Tests

To run tests, run the following command

```bash
  debug n *
```


## Customisation

Open the Folder and create a new file named
```bash
yourname.txt
```
Add the questions there in this format.
```bash
Yourquestion here?|.|Answer Here|.|Explaination Here
(Give the user an explaination of why the answer is.)
```


Now, go in the python code,
```python
'''
██╗░░░██╗░█████╗░██████╗░██╗██████╗░██╗░░░░░███████╗░██████╗
██║░░░██║██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔════╝██╔════╝
╚██╗░██╔╝███████║██████╔╝██║██████╦╝██║░░░░░█████╗░░╚█████╗░
░╚████╔╝░██╔══██║██╔══██╗██║██╔══██╗██║░░░░░██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║░░██║██║░░██║██║██████╦╝███████╗███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝╚═════╝░
'''

questionfile = "yourname.txt"
token = 00000000
```
Find this and rename the questionfile varible.


TOKEN CHANGING:

If you want to change the token, (it is to make the program run)
Find the Varibles section and change the token.
If you dont know your token, run the program, it will show up.