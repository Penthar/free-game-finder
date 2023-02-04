# freeGames
python script that notifies you every time a new game is free on Epic Games

To run this script on your computer, you must install a web driver up to date with your browser.

If you are using chrome, you may download a web driver [here](https://chromedriver.storage.googleapis.com/index.html)

After you've installed the driver, add the path to it in the get_current_free_games fucntion:

```yaml
def get_current_free_games(): #function to get the current free games in Epic Games
    free_games = [] #output list of games
    os.environ['PATH'] += r"C:/Desktop/selenium_codes" #add path to driver here
```
Then, simply run the code. I set it to run a check once an hour, but you can change the timing in the main function.
