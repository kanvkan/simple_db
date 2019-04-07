# encoding=utf-8
'''
create new class tool
1. add xx.h xx.cc
2. add head SIMPLE_DB_XXX_H
3. add namespace
4. create class template
'''

import sys, os
import re

class NewClass(object):
    '''
    创建类框架
    '''
    def __init__(self, class_name):
        self.class_name = class_name
        self.low_name = NewClass._camel_to_low(class_name)

    @staticmethod
    def _camel_to_low(up_name):
        '''驼峰命名到下划线命名'''
        pattern = "[A-Z]"
        new_name = re.sub(pattern, lambda x : "_" + x.group(0).lower(), up_name)
        return new_name[1:]


    @property
    def head_file_name(self):
        return "%s.h" % self.low_name

    @property
    def cc_file_name(self):
        return "%s.cc" % self.low_name

    @property
    def header_str(self):
        _header_str = ""
        _header_str += "#ifndef SIMPLE_DB_%s_H\n" % self.low_name.upper()
        _header_str += "#define SIMPLE_DB_%s_H\n\n" % self.low_name.upper()
        _header_str += "#include \"common.h\" \n"
        _header_str += "BEGIN_SIMPLE_DB_NS\n\n"
        _header_str += "class %s {\n\n" % self.class_name
        _header_str += "public:\n"
        _header_str += "    %s();\n" % self.class_name
        _header_str += "    ~%s();\n" % self.class_name
        _header_str += "private:\n"
        _header_str += "    %s(const %s&);\n" % (self.class_name, self.class_name)
        _header_str += "    %s& operator=(const %s&);\n" % (self.class_name, self.class_name)
        _header_str += "};\n\n"
        _header_str += "END_SIMPLE_DB_NS\n\n"
        _header_str += "#endif"
        return _header_str

    @property
    def cc_str(self):
        _cc_str = ""
        _cc_str += "#include \"%s\"\n\n" % self.head_file_name
        _cc_str += "BEGIN_SIMPLE_DB_NS\n\n"
        _cc_str += "%s::%s()\n" % (self.class_name, self.class_name)
        _cc_str += "{\n"
        _cc_str += "}\n"
        _cc_str += "%s::~%s()\n" % (self.class_name, self.class_name)
        _cc_str += "{\n"
        _cc_str += "}\n\n"
        _cc_str += "END_SIMPLE_DB_NS\n\n"
        return _cc_str
        



    @property
    def cpp_file_name(self):
        return "%s.cc" % self.low_name

    @staticmethod
    def create_file(file_name, file_str):
        print "Create file [%s]" % file_name
        if os.path.exists(file_name):
            print "file alread exists"
            return

        with open(file_name, "w") as f:
            f.write(file_str)

    def run(self):
        NewClass.create_file(self.head_file_name, self.header_str)
        NewClass.create_file(self.cc_file_name, self.cc_str)
        pass

    
if __name__ == '__main__':
    '''输入为类名，采用驼峰格式
    '''
    if len(sys.argv) != 2:
        print "Error input "
        exit(-1)
    class_name = sys.argv[1]
    NewClass(class_name).run()
    
