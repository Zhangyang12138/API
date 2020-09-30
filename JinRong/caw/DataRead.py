'''
读写文件类（读配置文件）
'''
import configparser

import os

import yaml


class DataRead:
    def get_project_path(self):
        '''
        获取当前工程路径
        :return:
        '''
        current_file_path=os.path.realpath(__file__)
        # print(current_file_path)#C:\Users\Administrator\PycharmProjects\API\JinRong\caw\DataRead.py
        dir_name=os.path.dirname(current_file_path)
        # print(dir_name)#C:\Users\Administrator\PycharmProjects\API\JinRong\caw
        dir_name=os.path.dirname(dir_name)
        return dir_name+"\\"
    def read_ini(self,file_path,key):
        '''
        读取ini文件，返回key对应的value值
        :param file_path:文件路径,相对路径
        :param key: key
        :return:    key对应的value
        '''
        real_file_path=self.get_project_path()+file_path
        config=configparser.ConfigParser()
        config.read(real_file_path)#读取ini配置文件
        value=config.get("env",key)#读取[env]里面的key
        return value

    def read_yaml(self,file_path):
        '''
        读取yaml文件
        :param file_path: 文件的路径，相对路径
        :return: yaml文件的内容
        '''
        real_file_path=self.get_project_path()+file_path
        with open(real_file_path,"r",encoding="UTF-8")as  f:
            file_content=f.read()
            #用yaml的load方法把文本的文件内容转成字典的list
        content=yaml.load(file_content,Loader=yaml.FullLoader)
        return content




if __name__=='__main__':
    # value=DataRead().read_ini(r"data_env\env.ini","url")
    # print(value)
    # print(DataRead().get_project_path())

    c=DataRead().read_yaml("data_case\\register_fail.yaml")
    print(c)

