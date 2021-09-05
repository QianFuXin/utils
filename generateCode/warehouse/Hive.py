def createTable():
    info = """""".lower()
    return info
def commandLineInterface():
    info = """
hive --help --service cli
usage: hive
-d,--define <key=value>          Variable subsitution to apply to hive
                                  commands. e.g. -d A=B or --define A=B
                                  变量
--database <databasename>     Specify the database to use
    				指定使用某个数据库
-e <quoted-query-string>         SQL from command line
 					执行字符串中的指令
-f <filename>                    SQL from files
 					执行文件中的指令
-H,--help                        Print help information
 					帮助
--hiveconf <property=value>   Use value for given property
    				变量
--hivevar <key=value>         Variable subsitution to apply to hive
                                  commands. e.g. --hivevar A=B
                                  变量                                  	
-i <filename>                    Initialization SQL file
 					指定hive初始化文件
-S,--silent                      Silent mode in interactive shell
 					沉默输出模式 						
-v,--verbose                     Verbose mode (echo executed SQL to the
                                  console)
                                    啰嗦输出模式   
    """.lower()
    return info