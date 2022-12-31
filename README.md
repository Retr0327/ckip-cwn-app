# **ckip-cwn-app**

This repository for the [2022 台大自然語言處理與網路應用](https://github.com/lopentu/nlp_web) participants demonstrates how to turn data scripts into shareable web apps.


## **Documentation**
### 1. Installation

1. Python version
   * `python == 3.7.5`

2. Clone repository

    ```bash
    git clone git@github.com:Retr0327/ckip-cwn-app.git
    ```

3. Install Requirement
    ```bash
    cd ./ckip-cwn-app && pip install -r requirements.txt      
    ```


### 2. Start the app
There are two main ways to run the app:

- run with Python 

  First make sure you are in the `ckip-cwn-app` folder, and then simply run:

  ```bash 
  streamlit run src/app.py
  ```

- run with Docker
  
  Install Docker, and user the following command to run:
  
  ```bash
  docker-compose up
  ```

  Then acces `http://localhost` in the browser.


## Contact
If you have any suggestion or question, please do not hesitate to email me at r07142010@g.ntu.edu.tw