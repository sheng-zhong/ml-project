# ml-project
机器学习项目

image-handel文件夹内是检测行人属性的模型（从街头到行人属性数据库）:

    输入：包含行人图片的图像

    输出: 图像中每个行人的结构化属性
    
    该工程项目文件包含的算法: facebook开源的detectron2 + 自己训练的行人结构化属性识别模型

示例输入：

![image](https://github.com/sheng-zhong/ml-project/blob/master/image-handel/test_samples/example.png)

输出:

![image](https://github.com/sheng-zhong/ml-project/blob/master/image-handel/detected_frame/detected-example.png)

for ml-trade:
    describe: predict BTC price every hour dataset flow from exchange house
    input: every hours BTC information (val highest price per hour ...)
    output: highest price next hour
    include algorithm: randomforest, xgboost
