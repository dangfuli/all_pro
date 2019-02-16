# coding=utf-8
from selenium import webdriver

URL = "https://liebaodaikuan.com/"
from PIL import Image
from PIL import ImageEnhance
import pytesser3,time,os
# drider = webdriver.Chrome()
# drider.get(URL)


def processVerCode(driver,verCodeImgPath, ID=None, Class=None, css=None, link_text=None, xpath=None):
    ## 先判断传入的图片路径是否存在
    if os.path.exists(verCodeImgPath):
        ## 需要保存的路径存在，拼接验证码图片的路径名称
        _codeImgPath = os.path.join(verCodeImgPath,'verifyCode.png')
    else:
        print('传入路径错误，检查传入路径')
        raise Exception
    if ID != None:
        ID = str(ID)
        # 获取验证码的x，y
        imageEle = driver.find_element_by_id(ID)
    if Class != None:
        Class = str(Class)
        # 获取验证码的x，y
        imageEle = driver.find_element_by_class_name(Class)
    if css != None:
        css = str(css)
        # 获取验证码的x，y
        imageEle = driver.find_element_by_css_selector(css)
    if link_text != None:
        link_text = str(link_text)
        # 获取验证码的x，y
        imageEle = driver.find_element_by_link_text(link_text)

    if xpath != None:
        xpath = str(xpath)
        # 获取验证码的x，y
        imageEle = driver.find_element_by_xpath(xpath)

    location = _codeImgPath.location
    # 获取size
    size = _codeImgPath.size
    codeRange = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                      int(location['y'] + size['height']))
    # 打开jpg图片
    imageTemp = Image.open(_codeImgPath)

    imageFrame = imageTemp.crop(codeRange)  # 截取验证码图片区域

    imageFrame.save(_codeImgPath)
    time.sleep(2)
    image = Image.open(_codeImgPath)
    image = image.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像

    ImageEnhance.Contrast(image)  # 对比度增强
    threshold = 80  # 设定阈值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # print(table)
    image = image.point(table, '1')

    # image = image.convert('RGBA')
    # picData = image.load()
    # for y in range(image.size[1]):
    #     for x in range(image.size[0]):
    #         # 循环图像里的每一个像素。每个像素为一个长度为4的列表。因为图片转换成RGBA模式，所以列表长度为4，A就是透明度
    #         if picData[x, y][0] > 80 and picData[x, y][1] > 80 and picData[x, y][2] > 80 and picData[x, y][3] > 80:
    #             picData[x, y] = (255, 255, 255, 0)
    #         else:
    #             picData[x, y] = (0, 0, 0, 0)
    # image.resize((500,400))
    # image.show()

    result = pytesser3.image_to_string(image).replace(' ', '').replace('"', '').replace('-', '').replace('.',
                                                                                                         '').replace(
        '`', '').replace(';', '')
    print(result)
    return result
if __name__ == '__main__':
    verCodeImgPath = r'C:\Users\dangfuli_v\Desktop'
    a = '1'
    processVerCode(a,verCodeImgPath)