files = ['font', '1.png', '10.jpg', '11.gif',
         '2.jpg', '3.png', 'table.xslx', 'spec.docs']


print([ file for file in files if file[-4:] in ['.png' ,'.jpg']])


