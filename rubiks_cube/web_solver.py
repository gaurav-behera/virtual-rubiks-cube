import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def get_solution(pos):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # opens chrome window in the background and gets solution
    driver = webdriver.Chrome(executable_path="./utils/chromedriver", options=option)
    # driver = webdriver.Chrome(executable_path="./utils/chromedriver")

    driver.get("https://rubiks-cube-solver.com/")  # site used to get solution

    sticker = [0]
    for i in range(1, 55):
        sticker.append(driver.find_element_by_id("sticker" + str(i)))

    count = 1
    color = {'w': 'color1', 'o': 'color2', 'g': 'color3', 'r': 'color4', 'b': 'color5', 'y': 'color6'}
    moves = {"L": "Red clockwise", "R": "Orange clockwise", "F": "Green clockwise", "B": "Blue clockwise", "U": "Yellow clockwise",
             "D": "White clockwise", "L'": "Red anti-clockwise", "R'": "Orange anti-clockwise", "F'": "Green anti-clockwise", "B'": "Blue anti-clockwise",
             "U'": "Yellow anti-clockwise", "D'": "White anti-clockwise", "L2": "Red twice", "R2": "Orange twice", "F2": "Green twice",
             "B2": "Blue twice", "U2": "Yellow twice", "D2": "White twice"}

    for i in range(0, 3):
        for j in range(3, 6):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    for i in range(3, 6):
        for j in range(0, 3):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    for i in range(3, 6):
        for j in range(3, 6):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    for i in range(3, 6):
        for j in range(6, 9):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    for i in range(3, 6):
        for j in range(9, 12):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    for i in range(6, 9):
        for j in range(3, 6):
            driver.execute_script("arguments[0].setAttribute('class',arguments[1])", sticker[count], color[pos[i][j]])
            count += 1

    time.sleep(5)
    element = driver.find_element_by_id("solveCube")
    element.send_keys(Keys.RETURN)

    timeout = 60
    driver.switch_to.window(driver.window_handles[-1])
    solution, solve, text = '', '', ''
    try:
        element_present = EC.presence_of_element_located((By.ID, 'algoritmusHanyadik1'))
        WebDriverWait(driver, timeout).until(element_present)
    except selenium.common.exceptions.TimeoutException:
        text = "Invalid Scramble or page took too long to respond"
    else:
        for i in range(1, 22):
            try:
                alg = driver.find_element_by_id("algoritmusHanyadik" + str(i)).text
                solution = solution + alg + ' '
                solve = solve + str(i) + ') ' + alg + ' : ' + moves[alg] + '\n'
            except selenium.common.exceptions.NoSuchElementException:
                pass
    driver.close()
    return solve, solution, text
