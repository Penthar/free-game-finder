from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

def get_current_free_games(): #function to get the current free games in Epic Games
    free_games = [] #output list of games
    os.environ['PATH'] += r"C:/Desktop/selenium_codes" #add path to driver here
    driver = webdriver.Chrome()
    driver.get("https://store.epicgames.com/en-US/")
    driver.implicitly_wait(3)
    games_group = driver.find_element(By.CLASS_NAME, "css-1myhtyb")

    game_cards = (games_group.find_elements(By.CLASS_NAME, "css-aere9z"))

    for i in game_cards:
        if i.get_attribute("innerText")[0]=="F":
            free_games.append(i.get_attribute("innerText").split("\n")[1])
    return free_games


def compare_free_games(current_games, new_games): #function two check if two game lists are same
    return current_games == new_games #if games have not changed, returns true
    #/*******************************/ else returns false


def main():
    free_games = get_current_free_games()
    for game in free_games:
        print("New Free Game! " + game)
    while True:
        time.sleep(3600) #delay between checks in seconds
        if compare_free_games(free_games, get_current_free_games()) == False:
            main()
        


if __name__ == "__main__":
    main()




