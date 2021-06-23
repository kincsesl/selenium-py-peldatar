from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/todo.html")

todo_k = driver.find_elements_by_class_name("done-false")

for x in todo_k:
    print(x.text)

driver.close()
