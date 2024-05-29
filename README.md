## Command Line version of ezReverse

In command line, type `./runInvert.py -i {input image path} -o {output path} -s {hls/lab/yiq} -k {blur/sharpen/edge/None} -g {gamma value}` to run the app. 

Example: `./runInvert.py -i demo.png`


## Command:


##### `-h, --help`          	
	
 show this help message and exit

##### ` -i --input `
	
 input image path

#####  `-o --output`	
	
 output image path. 
	default is 'output.png'.

#####  `-s --colorspace`
	
 hls/lab/yiq. 
	default is hls

#####  `-k --kernel`
	
 blur/sharpen/edge/None
	default is None

#####  `-g --gamma`
	
 a float equal to gamma value
	default is 1

> Web app: [ezReverse web app](https://amsterdamstudygroup.shinyapps.io/ezreverse/)
Manuscript: [bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.05.27.594095v1)
Original project: ：[ezReverse github](https://github.com/Morwey/ezreverse)
