
# eggwash
This started as a data cleaning challenge but then friends wanted to use the tools I wrote so now they're here. 

to clone go to your terminal navigate to wherever you want these tools to live and type 

'''
git clone https://github.com/Jef-H/eggwash.git
'''


hey, you're gonna have to prolly install pip it installs libraries that I use. 

https://pip.pypa.io/en/stable/installing/

if you're having issues let me know!

once pip is intalled try calling 


''' 

pip install -r requirements.txt

'''


to run the tools they're the same so you'll do a call like thisl


'''

python combine.py -i yourInputDirectory
  
  
  '''
  
  inputDir = the directory where your csvs are that you want to combine.  you can use relative paths so ../Dataset would be a valid example of input
  
  * please note this assumes all the headers are the same. 
  
  ''' 
  
next, missingValues.py is similar. it just gives you stats on the number of nullls in your dataset. 

python missingValues.py -i yourData.csv
  
  
