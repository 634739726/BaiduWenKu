import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WenKu:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def write_to_txt(self, text):
        with open('wenku.txt', 'a', encoding='utf-8') as f:
            f.write(text)

    def run(self):
        opt = webdriver.ChromeOptions()
        print(opt._arguments)
        opt.set_headless()
        print(opt._arguments)
        driver = webdriver.Chrome(options=opt)
        # driver = webdriver.PhantomJS()
        driver.get(self.url)
        driver.execute_script('window.scrollTo(0,3/4*document.body.scrollHeight)')
        time.sleep(0.5)
        try:
            driver.find_element_by_class_name('fc2e').click()
            time.sleep(0.5)
        except:
            pass
        driver.execute_script('window.scrollTo(0,0)')
        page_list = driver.find_elements_by_class_name("reader-page")
        all_y = len(page_list)
        print(len(page_list))
        for i, page in enumerate(page_list):
            time.sleep(1)
            ie_fix = page.find_element_by_class_name('ie-fix')
            onePage = ie_fix.find_elements_by_tag_name('p')
            print(onePage)
            s = ''
            for word in onePage:
                print(word.text)
                if word.text:
                    s += word.text
                else:
                    s += '\n\t'
            self.write_to_txt(s)
            print(i)
            y = 'window.scrollTo(0,'+str(i+1)+'/'+str(all_y)+'*document.body.scrollHeight)'
            driver.execute_script(y)



if __name__ == "__main__":
    url = "https://wenku.baidu.com/view/021a66fe0722192e4536f6e2.html?rec_flag=default&sxts=155185128564"
    wenku = WenKu(url)
    wenku.run()
