## Command Line version of ezReverse

In command line, type:

```python runInvert.py -i {input image path} -o {output path} -s {hsl/lab/yiq} -k {blur/sharpen/None} -g {gamma value}```

to run the app. 

Example: `python runInvert.py -i demo.png -o output.png -s hsl`


## Features:


##### `-h, --help`          	
	
 show this help message and exit

##### ` -i --input `
	
 input image path

#####  `-o --output`	
	
 output image path. 
	default is 'output.png'.

#####  `-s --colorspace`
	
 hsl/lab/yiq. 
	default is hsl

#####  `-k --kernel`
	
 blur/sharpen/None
	default is None

#####  `-g --gamma`
	
 a float equal to gamma value
	default is 1

> Web app: [ezReverse web app](https://amsterdamstudygroup.shinyapps.io/ezreverse/)
Manuscript: [bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.05.27.594095v1)
Original project: ：[ezReverse github](https://github.com/Morwey/ezreverse)
