# Adyogi Assignment
Instruction: To run this project on linux system you need linux, python3 and virtualenv packages on system
# steps to follow
> Open terminal
> install pip on system so that python packages can be installed.
  to install pip use command `use sudo apt-get install python3-pip`
> Now Install virtualenv with command`sudo pip3 install virtualenv`
> Now Create a new virtualenv for the project with command`virtualenv venv`.
> As next step Activate your virtualenv Command `source venv/bin/activate`
> Install all dependency using req.txt file
  to do this use command `pip3 install -r req.txt`
  
Setup has been done here, now try to run the project. Go to project directory where manage.py file exist and follow below instruction.
step1. start server using 'python manage.py runserver'
step2. Open browser and hit following url
  'http://127.0.0.1:8000/product/1' will fetch product with id=1
step3. On the same url a new product can be created and can be deleted.

# To view tables and data at project admin use following steps
1. url: http://127.0.0.1:8000/admin/
2. credential: user= mhimanshu, password= adyogi@123
3. you'll have multiple db table as a list, you can access those table and its data too.

# Note: aws rds will be inactive in 48 hrs
