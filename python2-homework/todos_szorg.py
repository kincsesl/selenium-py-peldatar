# pclass =
# class = "bit-btn-primary"

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/todo.html")

# Egy-két todó beszúrása

inputmező = driver.find_element_by_xpath("/html/body/div/div/div/form/input[1]")  # Ide egy új todót!
submitgomb = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]")  # Hadd menjen!

for i in range(3):
    todó = str(i+1) + ". újabb meló."
    inputmező.send_keys(todó)
    submitgomb.click()

todo_k = driver.find_elements_by_class_name("done-false") #Elkérem a todókat.


for x in todo_k:
    print(x.text)

driver.close()
