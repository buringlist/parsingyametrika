from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv


def write_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data[0],
                         data[1],
                         data[2],
                         data[3]])
        # writer.writerow([data['date'],
        #                  data['views'],
        #                  data['visits'],
        #                  data['users']])


def pars():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()
    browser.get('http://atmosfera-clinic.ru')

    """click on the metrica"""
    elem = browser.find_element_by_css_selector('#stylef6 > table > tbody > tr >'
                                                ' td > center > a:nth-child(6) > img')
    """remove element that hides click"""
    element = browser.find_element_by_id('yjsg_botpanel')
    browser.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

    elem.click()
    sleep(2)

    """Switch to iframe"""
    iframe = browser.find_element_by_xpath('//*[@id="ym-informer"]/iframe')
    browser.switch_to_frame(iframe)
    """find statistic"""
    statistic_list = browser.find_elements_by_class_name('uniques')

    for i in statistic_list:
        statistic = i.get_attribute('data-list').split(';')
        date = statistic[0]
        views = statistic[2]
        visits = statistic[3]
        users = statistic[4]
        data = [date, views, visits, users]
        # data = {'date': date, 'views': views, 'visits': visits, 'users': users}
        write_csv(data)

    browser.quit()


if __name__ == '__main__':
    pars()