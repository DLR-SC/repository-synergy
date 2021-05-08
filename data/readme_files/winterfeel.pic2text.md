###Pic2Text
A script to transform picture to text, supporting Chinese.</br>

Preview：</br>
![image](preview.jpg)
###Dependencies
* Python 2.7</br>
* PIL or Pillow

###How to use
If you wanna use your own font,copy the font file to your folder and edit the font name in line 27:</br>
```python
  ft = ImageFont.truetype("msyhbd.ttf",fontSize)
```

Then edit the last several lines of codes:</br>
```python
    textList = ['撒','啊','呵','王','一'];
	pic2Text('test.jpg',textList);
```
Remenber to sort characters by Density</br>


###About
不灭的小灯灯</br>
An individual developer</br>
Blog:[www.winterfeel.com](www.winterfeel.com)
