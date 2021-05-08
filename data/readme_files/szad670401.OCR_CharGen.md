# 用于OCR训练的字符样本生成工具
A tools can generate samples for OCR trainning.

### 生成的字符样张：
![](./samples/01/04.jpg)
![](./samples/02/04.jpg)
![](./samples/03/04.jpg)
![](./samples/04/04.jpg)
![](./samples/05/04.jpg)
![](./samples/06/04.jpg)
![](./samples/08/04.jpg)
![](./samples/09/04.jpg)
![](./samples/10/04.jpg)
![](./samples/11/04.jpg)
![](./samples/12/04.jpg)
![](./samples/13/04.jpg)
![](./samples/15/04.jpg)
![](./samples/16/04.jpg)
![](./samples/17/04.jpg)
![](./samples/18/04.jpg)
![](./samples/19/04.jpg)
![](./samples/20/04.jpg)
![](./samples/21/04.jpg)
![](./samples/22/04.jpg)
![](./samples/23/04.jpg)
![](./samples/24/04.jpg)
![](./samples/25/04.jpg)
![](./samples/26/04.jpg)
![](./samples/27/04.jpg)
![](./samples/28/04.jpg)
![](./samples/29/04.jpg)
![](./samples/30/04.jpg)
![](./samples/31/04.jpg)
![](./samples/32/04.jpg)
![](./samples/33/04.jpg)
![](./samples/34/04.jpg)
![](./samples/35/04.jpg)
![](./samples/36/04.jpg)
![](./samples/37/04.jpg)
![](./samples/38/04.jpg)
![](./samples/39/04.jpg)
![](./samples/40/04.jpg)
![](./samples/41/04.jpg)
![](./samples/42/04.jpg)
![](./samples/43/04.jpg)
![](./samples/44/04.jpg)
![](./samples/45/04.jpg)
![](./samples/46/04.jpg)
![](./samples/47/04.jpg)
![](./samples/48/04.jpg)
![](./samples/49/04.jpg)
![](./samples/50/04.jpg)
![](./samples/51/04.jpg)
![](./samples/52/04.jpg)
![](./samples/53/04.jpg)
![](./samples/54/04.jpg)
![](./samples/55/04.jpg)
![](./samples/56/04.jpg)
![](./samples/57/04.jpg)
![](./samples/58/04.jpg)
![](./samples/59/04.jpg)
![](./samples/60/04.jpg)
![](./samples/61/04.jpg)
![](./samples/62/04.jpg)
![](./samples/63/04.jpg)
![](./samples/64/03.jpg)
### 需要的依赖：
+ opencv-python
+ pillow
+ numpy
+ PIL

### 使用方法：
+ genSamples 构造函数
	+ chineseFontpath 车牌中文字体的路径
	+ EnglishFontPath 车牌英文字体的路径

+ genImage 渲染生成一张样本
	+ id 用于生成字符索引 [0,30] 为汉字 [31，41] 为数字 [42,64] 为英文大写字符
	+ tranformFactor 形变程度 为了使分类器具有较好抗扭曲性应该对其生成的字符进行一定程度的形变。这里建议的值是  5-10。 越大形变程度越大
	+ shadeSize 遮罩尺寸 能使字符
	+ shadeFilter 排除添加遮罩的字符
	+ smuFilter 排除添加污迹的字符
	+ blur 模糊卷积核大小程度
	+ rotFilter 排除形变的字符
	+ blurFilter_level1 削弱模糊的字符
	+ blurFilter_level2 排除模块的字符
	+ size 输出尺寸
	
+ genBatch 批量生成
	+ batchSize 每批的尺寸 如果是 1000 就是每个字符 1000 张
	+ charRange 字符范围 如 range(65) ,range(0,31)
	+ outputPath 输出路径
	+ ...同上

### 字符索引表：
index = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10, "浙": 11, "皖": 12,
         "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20, "琼": 21, "川": 22, "贵": 23, "云": 24,
         "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30, "0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36,
         "6": 37, "7": 38, "8": 39, "9": 40, "A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48,
         "J": 49, "K": 50, "L": 51, "M": 52, "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60,
         "W": 61, "X": 62, "Y": 63, "Z": 64};
         
### 作者：
+ Jack Yu

