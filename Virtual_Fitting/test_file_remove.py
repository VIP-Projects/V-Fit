import os

def DeleteFiles(path):
    if os.path.exists(path):
        for file in os.scandir(path):
            os.remove(file.path)
            print("File Remove")
            return 0
        else:
            print("File not Find")
            return 0

DeleteFiles('./ACGPN/Data_preprocessing/test_color/')
    
# if os.path.exists('/home/jykim/JY_project/Project/Fashine/ACGPN/Data_preprocessing/test_color/*.png'):
#     print("clear")
#     # os.remove('ACGPN/Data_preprocessing/text_color/*')