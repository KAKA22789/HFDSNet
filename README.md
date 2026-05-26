# HFDSNet
Hyper-Frequency Dynamic-Streams Network for Non-Uniform Real-World Dehazing
### Installation
python = 3.8
pytorch = 2.0
cuda = 11.2
~~~
pip install -r requirements.txt
~~~

### Download the Datasets
- Dense-Haze
- NH-HAZE
- O-HAZE
- I-HAZE
### Train and test on Dense-Haze
~~~
cd Dense-Haze
# train
python main.py --mode train --data_dir your_path/Dense-Haze
# test
python main.py --data_dir your_path/Dense-Haze --test_model your_path/Dense-Haze/Best.pkl
~~~

### Train and test on NH-HAZE
~~~
cd NH-HAZE
# train
python main.py --mode train --data_dir your_path/NH-HAZE
# test
python main.py --data_dir your_path/Dense-Haze --test_model your_path/NH-HAZE/Best.pkl
~~~

### Train and test on O-HAZE
~~~
cd O-HAZE
# train
python main.py --mode train --data_dir your_path/O-HAZE
# test
python main.py --data_dir your_path/Dense-Haze --test_model your_path/O-HAZE/Best.pkl
~~~

### Train and test on I-HAZE
~~~
cd I-HAZE
# train
python main.py --mode train --data_dir your_path/I-HAZE
# test
python main.py --data_dir your_path/Dense-Haze --test_model your_path/I-HAZE/Best.pkl
~~~

########################################################################################


For training and testing, your directory structure should look like this

`Your datapath` <br/>
`├──data_augment.py` <br/>
`├──data_load.py` <br/>
`├──Dense-Haze` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
`└──NH-HAZE` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 
`└──O-HAZE` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 
`└──I-HAZE` <br/>
     `├──train`  <br/>
          `├──gt`  <br/>
          `└──hazy`  
     `└──test`  <br/>
          `├──gt`  <br/>
          `└──hazy` 
