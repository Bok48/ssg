# Static Site Generator

## Description
This is a static site generator that creates html files from markdown files.

This is a guided project by Boot.dev. A few pieces of the code, as well as tests has been supplied directly, but most of the project has been supplied pseudocode that has been manually programmed by me.

This generator handles simple markdown to html.

## Specifics
The markdown types it handles includes:
* Header (h1 - h6)
* Paragraph
* Quote
* Unordered list
* Ordered list
* Code (blocks and inline)
* Image
* Link
* Bold text
* Italic text

The generator is not designed to properly handle text with more than one modifier at once. So no text that is both italic *_and_* bold.

## Usage
To use this generator, you will need Python 3.10 installed on your machine.

Put markdown files that are going to be processed in the *content* folder.
Images, css files and other content that does not need any processing should be put into the *static* folder.

When all the files are ready, run *main.sh* in the root of the project to start generating the html files and start up the new website locally.
Alternatively, write `python src/main.py` to only generate the files.

The markdown files in the *content* folder should now be processed into html files and be in the *docs* folder, together with any other files from the *static* folder.
If main.sh was used to run the program, the newly generated webpage should now be running locally on your machine. To see it, open any web browser and enter `http://localhost:8888` into the url field.
If you did not run the main.sh shell script, or you want to simply run the website locally to look at the final result, run this command at the root of the project: `cd docs && python3 -m http.server 8888`.
