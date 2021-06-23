from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/filltablewithsum.html")

id_k = ["product", "quantity", "price"]
belevalók = []
belevalók.append(["Árvíztűrő tükörfúrógép", "2", "19.2"])
belevalók.append(["Zabhegyező", "3", "9.2"])
submit = driver.find_element_by_id("add")

for i in range(len(belevalók)):
    for j in range(len(belevalók[i])):
        print(i, j, belevalók[i][j], id_k[j])
        mező = driver.find_element_by_id(id_k[j])
        mező.clear()
        mező.send_keys(belevalók[i][j])
    submit.click()

# driver.close()
